from app.models.Blogpost import *
from app.models.Accounts import *
from app import db
import datetime

# Creating Answer Database
class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    post_id = db.Column(db.Integer, db.ForeignKey('query.id'), nullable=False) 
    username = db.Column(db.String(50))
    

    def __init__(self, content, post_id, username):
        self.content = content
        self.post_id =post_id
        self.username=username

# Inserting answer in database
def insert(answer,query_id, username):
    insert = Answer(content=answer, post_id=query_id, username=username)
    db.session.add(insert)
    db.session.commit()
    return True

# Retrieving answers from database
def fetch_answers(query_id):
    answers = Answer.query.filter_by(post_id = query_id).all()
    return (answers)


