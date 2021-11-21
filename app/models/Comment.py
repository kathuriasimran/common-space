from logging import info
from sqlalchemy import Column, Integer, String, DateTime
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
    
    user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    author = db.relationship(Accounts, backref=db.backref('comments', lazy=True))
   
    post_id = db.Column(db.Integer, db.ForeignKey('blogposts.id'), nullable=False)
    post = db.relationship(Blogposts, backref=db.backref('comments',
                                                    order_by='Comment.date_posted.desc()',
                                                    lazy=True,
                                                    # the following line enables deleting automatically
                                                    # the comments of a post when deleting the post
                                                    # uncomment to activate it
                                                    # cascade="all, delete-orphan"
                                                    ))

    def __init__(self, content, user_id, post_id):
        self.content = contents
        self.user_id = user_id
        self.post_id =post_id


def fetch_comment(user_id, post_id):
    comments = Comment.query.filter_by(user_id=user_id, post_id=post_id).all()
    return (comments)
