from flask import render_template, request, redirect, url_for,session
from sqlalchemy.orm.query import Query
from app import app
import re
from app.models import Blogpost, Accounts, Query, Answer
from werkzeug.utils import redirect
import os


#Create a route decorator

#Login page (first page of website)
@app.route('/')
def login():
    return render_template("Login.html")


# For authenticating credentials
@app.route('/', methods=['POST'])
def authenticate():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        
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
    return render_template('Login.html', msg=msg)


# For logging out
@app.route('/profile/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('logged_in', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('user_image', None)
   # Redirect to login page
   return redirect(url_for('login'))


#For registeration
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
    

# To show sign Up page with message
@app.route('/SignUp/<string:msg>')
def signup_message(msg):
        return render_template("Register.html",msg=msg)



#Feed page(all posts will show) 
@app.route('/feeds')
def feed():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        blog=Blogpost.fetch_all()
        return render_template("Feeds.html",blog=blog)
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


#shows all the posts related to the keywords entered in search bar
@app.route('/feeds' , methods=['GET','POST'])
def search():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
            if request.method =='POST':
                form = request.form
                search_value=form['search']
                search = "%{}%".format(search_value)
                result = Blogpost.search(search)
                return render_template("Feeds.html",blog=result)
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


#For Adding new post on Feeds
@app.route('/feeds/Add_Post')
def addpost():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:   
        return render_template("Add-Post.html")
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


#Taking enteries in form for adding post on feed section
@app.route('/feed/Add_post', methods=['GET','POST'])
def add():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:   
        
        if 'file' in request.files:
            image = request.files['file']
            image_name = image.filename
            #if user uploaded image file 
            if image_name != "":
                    #creating path for image to save 
                    image_path = os.path.join(app.config['UPLOAD_FOLDER_BLOG'], image_name)
                    image.save(image_path)

            #if user not upload image file then default image will get saved
            else:
                image_name = "default.jpg"

        title = request.form['title']
        subtitle = request.form['subtitle']
        content = request.form['content']
        author=session['username']
        #Saving data in Blogpost database
        insert = Blogpost.insert(title, subtitle, content, author ,image_name)

        #if successfuly added to database then return to feed page
        if insert: 
            return redirect(url_for('feed'))
        else:
            msg = "Error Inserting record"
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


#To read any particular full article from feed page
@app.route('/feeds/Post/<int:id>/')
def post(id):
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        blog=Blogpost.fetch(id)
        return render_template("Post.html",blog=blog)

    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

#QnA page(all questions will appear)
@app.route('/qna')
def QnA():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        queries=Query.fetch_all()
        return render_template("QnA.html",queries=queries)
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


#shows all the posts related to the keywords entered in search bar
@app.route('/qna' , methods=['GET','POST'])
def search_question():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
            if request.method =='POST':
                form = request.form
                search_value=form['search']
                search = "%{}%".format(search_value)
                result = Query.search(search)
                return render_template("QnA.html",queries=result)

    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

#For Adding new question in QnA
@app.route('/qna/ask')
def ask():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        return render_template("Question-post.html")
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

#Taking enteries in form for adding question in QnA section
@app.route('/qna/ask' ,methods=['GET','POST'])
def Qna_add():
     #First check if the user in logged in or not
    if session.get('logged_in') == True:
        title = request.form['title']
        body = request.form['body']

        insert =  Query.insert(title, body, session['username'])
        if insert:
            return redirect(url_for('QnA'))
     #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

#For reading answers to that perticular question
@app.route('/answer_page/<int:query_id>')
def Answers(query_id):
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        query=Query.fetch(query_id)
        answers=Answer.fetch_answers(query_id)
        return render_template('Answer-page.html',query=query,answers=answers)
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

#For adding answer to that perticular question by user
@app.route('/add_answer/<int:query_id>/<string:msg>')
def Add_answer(query_id,msg):
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        query=Query.fetch(query_id)
        return render_template('Add-Answer.html',query=query,msg=msg)
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")
   
#Taking answer from user and adding to database
@app.route('/add_answer/<int:query_id>' ,methods=['GET','POST'])
def answer_page(query_id):
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        if 'answer' in request.form:
            answer = request.form['answer']
            insert=Answer.insert(answer,query_id,session['username'])
            if insert:
                return redirect(url_for('Answers', query_id = query_id))
            else:
                return redirect('Add_answer',msg="ERROR")
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


# To show profile page
@app.route('/profile')
def profile():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        #Fetching data from account database
        data=Accounts.fetch(session['id'])
        #Fetching post data from blogpost database 
        post_count=Blogpost.fetch_post(session['username'])
        #Fetching query data from query database
        question_count=Query.fetch_question_count(session['username'])
        return render_template('Profile.html', data1=data , post_count = post_count, question_count=question_count)

    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


# To see all the articles posted by user
@app.route('/profile/edit-post')
def edit_post():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        blog=Blogpost.fetch_post_all(session['username'])
        return render_template("Edit-Post.html", blog=blog)
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

# To delete any article posted by user
@app.route('/profile/edit-post/delete/<int:id>')
def delete_post(id):
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        delete=Blogpost.deletepost(id)
        if delete:
            return redirect(url_for('edit_post'))
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

# To see all the questions posted by user
@app.route('/profile/edit-question')
def edit_question():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        questions=Query.fetch_question_all(session['username'])
        return render_template("Edit-question.html", questions=questions)
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

# To delete any question asked by user
@app.route('/profile/edit-question/delete/<int:_id>')
def delete_question(_id):
    #First check if the user in logged in or not
    if session.get('logged_in') == True: 
        if(Query.deletequestion(_id)):
            return redirect(url_for('edit_question'))
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")

# To edit profile (display image, firstname, lastname)
@app.route('/profile/edit')
def edit():
    #First check if the user in logged in or not
    if session.get('logged_in') == True:
        return render_template('Edit.html', username=session['username'],user_image=session["user_image"])
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")


#Taking enteries in form for editing firstname, latsname and display image
@app.route('/profile/edit' , methods=['GET','POST'])
def edit_form():
     #First check if the user in logged in or not
    if session.get('logged_in') == True:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        print(firstname,lastname)
        print(request.files)
        if 'file' in request.files: 
            image = request.files['file']
            image_name = image.filename
            if image_name != "":
                #creating path for image to save 
                image_path = os.path.join(app.config['UPLOAD_FOLDER_PROFILE'], image_name)
                image.save(image_path)
                session['user_image']=image_name
                #If image is a uploaded then called update function of account database
                Accounts.update(session['id'], firstname, lastname,image_name)
                #If image is not a uploaded then called update_fl function of account database
            else:
                Accounts.update_fl(session['id'], firstname, lastname)
      
        return redirect(url_for('profile'))
    #If not logged in redirect to login page
    else:
        return render_template('Login.html', msg="Login First")