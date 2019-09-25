from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:foo.db')
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    phone = Column(String)
    code = Column(String)


Base.metadata.create_all(engine)

