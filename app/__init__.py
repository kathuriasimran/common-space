from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,url_for,render_template,request,abort,session
from sqlalchemy.ext.declarative import declarative_base

import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.secret_key = 'S3$&F@$%DSRER'
app.config['SESSION_TYPE'] = 'filesystem'

app.config['SESSION_PERMANENT']=False

folder_path = os.getcwd()

app.config['UPLOAD_FOLDER_BLOG'] =  os.path.join(folder_path, r"/static/image/blog/")
print(app.config['UPLOAD_FOLDER_BLOG'])
app.config['UPLOAD_FOLDER_PROFILE'] = os.path.join(folder_path, r"/static/image/profile/")
print(app.config['UPLOAD_FOLDER_PROFILE'])

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:simran@localhost/common_space"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import api
