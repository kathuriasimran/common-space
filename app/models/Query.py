from sqlalchemy import Column, Integer, String, DateTime
from app import db
import datetime


class Query(db.Model):
    __tablename__ = 'query'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)
    username = db.Column(db.String(50) )
    comments = db.relationship('Comment',cascade="all, delete", backref='question', lazy=True)

    def __init__(self, title, body, username):
        self.title = title
        self.body = body
        self.date_posted = datetime.datetime.now()
        self.username = username

def insert(_title, _body, username):
        insert = Query(title = _title, body = _body, username = username)
        db.session.add(insert)
        db.session.commit()
        return True

def fetch_all():
    data = Query.query.order_by(Query.date_posted.desc()).all()
    return (data)

def fetch(_id):
    data = Query.query.filter_by(id=_id).first()
    return (data)

def fetch_question_count(username):
    count = Query.query.filter_by(username=username).count()
    return (count)

def fetch_question_all(username):
    count = Query.query.filter_by(username=username).all()
    return (count)

def deletequestion(id):
    obj = Query.query.filter_by(id =id).first()
    db.session.delete(obj)
    db.session.commit()
    return True
