from app import db
import datetime

#Creating query database
class Query(db.Model):
    __tablename__ = 'query'
    
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)
    username = db.Column(db.String(50) )
    answers = db.relationship('Answer',cascade="all, delete", backref='question', lazy=True)
    # when question is deleted the answers to that question will also get deleted

    def __init__(self, title, body, username):
        self.title = title
        self.body = body
        self.date_posted = datetime.datetime.now()
        self.username = username

# Adding question to database
def insert(_title, _body, username):
        insert = Query(title = _title, body = _body, username = username)
        db.session.add(insert)
        db.session.commit()
        return True

# Retrieving all questions 
def fetch_all():
    data = Query.query.order_by(Query.date_posted.desc()).all()
    return (data)

# Retrieving question for perticular ID
def fetch(_id):
    data = Query.query.filter_by(id=_id).first()
    return (data)

# Counting no. of question for perticular username
def fetch_question_count(username):
    count = Query.query.filter_by(username=username).count()
    return (count)

# Retrieving all questions for perticular username
def fetch_question_all(username):
    count = Query.query.filter_by(username=username).all()
    return (count)

# Deleting question from database
def deletequestion(id):
    obj = Query.query.filter_by(id =id).first()
    db.session.delete(obj)
    db.session.commit()
    return True

# To search question for given keywords
def search(search):
    info = Query.query.filter((Query.body.like(search)) | (Query.title.like(search)) ).all()
    return (info)