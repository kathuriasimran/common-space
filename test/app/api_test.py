from enum import Flag
from os import access, name
from flask.wrappers import Request
from sqlalchemy.orm import query
   

from sqlalchemy.orm.query import Query
#from sqlalchemy.util.compat import dataclass_fields
from app import app
import re

from logging.handlers import RotatingFileHandler
from app.models import Blogpost, Accounts, Query, Answer
from sqlalchemy.orm import load_only
from flask import render_template, request, redirect, url_for,session
from app import  db
from werkzeug.utils import redirect
import os
import pytest



#create a route decorator
@app.route('/')
def test_login():
    assert True
    return render_template("Login.html")



@app.route('/Login/authenticate', methods=['POST'])
def test_authenticate():
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
           
            session['logged_in'] = True
            session['id'] = account.id
            session['username']=account.username
            session['user_image']=account.image_file

            # Redirect to home page
            return redirect(url_for('feed'))
        else:
            # Account doesnt exist or username/password incorrect
            msg='Wrong Username or Password'
    # Show the login form with message (if any)
    assert msg
    return render_template('Login.html', msg=msg)


@app.route('/profile/logout')
def test_logout():
    # Remove session data, this will log the user out
   session.pop('logged_in', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('user_image', None)
   # Redirect to login page
   assert session
   return redirect(url_for('login'))


@app.route('/feeds')
def test_feed():
    if session.get('logged_in') == True:
        blog=Blogpost.fetch_all()
        assert blog
        return render_template("Feeds.html",blog=blog)
    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/feeds/search' , methods=['GET','POST'])
def test_search():
    if session.get('logged_in') == True:
            if request.method =='POST':
                form = request.form
                search_value=form['search']
                search = "%{}%".format(search_value)
                result = Blogpost.search(search)
                assert result
                return render_template("Feeds.html",blog=result)
    else:
        assert True
        return render_template('Login.html', msg="Login First")





@app.route('/feeds/Add_Post')
def test_addpost():
    if session.get('logged_in') == True:
        assert session
        return render_template("Add-Post.html")
    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/feed/Add_post/Add', methods=['GET','POST'])
def test_add():
    if session.get('logged_in') == True:   
        
        if 'file' in request.files:
            image = request.files['file']
            image_name = image.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER_BLOG'], image_name)
            image.save(image_path)
        else:
            image_name = "default.jpg"

        title = request.form['title']
        subtitle = request.form['subtitle']
        content = request.form['content']
        author=session['username']
        insert = Blogpost.insert(title, subtitle, content, author ,image_name)

        if insert:
            assert True
            return redirect(url_for('feed'))
        else:
            assert msg
            msg = "Error Inserting record"
    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/feeds/Post/<int:id>/')
def test_post(id):
    if session.get('logged_in') == True:
        blog=Blogpost.fetch(id)
        assert blog
        return render_template("Post.html",blog=blog)

    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/feeds/Blog', methods=['GET','POST'])
def test_show_post():
    if session.get('logged_in') == True:
        assert True 
        return render_template('Post.html')
    else:
        assert True 
        return render_template('Login.html', msg="Login First")


@app.route('/SignUp', methods=['GET','POST'])
def test_signup():
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
        assert msg
        return redirect(url_for('signup_message', msg=msg))

    elif request.method == 'GET':
        assert True
        return render_template("Register.html")
    


@app.route('/SignUp/<string:msg>')
def test_signup_message(msg):
    if session.get('logged_in') == True:
        assert msg
        return render_template("Register.html",msg=msg)
    else:
        assert True
        return render_template('Login.html', msg="Login First")



@app.route('/profile')
def profile():
    if session.get('logged_in') == True:
        data=Accounts.fetch(session['id'])
        post_count=Blogpost.fetch_post(session['username'])
        question_count=Query.fetch_question_count(session['username'])
        if session.get('logged_in') == True:
            assert data
            return render_template('Profile.html', data1=data , post_count = post_count, question_count=question_count)
        assert True
        return redirect(url_for('login'))
    else:
        assert True
        return render_template('Login.html', msg="Login First")



@app.route('/profile/edit-post')
def test_edit_post():
    if session.get('logged_in') == True:
        blog=Blogpost.fetch_post_all(session['username'])
        assert blog
        return render_template("Edit-Post.html", blog=blog)
    else:
        assert True
        return render_template('Login.html', msg="Login First")

@app.route('/profile/edit-post/delete/<int:id>')
def test_delete_post(id):
    if session.get('logged_in') == True:
        delete=Blogpost.deletepost(id)
        if delete:
            assert True
            return redirect(url_for('edit_post'))
    else:
        assert True
        return render_template('Login.html', msg="Login First")

@app.route('/profile/edit-question')
def test_edit_question():
    if session.get('logged_in') == True:
        questions=Query.fetch_question_all(session['username'])
        assert question
        return render_template("Edit-question.html", questions=questions)
    else:
        assert msg
        return render_template('Login.html', msg="Login First")

@app.route('/profile/edit-question/delete/<int:_id>')
def test_delete_question(_id):
    if session.get('logged_in') == True: 
        if(Query.deletequestion(_id)):
            assert True
            return redirect(url_for('edit_question'))
    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/profile/edit')
def test_edit():
    if session.get('logged_in') == True:
        assert username
        return render_template('Edit.html', username=session['username'],user_image=session["user_image"])
    else:
        assert True
        return render_template('Login.html', msg="Login First")



@app.route('/profile/edit/edit_form' , methods=['GET','POST'])
def test_edit_form():
    if session.get('logged_in') == True:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        print(firstname,lastname)
        print(request.files)
        if 'file' in request.files:
            image = request.files['file']
            image_name = image.filename
            print(image_name)
            image_path = os.path.join(app.config['UPLOAD_FOLDER_PROFILE'], image_name)
            print(image_path)
            image.save(image_path)
        else:
            image_name = "dp.png"
        Accounts.update(session['id'], firstname, lastname,image_name)
        assert True
        return redirect(url_for('profile'))
    else:
        assert True
        return render_template('Login.html', msg="Login First")



@app.route('/QnA')
def test_QnA():
    if session.get('logged_in') == True:
        queries=Query.fetch_all()
        assert queries
        return render_template("QnA.html",queries=queries)
    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/QnA/search' , methods=['GET','POST'])
def test_search_question():
    if session.get('logged_in') == True:
            if request.method =='POST':
                form = request.form
                search_value=form['search']
                search = "%{}%".format(search_value)
                result = Query.search(search)
                assert result
                return render_template("QnA.html",queries=result)
    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/QnA/ask')
def test_ask():
    if session.get('logged_in') == True:
        assert True
        return render_template("Question-post.html")
    else:
        assert True
        return render_template('Login.html', msg="Login First")


@app.route('/QnA/Add_Question' ,methods=['GET','POST'])
def test_Qna_add():
    if session.get('logged_in') == True:
        title = request.form['title']
        body = request.form['body']

        insert =  Query.insert(title, body, session['username'])
        if insert:
            msg = 'You have successfully registered!'
            assert True
            return redirect(url_for('QnA'))
        else:
            msg = "Error Inserting record"
    else:
        assert True
        return render_template('Login.html', msg="Login First")

@app.route('/answer_page/<int:query_id>')
def test_Answers(query_id):
    if session.get('logged_in') == True:
        query=Query.fetch(query_id)
        answers=Answer.fetch_answers(query_id)
        assert answers
        return render_template('Answer-page.html',query=query,answers=answers)
    else:
        assert true
        return render_template('Login.html', msg="Login First")


@app.route('/add_answer/<int:query_id>/<string:msg>')
def test_Add_answer(query_id,msg):
   
        query=Query.fetch(query_id)
        assert msg
        return render_template('Add-Answer.html',query=query,msg=msg)
   


@app.route('/add_answer/<int:query_id>' ,methods=['GET','POST'])
def test_answer_page(query_id):
    if session.get('logged_in') == True:
        if 'answer' in request.form:
            answer = request.form['answer']
            insert=Answer.insert(answer,query_id,session['username'])
            if insert:
                assert query_id
                return redirect(url_for('Answers', query_id = query_id))
            else:
                assert True
                return redirect('Add_answer',msg="ERROR")
    

    else:
        assert True
        return render_template('Login.html', msg="Login First")

