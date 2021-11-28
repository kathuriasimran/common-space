from sqlalchemy import DateTime
from app import db
import datetime
 

# Creating Account Database
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

    
    def __init__(self, firstname, lastname, username, email, password, image_file):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.created_time = datetime.datetime.now()
        self.image_file =image_file
    
# For login In (checking credentials)
def account_authenticate(_username,_password):
    user = Accounts.query.filter_by(username = _username).filter_by(password = _password).first()
    if user is None:
        return False
    else:
        return (user)

# Checking account already exist or not
def account_exist(_username,_email):
    user = Accounts.query.filter_by(username = _username).filter_by(email = _email).first()
    if user is None:
        return False
    else:
        return True

# Creating new account
def insert(firstname, lastname, username, email, password, image_file="dp.png"):
        insert = Accounts(firstname=firstname, lastname=lastname, username=username, email=email,password=password,image_file=image_file)
        db.session.add(insert)
        db.session.commit()
        return True

# Editing firstname, lastname and display picture 
def update(_id, firstname, lastname,image_file):
    update=Accounts.query.filter_by(id=_id).update(dict(firstname=firstname, lastname=lastname,image_file=image_file))
    db.session.commit()

# Editing only firstname and lastname , if image is no uploaded
def update_fl(_id, firstname, lastname):
    update=Accounts.query.filter_by(id=_id).update(dict(firstname=firstname, lastname=lastname))
    db.session.commit()

# For retrieving data from account database 
def fetch(_id):
    user = Accounts.query.filter_by(id = _id).first()
    return (user)