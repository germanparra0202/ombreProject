from flask import Flask
from flask_restful import Api, Resource

# Creating the Application and the API 
app = Flask(__name__)
api = Api(app)

# This will be the dictionary that stores the parameters for ingredients
ingredients = {}

# Defining the /foods class
class foods(Resource):
    pass

# Adding the /foods endpoint
api.add_resource(foods, "/foods")

# Running the actual application
if __name__ == "__main__":
    app.run(debug=True) # Debug = true only when developing, take it off