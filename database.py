from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Create a flask instance 
app = Flask(__name__)
#Add Database 
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@172.17.0.2:3306/Area"

#Intilaize The Database 
db = SQLAlchemy(app)

#Create a Model 
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100), unique=True, nullable=False)
    shop = db.Column(db.String(200), unique=True, nullable=False)

    #Create A string
    def __repr__(self):
        return '<Users %r>' % self.area

if  __name__ == "__main__":
    app.run(debug=True)