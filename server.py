from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect)
from model import connect_to_db, db
import crud
import sympy as sp
from random import randint
# from mathjax import typeset
import os, students

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# route all the apps through here
@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/character_profile')
def character_profile():
    return render_template('character_profile.html')

@app.route('/student_profile')
def student_profile():
    return render_template('student_profile.html')

@app.route('/unit1')
def unit1():
    return render_template('unit1.html')

@app.route('/concept1_1')
def concept1_1():
    return render_template('concept1_1.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/test2')
def test2():
    return render_template('test2.html')



@app.route('/derivative')
def u1_c1_write():

    x = sp.Symbol('x')
    terms = []
    term_num = randint(1, 6) #select a random number of terms from 1-6
    for i in range(term_num): # generate randome coefficient/degree pairs as tuples
        coefficient = randint(-9, 9)
        degree = randint(0, 9)
        pair = (coefficient, degree)
        terms.append(pair)

    # initialize the function
    function_terms = [] # put the tuples into an expression
    for n in range(len(terms)):
        function_terms.append((terms[n][0])*x**(terms[n][1]))
    # put all the terms together in a single expression
    f = sum(function_terms)
    df_dx = sp.diff(f,x)

    f = str(f)
    df_dx = str(df_dx)

    f = f.replace('**', '^')
    df_dx = df_dx.replace('**', '^')

    return f, df_dx #, {'data': [str(f), str(df_dx)]}#f, df_dx# fetch request, Ajax lecture. 

@app.route('/problem1_1_1')
def problem1_1_1():
    f, df_dx = u1_c1_write()
    return render_template('problem1_1_1.html', f=f, df_dx=df_dx)#, func=func, deriv=deriv)


@app.route("/db") # when model is changed, reboot the database by going to this route in the browser
def db_1():
    students.seed()
    return "Done with db route"

@app.route("/student", methods=["POST"])
def register_user():

    # assigned name of the elemment in parentheses
    email = request.form.get("email") # get the email from html and save it to a variable
    password = request.form.get("password") # get password and save it to variable
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    print('************************************************************==============')
    print(email,password, lname, fname)
    user = crud.get_student_by_email(email)
    if user: # if the user exists
        flash("Cannot create an account with that email. Try again.")
    else: # go to the crud function to CREATE
        user = crud.create_student(fname, lname, email, password) # set return of function to user
        db.session.add(user) # add the created user to the database
        db.session.commit() # commit it to the database. 
        flash("Account created! Please log in.")

    return redirect("/dashboard") #once done, return to homepage. 

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    connect_to_db(app)
    
    app.run(debug=True, host="0.0.0.0")