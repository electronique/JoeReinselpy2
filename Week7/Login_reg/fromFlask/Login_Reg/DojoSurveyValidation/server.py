from flask import Flask, render_template, request, redirect,flash,session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = "SecretKey"
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=['POST'])
def create_user():
  session['name']= request.form['name']
  session['location']=request.form['location']
  session['favlang']=request.form['favlang']
  session['comments']=request.form['comments']

  if len(session['name']) < 1:
      flash("Name cannot be empty!") 
  elif len(session['name']) > 1:
      flash("Success! Your name is {}".format(request.form['name']))
  if len(session['comments']) > 150:
      flash("Must be under 150 characters.")
  elif len(session['comments']) < 150:
      flash("Success! Your comments are {}".format(session['comments']))       
      #location = request.form['location']
      #favlang = request.form['favlang']
      #comments = request.form['comments']
   #print name
   #print location
  return render_template("index.html")#location=location, favlang=favlang, comments=comments
app.run(debug=True) # run our server
