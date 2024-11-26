import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    user_name = Column(String(30), nullable=False)
    user_info = Column(String(250), nullable=False)
    profile_pic_url = Column(String(250), nullable=True)

class Content(Base):
    __tablename__ = 'content'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    content_id = Column(Integer, primary_key=True)
    content_type = Column(String(20), nullable=False)
    content_description = Column(String(250))
    publish_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Content_media(Base):
    __tablename__='conten_media'
    media_id = Column(Integer, primary_key=True)
    media_file_url = Column(String(250))
    content_id = Column(Integer, ForeignKey(Content.content_id))
    content = relationship(Content)
    
class Content_comments(Base):
    __tablename__='content_comments'
    comment_id= Column(Integer, primary_key=True)
    comment_text= Column(String(250))
    user_who_commented = Column(Integer, ForeignKey(User.id))
    content_id = Column(Integer,ForeignKey(Content.content_id))
    comment = relationship(Content)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
