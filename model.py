
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    career_path = db.Column(db.String(100))
    mathematical_level = db.Column(db.Float)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    planet_points = db.Column(db.Integer)

    unit_progress = db.relationship('UnitProgress', back_populates='student') 
    concept_progress = db.relationship('ConceptProgress', back_populates='student')
    problem_progress = db.relationship('ProblemProgress', back_populates='student')


    def __repr__(self):
        return f"<Student student_id={self.id} email={self.email}>"

class Unit(db.Model):

    __tablename__ = "units"

    id = db.Column(db.Float, primary_key=True)
    concepts_covered = db.Column(db.String(500))
    level_req = db.Column(db.Float)

    unit_progress = db.relationship('UnitProgress', back_populates='unit')
    concept = db.relationship('Concept', back_populates='unit')
    unit_equation = db.relationship('UnitEquation', back_populates='unit')

    def __repr__(self):
        return f"<Unit unit_id={self.id}>"

class Concept(db.Model):

    __tablename__ = "concepts"
    # attributes
    id = db.Column(db.Float, primary_key=True)
    problems_covered = db.Column(db.String(500))
    # foreign keys out
    unit_id = db.Column(db.Float, db.ForeignKey('units.id'))
    goal_id = db.Column(db.Float, db.ForeignKey('goals.id'))
    # foreign key out relationships
    unit = db.relationship('Unit', back_populates='concept')
    goal = db.relationship('Goal', back_populates='concept')
    # foreign key in relationships
    concept_progress = db.relationship('ConceptProgress', back_populates='concept')
    problem = db.relationship('Problem', back_populates='concept')
    concept_equation = db.relationship('ConceptEquation', back_populates='concept')

    def __repr__(self):
        return f"<Concept concept_id={self.id}>"

class Problem(db.Model):

    __tablename__ = "problems"

    id = db.Column(db.Float, primary_key=True)
    point_worth = db.Column(db.Integer)
    # foreign keys out
    concept_id = db.Column(db.Float, db.ForeignKey('concepts.id'))
    # foreign keys out relationship
    concept = db.relationship('Concept', back_populates='problem')
    # foreign keys in relationship
    problem_progress = db.relationship('ProblemProgress', back_populates='problem')
    math_expression = db.relationship('MathExpression', back_populates='problem')
    problem_equation = db.relationship('ProblemEquation', back_populates='problem')
    user_input = db.relationship('UserInput', back_populates='problem')


    def __repr__(self):
        return f"<Problem problem_id={self.id}>"


class UnitProgress(db.Model):

    __tablename__ = "units_complete"

    id = db.Column(db.Float, primary_key=True)
    units_done = db.Column(db.String(100))
    completion = db.Column(db.Boolean)
    # foreign keys out
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    unit_id = db.Column(db.Float, db.ForeignKey('units.id'))
    # foreign keys out relationships
    student = db.relationship('Student', back_populates='unit_progress')
    unit = db.relationship('Unit', back_populates='unit_progress')

    def __repr__(self):
        return f"<UnitProgress id={self.id}>"


class ConceptProgress(db.Model):

    __tablename__ = "concepts_complete"

    id = db.Column(db.Float, primary_key=True)
    concepts_done = db.Column(db.String(100))
    completion = db.Column(db.Boolean)
    # foreign keys out
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    concept_id = db.Column(db.Float, db.ForeignKey('concepts.id'))
    # foreign keys out relationships
    student = db.relationship('Student', back_populates='concept_progress')
    concept = db.relationship('Concept', back_populates='concept_progress')


    def __repr__(self):
        return f"<ConceptProgress id={self.id}>"

class ProblemProgress(db.Model):

    __tablename__ = "problems_complete"
    
    id = db.Column(db.Float, primary_key=True)
    problems_done = db.Column(db.String(100))
    completion = db.Column(db.Boolean)
    points_gained = db.Column(db.Integer)
    # foreign keys out
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    # foreign keys out relationships
    student = db.relationship('Student', back_populates='problem_progress')
    problem = db.relationship('Problem', back_populates='problem_progress')


    def __repr__(self):
        return f"<ProblemProgress id={self.id}>"

class Goal(db.Model):

    __tablename__ = "goals"

    id = db.Column(db.Float, primary_key=True)
    applications = db.Column(db.String(100))
    # foreign key relationships in
    concept = db.relationship('Concept', back_populates='goal')

    def __repr__(self):
        return f"<Goal id={self.id}>"


class UnitEquation(db.Model):

    __tablename__ = "unit_equations"

    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    unit_id = db.Column(db.Float, db.ForeignKey('units.id'))
    equation_id = db.Column(db.Float, db.ForeignKey('equations.id'))
    # foreign keys out relationships
    unit = db.relationship('Unit', back_populates='unit_equation')
    equation = db.relationship('Equation', back_populates='unit_equation')
   

    def __repr__(self):
        return f"<UnitEquation id={self.id}>"

class ConceptEquation(db.Model):

    __tablename__ = "concept_equations"
    
    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    concept_id = db.Column(db.Float, db.ForeignKey('concepts.id'))
    equation_id = db.Column(db.Float, db.ForeignKey('equations.id'))
    # foreign keys out relationships
    concept = db.relationship('Concept', back_populates='concept_equation')
    equation = db.relationship('Equation', back_populates='concept_equation')
   
    def __repr__(self):
        return f"<ConceptEquation id={self.id}>"

class ProblemEquation(db.Model):

    __tablename__ = "problem_equations"

    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    equation_id = db.Column(db.Float, db.ForeignKey('equations.id'))
    # foreign keys out relationships
    problem = db.relationship('Problem', back_populates='problem_equation')
    equation = db.relationship('Equation', back_populates='problem_equation')
   

    def __repr__(self):
        return f"<ProblemEquation id={self.id}>"

class UserInput(db.Model):

    __tablename__ = "user_inputs"

    user_input_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    problem_id = db.Column(db.Integer)
    all_inputs = db.Column(db.String)

    def __repr__(self):
        return f"<UserInput user_input_id={self.user_input_id}>"
    id = db.Column(db.Float, primary_key=True)
    all_inputs = db.Column(db.String)
    # foreign keys out
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    # foreign keys out relationships
    problem = db.relationship('Problem', back_populates='user_input')

    def __repr__(self):
        return f"<UserInput id={self.id}>"

class Equation(db.Model):

    __tablename__ = "equations"

    id = db.Column(db.Float, primary_key=True)
    equation = db.Column(db.String(100))
    # foreign keys in relationships
    unit_equation = db.relationship('UnitEquation', back_populates='equation')
    concept_equation = db.relationship('ConceptEquation', back_populates='equation')
    problem_equation = db.relationship('ProblemEquation', back_populates='equation')


    def __repr__(self):
        return f"<Equation id={self.id}>"

class MathExpression(db.Model):

    __tablename__ = "math_expressions"

    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    # foreign keys out relationships
    problem = db.relationship('Problem', back_populates='math_expression')

    def __repr__(self):
        return f"<MathExpression id={self.id}>"


def connect_to_db(flask_app, db_uri="postgresql:///students", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    # db.create_all()
    print("Connected to the db!")

if __name__ == "__main__":
    # from flask import Flask

    # app = Flask(__name__)
    from server import app
    connect_to_db(app)
