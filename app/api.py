from os import access, name
import pymysql.cursors   

from sqlalchemy.orm.query import Query
#from sqlalchemy.util.compat import dataclass_fields
from app import app
import re
import logging
from logging.handlers import RotatingFileHandler
from app.models import Blogpost, Accounts, Query, Comment
from sqlalchemy.orm import load_only
from flask import render_template, request, redirect, url_for, abort, jsonify,session
from app import  db
from werkzeug.utils import redirect
import os
from base64 import b64encode
import base64
from io import BytesIO #Converts data from Database into bytes


#create a route decorator
@app.route('/')
def login():
    return render_template("Login.html")

@app.route('/Login/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        # account = db.session.query(db.Accounts).filter(db.Accounts.username == username,db.Accounts.password== password).one()
        # If account exists in accounts table in out database
        account = Accounts.account_authenticate(username,password)
        if account:
            # Create session data, we can access this data in other routes
           
            session['loggedin'] = True
            session['id'] = account.id
            session['username']=account.username
            # Redirect to home page
            return redirect(url_for('feed'))
        else:
            # Account doesnt exist or username/password incorrect
            msg='Wrong Username or Password'
    # Show the login form with message (if any)
    return render_template('Login.html', msg=msg)


@app.route('/profile/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))


@app.route('/feeds')
def feed():
    blog=Blogpost.fetch_all()
    return render_template("Feeds.html",blog=blog)


@app.route('/feeds/search' , methods=['GET','POST'])
def search():
    if request.method =='POST':
        form = request.form
        search_value=form['search']
        search = "%{}%".format(search_value)
        result = Blogpost.search(search)
        return render_template("/feeds/Feeds.html",blog=result)


@app.route('/feeds/Add_Post')
def addpost():
    return render_template("Add-Post.html")


@app.route('/feed/Add_post/Add', methods=['GET','POST'])
def add():
    
    title = request.form['title']
    subtitle = request.form['subtitle']
    content = request.form['content']
    author=session['username']

    insert = Blogpost.insert(title, subtitle, content, author )
    if insert: 
        return redirect(url_for('feed'))
    else:
        msg = "Error Inserting record"


@app.route('/feeds/Post/<int:id>/')
def post(id):

    blog=Blogpost.fetch(id)
    return render_template("Post.html",blog=blog)


@app.route('/feeds/Blog', methods=['GET','POST'])
def Show_post():
    return render_template('Post.html')


@app.route('/SignUp', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        if 'firstname' in request.form and 'lastname' in request.form and 'username' in request.form and 'email' in request.form and 'password' in request.form :
            app.logger.info("User Registeration started")
            # Create variables for easy access
            firstname = request.form ['firstname']
            lastname = request.form ['lastname']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            app.logger.info("Recieved user input as FirstName: "+firstname + " LastName: "+lastname+" username:"+username+" email:"+email+" password:"+"xxxxxxx")
            
            account = Accounts.account_exist(username,email)
            # If account exists show error and validation checks
            if account:
                msg = 'Account already exists!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers!'
            elif not username or not password or not email or not firstname or not lastname:
                msg = 'Please fill out the form!'
            else:
                # Account doesnt exists and the form data is valid, now insert new account into accounts table
                insert = Accounts.insert(firstname, lastname,username,email,password)
                if insert:
                    msg = str("You have successfully registered!") 
                else:
                    msg = str("Error Inserting record")
        else:
            msg = 'Please fill out the form!'

        app.logger.info("Register Returned message as "+msg)
        return redirect(url_for('signup_message', msg=msg))

    elif request.method == 'GET':
        return render_template("Register.html")


@app.route('/SignUp/<string:msg>')
def signup_message(msg):
    return render_template("Register.html",msg=msg)

@app.route('/QnA')
def QnA():
    queries=Query.fetch_all()
    return render_template("QnA.html",queries=queries)

@app.route('/QnA/ask')
def ask():
    return render_template("Question-post.html")

@app.route('/QnA/Add_Question' ,methods=['GET','POST'])
def Qna_add():
    title = request.form['title']
    body = request.form['body']

    insert =  Query.insert(title, body)
    if insert:
        msg = 'You have successfully registered!' 
        return redirect(url_for('QnA'))
    else:
        msg = "Error Inserting record"




@app.route('/profile')
def profile():

    data=Accounts.fetch(session['id'])
    post_count=Blogpost.fetch_post(session['username'])
    if 'loggedin' in session:
        return render_template('Profile.html', data1=data , post_count = post_count)

    return redirect(url_for('login'))


@app.route('/profile/edit')
def edit():
    return render_template('Edit.html', username=session['username'])


@app.route('/profile/edit/edit_form' , methods=['GET','POST'])
def edit_form():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    Accounts.update(session['id'], firstname, lastname)
        
    return redirect(url_for('profile'))


@app.route('/answer_page')
def Answers():
    return render_template('Answer-page.html')
