from re import S
from flask import Flask
from database import Users, db, app
from flask_restful import Resource, Api, reqparse

# Instantiate API 
api = Api(app)

# Create Variables 
Area = ""
Shop = ""

# Create Parser
parser = reqparse.RequestParser()
parser.add_argument('Area',required=True,
                                help="Area cannot be blank!")
parser.add_argument('Shop',required=True,
                                help="Shop cannot be blank!")

parser_2 = reqparse.RequestParser()
parser_2.add_argument('Area',required=True,
                                help="Area cannot be blank!")



class Location(Resource):
    def get(self):
        args = parser_2.parse_args()
        Area = args['Area']
        Shops = Users.query.filter_by(area=Area).first()
        if Area == Shops.area:
            for shops in Shops.shops:
                return { "Shops" : shops}
        elif Area != Shops.area and Shops == None:
            return "The area is not avalaible in the system"
        else: 
            return "No Shops in this area"


    def put(self):
            args = parser.parse_args()
            Area = args['Area']
            Shop = args['Shop']
            data = Users(area =Area, shop=Shop)
            db.session.add(data)
            db.session.commit()
            return { "Area" : Area, "Shop" : Shop}
    
    def delete(self):
            args = parser.parse_args()
            Area = args['Area']
            Shop = args['Shop']
            data = Users(area =Area, shop=Shop)
            db.session.delete(data)
            db.session.commit()
            return { "Area" : Area, "Shop" : Shop}

api.add_resource(Location, '/location')

if __name__ == "__main__":
    app.run(debug=True)
