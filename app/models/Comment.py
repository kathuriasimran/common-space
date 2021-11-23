from logging import info
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm.query import Query
from sqlalchemy.sql.schema import ForeignKey
from app.models.Blogpost import *
from app.models.Accounts import *
from app import db
import datetime


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    post_id = db.Column(db.Integer, db.ForeignKey('query.id',ondelete='SET NULL'), nullable=False)
    username = db.Column(db.String(50))
    

    def __init__(self, content, post_id, username):
        self.content = content
        self.post_id =post_id
        self.username=username


def insert(answer,query_id, username):
    insert = Comment(content=answer, post_id=query_id, username=username)
    db.session.add(insert)
    db.session.commit()
    return True


def fetch_answers(query_id):
    answers = Comment.query.filter_by(post_id = query_id).all()
    return (answers)


