import re
from sqlalchemy import Column, Integer, String, DateTime
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
    #dp = db.Column(db.LargeBinary) 
    #rendered_dp = db.Column(db.Text)
    created_time = db.Column(DateTime(), nullable=False)


    def __init__(self, firstname, lastname,username,email,password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.created_time = datetime.datetime.now()
    

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

def insert( firstname, lastname,username,email,password):
        insert = Accounts(firstname=firstname, lastname=lastname, username=username, email=email,password=password)
        db.session.add(insert)
        db.session.commit()
        return True

def update(_id, firstname, lastname):
    update=Accounts.query.filter_by(id=_id).update(dict(firstname=firstname, lastname=lastname))
    db.session.commit()


def fetch(_id):
    user = Accounts.query.filter_by(id = _id).first()
    return (user)