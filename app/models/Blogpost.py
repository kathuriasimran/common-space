from logging import info
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from app import db
import datetime

class Blogposts(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    image_file = db.Column(db.String(200), nullable=False, default='default.jpg')
    author = db.Column(db.String(50) )

    def __init__(self, title, subtitle, content , author,image_file):
        self.title = title
        self.subtitle = subtitle
        self.date_posted = datetime.datetime.now()
        self.content = content
        self.image_file =image_file
        self.author = author

def insert(_title, _subtitle,_content,_username,_image_file):
    insert = Blogposts (title=_title, subtitle=_subtitle, content=_content, author=_username,image_file=_image_file)
    db.session.add(insert)
    db.session.commit()
    return 1

def fetch_all():
    blog = Blogposts.query.order_by(Blogposts.date_posted.desc()).all()
    return (blog)

def fetch(_id):
    blog = Blogposts.query.filter_by(id=_id).first()
    return (blog)

def fetch_post(username):
    count = Blogposts.query.filter_by(author=username).count()
    return (count)

def fetch_post_all(username):
    blog = Blogposts.query.filter_by(author=username).all()
    return (blog)

def deletepost(id):
    obj = Blogposts.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    return True

def search(search):
    info = Blogposts.query.filter(Blogposts.content.like(search)).all()
    return (info)