from email import message
from re import S
from flask import Flask
from database import Users, db, app
from flask_restful import Resource, Api, reqparse, abort

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
        shop_list = []
        Shops = Users.query.filter_by(area=Area).all()
        for shop in Shops:
            if shop.area == Area:
                shop_list.append(shop.shop)
            elif Area != shop.area and shop.area == None:
                abort(404, message= "The area is not avalaible in the system")
            else: 
                abort(201,message=" No Shops in this area")
        return { "Shops" : shop_list}

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
            to_delete = Users.query.filter_by(shop=Shop).delete()
            db.session.commit()
            return { "Area" : Area, "Deleted Shop" : Shop}

api.add_resource(Location, '/location')

if __name__ == "__main__":
    app.run(debug=True)
