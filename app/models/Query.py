from sqlalchemy import Column, Integer, String, DateTime
from app import db
import datetime


class Query(db.Model):
    __tablename__ = 'query'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
   # ask_by = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    


    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.date_posted = datetime.datetime.now()

 
def insert(_title,_body):
        insert = Query(title = _title, body = _body)
        db.session.add(insert)
        db.session.commit()
        return True

def fetch_all():
    blog = Query.query.order_by(Query.date_posted.desc()).all()
    return (blog)