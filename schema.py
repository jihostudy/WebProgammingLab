from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 사용자 데이터 정의
class UserSchema(BaseModel):
    id: Optional[int] #Optional : 선택적 데이터
    username: Optional[str]
    password: Optional[str]
    
    # ORM 모드에서 작동하도록 도와준다
    class Config:
        orm_mode = True

