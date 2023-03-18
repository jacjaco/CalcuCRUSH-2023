from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
import sympy as sp

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# route all the apps through here
@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/derivative_calc', methods=['GET', 'POST'])
def derivative_calc():
    function = request.form.get('function')

    # Evaluate the function and determine if the user's answer is correct. 
    x = sp.Symbol('x')
    f = function
    df_dx = sp.diff(f, x)

    return df_dx


@app.route("/student", methods=["POST"])
def register_user():
    email = request.form.get("email") # get the email from html and save it to a variable
    password = request.form.get("password") # get password and save it to variable
    fname = request.form.get("fname")
    lname = request.form.get("lname")

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
    app.run(debug=True, host="0.0.0.0")