#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    gender = Column(String(250))

class report(Base):
    __tablename__ = 'report'

    id = Column(Integer, primary_key=True)
    url = Column(String(100))
    render_time = Column(String(50))
    key_word1 = Column(String(50))
    key_word2 = Column(String(50))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'url': self.url,
            'render_time': self.render_time,
            'key_word1': self.key_word1,
            'key_word2': self.key_word2,
        }

class report_meta(Base):
    __tablename__ = 'report_meta'

    meta_id = Column(Integer, primary_key=True)
    meta_name = Column(String(255))
    meta_key = Column(String(255))
    key_value = Column(String(255))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'meta_id': self.meta_id,
            'meta_name': self.meta_name,
            'meta_key': self.meta_key,
            'key_value': self.key_value
        }

class Vote(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    likes = Column(Integer)
    dislike = Column(Integer)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'likes': self.likes,
            'dislike': self.dislike,
            'id': self.id,
        }


engine = create_engine('sqlite:///skanner.db')
Base.metadata.create_all(engine)
