from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,url_for,render_template,request,abort,session
from sqlalchemy.ext.declarative import declarative_base
import json
import urllib.parse
import os
from flask_cors import CORS, cross_origin

#Creating flask app
app = Flask(__name__)
cors = CORS(app)

#Reading config.json file
my_dir = os.path.dirname(__file__)
json_file_path = os.path.join(my_dir, '../config.json')
with open(json_file_path, 'r') as f:
    config = json.load(f)
    app.config.update(config)

#Secret key from config.json
app.config['SECRET_KEY'] = app.config["startup_conf"]["secret_key"]
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT']=False


#Path for image uploading
folder_path = os.path.abspath(os.getcwd())
app.config['UPLOAD_FOLDER_BLOG'] =  os.path.join(folder_path,"app","static","image","blog")
print(app.config['UPLOAD_FOLDER_BLOG'])
app.config['UPLOAD_FOLDER_PROFILE'] =os.path.join(folder_path,"app","static","image","profile")
print(app.config['UPLOAD_FOLDER_PROFILE'])

#Connecting to database
if app.config["database_conf"]["type"] == "mysql":
    db_str ="mysql+pymysql://" + app.config["database_conf"]["username"]+":"+app.config["database_conf"]["password"]+"@"+app.config["database_conf"]["url"]+":"+app.config["database_conf"]["port"]+"/"+app.config["database_conf"]["database_name"]
    app.config["SQLALCHEMY_DATABASE_URI"] = db_str

elif app.config["database_conf"]["type"] == "azure_sql":
    db_str = "Driver={ODBC Driver 13 for SQL Server};Server=tcp:"+ app.config["database_conf"]["url"] +","+ app.config["database_conf"]["port"]+";Database="+app.config["database_conf"]["database_name"]+";Uid="+app.config["database_conf"]["username"]+";Pwd="+app.config["database_conf"]["password"]+";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
    params = urllib.parse.quote_plus(db_str)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


from app import api

