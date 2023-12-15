from fastapi import Depends, FastAPI, Response, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 로그인 관련
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm import Session

# db관련 import
from model import Base, User
from database import SessionLocal, engine
from crud import db_register_user
# from schema

app = FastAPI()

# 프론트엔드 파일 정적 파일로 서빙하기
app.mount("/static", StaticFiles(directory="static"), name="static")
# template
templates = Jinja2Templates(directory="templates")

# db가져오기
Base.metadata.create_all(bind=engine)

class NotAuthenticatedException(Exception):
    pass

SECRET_KEY = "super-secret-key"
manager = LoginManager(SECRET_KEY, "/login", use_cookie=True, 
                            custom_exception=NotAuthenticatedException)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 2.2. 쿠키가 없으면 자동으로 여기가 실행됨
@app.exception_handler(NotAuthenticatedException)
def auth_exception_handler(req: Request, exc: NotAuthenticatedException):
    """
    Redirect user to the login page if not logged in
    """
    print("Entered Here")
    return templates.TemplateResponse("login.html",{"request":req})

# 2.1. 쿠키가 있으면 db에서 username에 해당하는 객체를 가져온다.
@manager.user_loader()
def get_user(username: str, db: Session = None):
    if not db:        
        with SessionLocal() as db:
            return db.query(User).filter(User.username == username).first()    
    return db.query(User).filter(User.username == username).first()

# #1. loginManager는 쿠키가 있는지 확인한다.
@app.get("/")
def get_root(req: Request, user=Depends(manager)):
    return templates.TemplateResponse("main.html",{"request":req})

#1. 로그인하기    
@app.post('/login')
def login(response: Response, data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    
    user = get_user(username)
    if not user:
        print("Not found user")
        raise InvalidCredentialsException
    if user.password != password:
        print(user.password)
        print(password)
        print("Not found password")
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data = {'sub': username}
    )
    manager.set_cookie(response, access_token)
    # return {'access_token': access_token}
    return RedirectResponse(url="/main.html")

#2. 등록하기
@app.post('/register')
def register_user(response: Response,
                  data: OAuth2PasswordRequestForm = Depends(),
                  db: Session = Depends(get_db)):
    username = data.username
    password = data.password
    
    user = db_register_user(db, username, password)
    if user:
        access_token = manager.create_access_token(
            data = {'sub': username}
        )
        manager.set_cookie(response, access_token)
        return RedirectResponse(url="/main.html")
    else:
        return "Failed"
    
