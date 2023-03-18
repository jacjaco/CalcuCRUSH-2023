from model import db, Student, Unit, Concept, Problem, UnitProgress, ConceptProgress, ProblemProgress, Goal, UnitEquation, ConceptEquation, ProblemEquation, connect_to_db



def create_student(fname, lname, email, password):
    """Create and return a new student."""

    student = Student(fname=fname, lname=lname, email=email, password=password)

    db.session.add(student)
    db.session.commit()

    return student

def get_student_by_email(email):
     return Student.query.filter(Student.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    app.run(debug=True, port=5000)