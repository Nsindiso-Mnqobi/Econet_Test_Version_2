from email.policy import default
from msilib.schema import CreateFolder
import string
from sunau import Au_read
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Create a flask instance 
app = Flask(__name__)

#Add Database 
app.config('SQLALCHEMY_DATABASE_URI') == "mysql://root:root@localhost:3306/Area"

#Intilaize The Database 
db = SQLAlchemy()

#Create a Model 
class Users(db.Model):
    id = db.column(db.integer, primary_key=True)
    Area = db.column(db.string(200), nullable=False,unique=True)
    Shop = db.column(db.string(200), nullable=False,unique=True)
    Date = db.column(db.datetime, default = datetime.utcnow)

    #Create A string
    def __repr__(self):
        return '<Name %r>' % self.name

if  __name__ == "__main__":
    app.run(debug=True)