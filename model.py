
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):

    __tablename__ = "students"

<<<<<<< HEAD
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    career_path = db.Column(db.String(50))
    mathematical_level = db.Column(db.Float)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    # unit_progress = db.relationship('UnitProgress', back_populates='unit')

    # unit_progress = db.relationship('Unit', back_populates='student')
    concept_progress = db.relationship('Concept', back_populates='student')
    problem_progress = db.relationship('Student', back_populates='student')


    def __repr__(self):
        return f"<Student student_id={self.student_id} email={self.email}>"
=======
    id = db.Column(db.Float, primary_key=True)
    career_path = db.Column(db.String(100))
    mathematical_level = db.Column(db.Float)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))

    unit_progress = db.relationship('UnitProgress', back_populates='student') 
    concept_progress = db.relationship('ConceptProgress', back_populates='student')
    problem_progress = db.relationship('ProblemProgress', back_populates='student')


    def __repr__(self):
        return f"<Student student_id={self.id} email={self.email}>"
>>>>>>> 843c4f9 (Add files remotely)

class Unit(db.Model):

    __tablename__ = "units"

<<<<<<< HEAD
    unit_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    level_req = db.Column(db.Float)

    # unit_progress = db.relationship('UnitProgress', back_populates='unit')
    concepts = db.relationship('Concept', back_populates='unit')

    def __repr__(self):
        return f"<Unit unit_id={self.unit_id}>"
=======
    id = db.Column(db.Float, primary_key=True)
    concepts_covered = db.Column(db.String(500))
    level_req = db.Column(db.Float)

    unit_progress = db.relationship('UnitProgress', back_populates='unit')
    concept = db.relationship('Concept', back_populates='unit')
    unit_equation = db.relationship('UnitEquation', back_populates='unit')

    def __repr__(self):
        return f"<Unit unit_id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class Concept(db.Model):

    __tablename__ = "concepts"
<<<<<<< HEAD

    concept_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.unit_id'))
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.goal_id'))

    concept_progress = db.relationship('ConceptProgress', back_populates='concept')
    goal = db.relationship('Goal', back_populates='concept')
    unit = db.relationship('Unit', back_populates='concepts')


    def __repr__(self):
        return f"<Concept concept_id={self.concept_id}>"
=======
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
>>>>>>> 843c4f9 (Add files remotely)

class Problem(db.Model):

    __tablename__ = "problems"

<<<<<<< HEAD
    problem_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    point_worth = db.Column(db.Integer)
    concept_id = db.Column(db.Integer)

    problem_progress = db.relationship('ProblemProgress', back_populates='problem')

    def __repr__(self):
        return f"<Problem problem_id={self.problem_id}>"
=======
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
>>>>>>> 843c4f9 (Add files remotely)


class UnitProgress(db.Model):

    __tablename__ = "units_complete"

<<<<<<< HEAD
    units_done = db.Column(db.String(100))
    units_completion = db.Column(db.Boolean, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    unit_id = db.Column(db.Integer, db.ForeignKey('units.unit_id'))


=======
    id = db.Column(db.Float, primary_key=True)
    units_done = db.Column(db.String(100))
    completion = db.Column(db.Boolean)
    # foreign keys out
    student_id = db.Column(db.Float, db.ForeignKey('students.id'))
    unit_id = db.Column(db.Float, db.ForeignKey('units.id'))
    # foreign keys out relationships
>>>>>>> 843c4f9 (Add files remotely)
    student = db.relationship('Student', back_populates='unit_progress')
    unit = db.relationship('Unit', back_populates='unit_progress')

    def __repr__(self):
<<<<<<< HEAD
        return f"<UnitProgress completion={self.Units_completion}>"
=======
        return f"<UnitProgress id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)


class ConceptProgress(db.Model):

    __tablename__ = "concepts_complete"

<<<<<<< HEAD
    concepts_done = db.Column(db.String(100))
    concepts_completion = db.Column(db.Boolean, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    concept_id = db.Column(db.Integer, db.ForeignKey('concepts.concept_id'))

=======
    id = db.Column(db.Float, primary_key=True)
    concepts_done = db.Column(db.String(100))
    completion = db.Column(db.Boolean)
    # foreign keys out
    student_id = db.Column(db.Float, db.ForeignKey('students.id'))
    concept_id = db.Column(db.Float, db.ForeignKey('concepts.id'))
    # foreign keys out relationships
>>>>>>> 843c4f9 (Add files remotely)
    student = db.relationship('Student', back_populates='concept_progress')
    concept = db.relationship('Concept', back_populates='concept_progress')


    def __repr__(self):
<<<<<<< HEAD
        return f"<ConceptProgress completion={self.concepts_completion}>"
=======
        return f"<ConceptProgress id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class ProblemProgress(db.Model):

    __tablename__ = "problems_complete"
<<<<<<< HEAD

    problems_done = db.Column(db.String(100))
    problems_completion = db.Column(db.Boolean, primary_key=True)
    points_gained = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    problem_id = db.Column(db.Integer, db.ForeignKey('problems.problem_id'))

=======
    
    id = db.Column(db.Float, primary_key=True)
    problems_done = db.Column(db.String(100))
    completion = db.Column(db.Boolean)
    points_gained = db.Column(db.Integer)
    # foreign keys out
    student_id = db.Column(db.Float, db.ForeignKey('students.id'))
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    # foreign keys out relationships
>>>>>>> 843c4f9 (Add files remotely)
    student = db.relationship('Student', back_populates='problem_progress')
    problem = db.relationship('Problem', back_populates='problem_progress')


    def __repr__(self):
<<<<<<< HEAD
        return f"<ProblemProgress problem_id={self.problems_completion}>"
=======
        return f"<ProblemProgress id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class Goal(db.Model):

    __tablename__ = "goals"

<<<<<<< HEAD
    goal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    r_w_apps = db.Column(db.String(100))

    concept = db.relationship('Concept', back_populates='goal')

    def __repr__(self):
        return f"<Goal goal_id={self.goal_id}>"
=======
    id = db.Column(db.Float, primary_key=True)
    applications = db.Column(db.String(100))
    # foreign key relationships in
    concept = db.relationship('Concept', back_populates='goal')

    def __repr__(self):
        return f"<Goal id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)


class UnitEquation(db.Model):

    __tablename__ = "unit_equations"

<<<<<<< HEAD
    unit_equation_set = db.Column(db.String(100), primary_key=True)
    equation_id = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<UnitEquation equation_id={self.equation_id}>"
=======
    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    unit_id = db.Column(db.Float, db.ForeignKey('units.id'))
    equation_id = db.Column(db.Float, db.ForeignKey('equations.id'))
    # foreign keys out relationships
    unit = db.relationship('Unit', back_populates='unit_equation')
    equation = db.relationship('Equation', back_populates='unit_equation')
   

    def __repr__(self):
        return f"<UnitEquation id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class ConceptEquation(db.Model):

    __tablename__ = "concept_equations"
<<<<<<< HEAD

    concept_equation_set = db.Column(db.String(100), primary_key=True)
    concept_id = db.Column(db.Integer)
    equation_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<ConceptEquation equation_id={self.equation_id}>"
=======
    
    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    concept_id = db.Column(db.Float, db.ForeignKey('concepts.id'))
    equation_id = db.Column(db.Float, db.ForeignKey('equations.id'))
    # foreign keys out relationships
    concept = db.relationship('Concept', back_populates='concept_equation')
    equation = db.relationship('Equation', back_populates='concept_equation')
   
    def __repr__(self):
        return f"<ConceptEquation id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class ProblemEquation(db.Model):

    __tablename__ = "problem_equations"

<<<<<<< HEAD
    problem_equation_set = db.Column(db.String(100), primary_key=True)
    problem_id = db.Column(db.Integer)
    equation_id = db.Column(db.String)

    def __repr__(self):
        return f"<ProblemEquation equation_id={self.equation_id}>"
=======
    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    equation_id = db.Column(db.Float, db.ForeignKey('equations.id'))
    # foreign keys out relationships
    problem = db.relationship('Problem', back_populates='problem_equation')
    equation = db.relationship('Equation', back_populates='problem_equation')
   

    def __repr__(self):
        return f"<ProblemEquation id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class UserInput(db.Model):

    __tablename__ = "user_inputs"

<<<<<<< HEAD
    user_input_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    problem_id = db.Column(db.Integer)
    all_inputs = db.Column(db.String)

    def __repr__(self):
        return f"<UserInput user_input_id={self.user_input_id}>"
=======
    id = db.Column(db.Float, primary_key=True)
    all_inputs = db.Column(db.String)
    # foreign keys out
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    # foreign keys out relationships
    problem = db.relationship('Problem', back_populates='user_input')

    def __repr__(self):
        return f"<UserInput id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class Equation(db.Model):

    __tablename__ = "equations"

<<<<<<< HEAD
    equation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    equation = db.Column(db.String(100))

    def __repr__(self):
        return f"<Equation equation_id={self.equation_id}>"
=======
    id = db.Column(db.Float, primary_key=True)
    equation = db.Column(db.String(100))
    # foreign keys in relationships
    unit_equation = db.relationship('UnitEquation', back_populates='equation')
    concept_equation = db.relationship('ConceptEquation', back_populates='equation')
    problem_equation = db.relationship('ProblemEquation', back_populates='equation')


    def __repr__(self):
        return f"<Equation id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)

class MathExpression(db.Model):

    __tablename__ = "math_expressions"

<<<<<<< HEAD
    expression_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    problem_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<MathExpression expression_id={self.expression_id}>"
=======
    id = db.Column(db.Float, primary_key=True)
    # foreign keys out
    problem_id = db.Column(db.Float, db.ForeignKey('problems.id'))
    # foreign keys out relationships
    problem = db.relationship('Problem', back_populates='math_expression')

    def __repr__(self):
        return f"<MathExpression id={self.id}>"
>>>>>>> 843c4f9 (Add files remotely)


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    db.create_all()
    print("Connected to the db!")

if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)
