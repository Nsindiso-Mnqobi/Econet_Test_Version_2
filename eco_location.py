from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Create a flask instance 
app = Flask(__name__)

#Add Database 
app.config('SQLALCHEMY_DATABASE_URI') = "mysql://root:root@localhost:3306/Area"

#Intilaize The Database 
db = SQLAlchemy()


if  __name__ == "__main__":
    app.run(debug=True)