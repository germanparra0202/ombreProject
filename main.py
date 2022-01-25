from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource, reqparse

import json

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
    # This will maybe store the info on the dict and then take action from there 
    def put(self, ingredient_id):
        args = ingredient_put_args.parse_args()
        return {ingredient_id: args}

# Adding the /foods endpoint
api.add_resource(foods, "/foods/<int:ingredient_id>")

# Routes 
@app.route("/")
def index():
    return render_template('index.html')

# Create the route to get the json() data
@app.route("/ingredients", methods=["GET"])
def ingredients():

    listAppend = []
    with open('food_data.json') as json_file:
        data = json.load(json_file)

    for i in data['report']['foods']:
    # if i['nutrient_id'] == 203:
        for j in i['nutrients']:
            if j['nutrient'] == 'Protein':
                listAppend.append(j)

    # return using jsonify
    return jsonify(listAppend)

# Running the actual application
if __name__ == "__main__":
    app.run(debug=True) # Debug = true only when developing, take it off