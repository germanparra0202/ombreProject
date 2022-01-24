from flask import Flask, request
from flask_restful import Api, Resource, reqparse

# Creating the Application and the API 
app = Flask(__name__)
api = Api(app)

# Adding the entries, don't have to be required 
ingredient_put_args = reqparse.RequestParser()
ingredient_put_args.add_argument("protein", type=str, help="Protein is suggested if needed")
ingredient_put_args.add_argument("fat", type=int, help="Fat is suggested if needed")
ingredient_put_args.add_argument("carbohydrate", type=int, help="Carbohydrate is suggested if needed")
ingredient_put_args.add_argument("sugar", type=int, help="Sugar is suggested if needed")

# This will be the dictionary that stores the parameters for ingredients
ingredients = {}

# Defining the /foods class
class foods(Resource):
    def get(self, ingredient_id):
        return ingredients[ingredient]

    # If you want to create a certain 
    def put(self, ingredient_id):
        args = ingredient_put_args.parse_args()
        return {ingredient_id: args}

# Adding the /foods endpoint
api.add_resource(foods, "/foods/<int:ingredient_id>")

# Running the actual application
if __name__ == "__main__":
    app.run(debug=True) # Debug = true only when developing, take it off