from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a flask instance
app = Flask(__name__)
# Add Database
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://root:root@mysql-start:3306/Area"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Intilaize The Database
db = SQLAlchemy(app)


# Create a Model
class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100), unique=False, nullable=False)
    shop = db.Column(db.String(200), unique=True, nullable=False)
    

    # Create A string
    def __repr__(self):
        return "<Users %r>" % self.area



