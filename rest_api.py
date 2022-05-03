from database import Users, db, app
from flask_restx import Resource, Api, reqparse, abort, fields

# Instantiate API
api = Api(app)

# Create Variables
Area = ""
Shop = ""

# Create Parser for delete and Post request
parser = reqparse.RequestParser()
parser.add_argument("Area", required=True, help="Area cannot be blank!")
parser.add_argument("Shop", required=True, help="Shop cannot be blank!")

# Create Parser for GET Request
parser_2 = reqparse.RequestParser()
parser_2.add_argument("Area", required=True, help="Area cannot be blank!")

# Create API Models
Area = api.model("Area", {"Area": fields.String("Harare CBD")})
Shop = api.model(
    "Shop",
    {"Area": fields.String("Harare CBD"), "Shop": fields.String("Joina")},
)

# Create Class
class Location(Resource):

    # Get Request
    @api.expect(Area)
    def get(self,):
        args = parser_2.parse_args()
        Area = args["Area"]
        shop_list = []
        Shops = Users.query.filter_by(area=Area).all()
        for shop in Shops:
            if shop.area == Area:
                shop_list.append(shop.shop)
            elif shop.area is None:
                abort(404, message="The area is not avalaible in the system")
            else:
                abort(201, message=" No Shops in this area")
        return {"Shops": shop_list}

    # Put Request
    @api.expect(Shop)
    def put(self):
        args = parser.parse_args()
        Area = args["Area"]
        Shop = args["Shop"]
        data = Users(area=Area, shop=Shop)
        db.session.add(data)
        db.session.commit()
        return {"Area": Area, "Shop": Shop}

    # Delete Request
    @api.expect(Shop)
    def delete(self):
        args = parser.parse_args()
        Area = args["Area"]
        Shop = args["Shop"]
        Users.query.filter_by(shop=Shop).delete()
        db.session.commit()
        return {"Area": Area, "Deleted Shop": Shop}

    # Post Request to create database
    def post(self):
        db.create_all()
        return "Database has been created"


api.add_resource(Location, "/location/")

if __name__ == "__main__":
    app.run(debug=True)
