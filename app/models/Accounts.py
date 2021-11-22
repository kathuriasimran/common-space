import re
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import query
from app import db
import datetime
import pymysql.cursors 


class Accounts(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    image_file = db.Column(db.String(200), nullable=False, default='dp.png')
    created_time = db.Column(DateTime(), nullable=False)



    #answer = db.relationship('Comment', backref='answer', lazy=True)

    def __init__(self, firstname, lastname,username,email,password,image_file):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.created_time = datetime.datetime.now()
        self.image_file =image_file
    

def account_authenticate(_username,_password):
    user = Accounts.query.filter_by(username = _username).filter_by(password = _password).first()
    if user is None:
        return False
    else:
        return (user)

def account_exist(_username,_email):
    user = Accounts.query.filter_by(username = _username).filter_by(email = _email).first()
    if user is None:
        return False
    else:
        return True

def insert(firstname, lastname, username, email, password, image_file="dp.png"):
        insert = Accounts(firstname=firstname, lastname=lastname, username=username, email=email,password=password,image_file=image_file)
        db.session.add(insert)
        db.session.commit()
        return True

def update(_id, firstname, lastname,image_file):
    update=Accounts.query.filter_by(id=_id).update(dict(firstname=firstname, lastname=lastname,image_file=image_file))
    db.session.commit()


def fetch(_id):
    user = Accounts.query.filter_by(id = _id).first()
    return (user)