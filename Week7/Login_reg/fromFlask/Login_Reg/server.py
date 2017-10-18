from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt

from mysqlconnection import MySQLConnector
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'mydb')
app.secret_key = "SecretKey"
@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/reg', methods=['POST'])

def create():
    session['username']= request.form['']
    session['email']=request.form['email']
    session['password']=request.form['password']
    password = request.form['password']
    if len(session['username']) < 1 or len(session['email']) < 1 or len(session['password']) < 1:
        flash("Please fill out this form to register!") 
    else:
        pw_hash = bcrypt.generate_password_hash(password)
        print pw_hash
        flash("Thank you for registering!")
        query = "INSERT INTO user (username,password,email, created_at) VALUES (:username,:pw_hash,:email,NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'username': request.form['username'], 
                'pw_hash': pw_hash, 
                'email': request.form['email']
                    }
        mysql.query_db(query, data)
     
    return redirect('/')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM user WHERE username = :username LIMIT 1"
    data = {'username': username}
    mysql.query_db(query, data)
    return render_template("success.html")
app.run(debug=True)