from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    # email = Column(String, unique=True, index=True) 
    
    # FRIENDSHIP 관계
    friends = relationship("FRIENDSHIP",back_populates="user")
    
    # CHAT 관계
    sent_chats = relationship("CHAT", back_populates="sender")


class Friendship(Base):
    __tablename__ = "FRIENDSHIP"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("USERS.id"))
    friend_id = Column(Integer, ForeignKey("USERS.id"))

    # user 관계
    user = relationship("USER", back_populates="friends",foreign_keys=[user_id])

    # friend 관계
    friend = relationship("USER", back_populates="friends", foreign_keys=[friend_id])

class Chat(Base):
    __tablename__ = "CHAT"

    id = Column(Integer, primary_key=True, index=True)    
    sender_id = Column(Integer, ForeignKey("USER.id"), index=True)
    content = Column(String)
    timestamp = Column(DateTime)

    chatroom_id = Column(Integer, ForeignKey(""))

    # USER 관계
    sender = relationship("USER", back_populates="sent_chats")

    # CHATROOM 관계
    chatroom = relationship("CHATROOM", back_populates=chats)


class Chatroom(Base):
    __tablename__ = "CHATROOM"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # 채팅방이름(부가적인)

    # CHAT 관계
    chats = relationship("CHAT",back_populates="chatroom")
