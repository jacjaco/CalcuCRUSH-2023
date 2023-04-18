from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect)
from model import connect_to_db, db, Student, Problem, ProblemProgress
import crud
import sympy as sp
from random import randint
# from mathjax import typeset
import os, students

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.before_first_request
def create_database():
    db.create_all()



@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/terms')
def user_terms():
    return render_template('terms.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


    
@app.route('/character_profile')
def character_profile():
    return render_template('character_profile.html')

@app.route('/student_profile')
def student_profile():
    email = session.get('email')
    student = Student.query.filter_by(email=email).first()
    return render_template('student_profile.html', student=student)

@app.route('/unit1')
def unit1():
    return render_template('unit1.html')

@app.route('/concept1_1')
def concept1_1():
    return render_template('concept1_1.html')

@app.route('/update_career_goal', methods=['POST'])
def update_career_goal():
    data = request.get_json()
    new_career_goal = data['career_goal']
    
    student = Student.query.first()
    student.career_path = new_career_goal
    db.session.commit()

    return jsonify({ 'success': True })

@app.route('/update-points', methods=['POST'])
def update_points():
    email = request.form['email']
    points = int(request.form['points'])
    student = Student.query.filter_by(email=email).first()
    if student:
        student.planet_points = points
        db.session.commit()
        return jsonify(success=True)
    else:
        return jsonify(success=False)


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/test2')
def test2():
    return render_template('test2.html')

@app.route('/test3')
def test3():
    return render_template('test3.html')


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

    f = f.replace(" ", "")
    df_dx = df_dx.replace(" ", "")

    return f, df_dx #, {'data': [str(f), str(df_dx)]}#f, df_dx# fetch request, Ajax lecture. 

@app.route('/problem1_1_1')
def problem1_1_1():
    f, df_dx = u1_c1_write()
    email = session.get('email')
    student = Student.query.filter_by(email=email).first()
    return render_template('problem1_1_1.html', f=f, df_dx=df_dx, student=student) #, planet_points=students.planet_points)

@app.route('/problem111_check', methods=['POST'])
def problem111_check():
    user_input = request.json["answer"]

    problem, correct_answer = u1_c1_write()

    result = str(user_input) == str(correct_answer)
    if result:
        email = session.get('email')
        # student = Student.query.filter_by(email=email).first()
        # student.planet_points += 1
        # db.session.commit()

        return jsonify({"correct": True }), render_template('problem1_1_1.html', planet_points=student.planet_points) #, "user_input": user_input, "correct_answer": correct_answer, "result": "correct"})

    else:
        return jsonify({"correct": False }) #, "user_input": user_input, "correct_answer": correct_answer, "result": "incorrect"})



@app.route('/problem1_1_2')
def problem1_1_2():
    return render_template('problem1_1_2.html')#, func=func, deriv=deriv)


@app.route("/db") # when model is changed, reboot the database by going to this route in the browser
def db_1():
    students.seed()
    return "Done with db route"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['action'] == 'signin':
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            password = request.form['password']
            student = Student.query.filter_by(email=email).first()
            if student is not None: # If the student email already exists
                error = "An account has already been made with this email. Try logging in. "
                return render_template('homepage.html', error=error)
            else: # Create a new student
                new_student = Student(fname=fname, lname=lname, email=email, password=password)
                db.session.add(new_student)
                db.session.commit()
                session['email'] = email
                return redirect('/terms')

        elif request.form['action'] == 'login':
            email = request.form['email']
            password = request.form['password']
            student = Student.query.filter_by(email=email).first()
            if student is not None and student.password == password:
                session['email'] = email
                return redirect('/terms')
            else:
                error = 'Invalid username or password'
                return render_template('homepage.html', error=error)
    return render_template('homepage.html')

    
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    connect_to_db(app)
    
    app.run(debug=True, host="0.0.0.0")