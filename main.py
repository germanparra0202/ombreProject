from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource, reqparse

import json

# Creating the Application and the API 
app = Flask(__name__)
api = Api(app)

# Adding the entries, don't have to be required 
'''
Not actually needed 

ingredient_put_args = reqparse.RequestParser()
ingredient_put_args.add_argument("protein", type=str, help="Protein is suggested if needed")
ingredient_put_args.add_argument("fat", type=int, help="Fat is suggested if needed")
ingredient_put_args.add_argument("carbohydrate", type=int, help="Carbohydrate is suggested if needed")
ingredient_put_args.add_argument("sugar", type=int, help="Sugar is suggested if needed")'''

# This will be the dictionary that stores the parameters for ingredients
ingredients = {}

# Defining the /foods class
'''class foods(Resource):
    def get(self, ingredient_id):
        return ingredients[ingredient]

    # If you want to create a certain 
    # This will maybe store the info on the dict and then take action from there 
    def put(self, ingredient_id):
        args = ingredient_put_args.parse_args()
        return {ingredient_id: args}

# Adding the /foods endpoint
api.add_resource(foods, "/foods/<int:ingredient_id>")'''

# Routes 
@app.route("/")
def index():
    # should be index.html
    return render_template('index.html')

# Create the route to get the json() data
@app.route("/foods")
def ingredients():

    return render_template('questions.html')

@app.route("/foods", methods=["GET", "POST"])
def foods():

    protein = request.form['slider_protein']
    protein = float(protein)
    fat     = request.form['slider_fats']
    fat     = float(fat)
    carbs   = request.form['slider_carbohydrates']
    carbs   = float(carbs)
    sugar   = request.form['slider_sugar']
    sugar   = float(sugar)

    proteinValue = 0
    fatValue = 0
    carbValue = 0
    sugarValue = 0

    listAppend = ['Here are the reccommended meals for the inputted values.']
    with open('food_data.json') as json_file:
        data = json.load(json_file)

    for i in data['report']['foods']:
    # if i['nutrient_id'] == 203:
        proteinValue = 0
        fatValue = 0
        carbValue = 0
        sugarValue = 0
        counter = 0

        for j in i['nutrients']:

            if isinstance(j['gm'], float) == False:
                continue
            
            else:

                if (j['nutrient_id'] == '203' and float(j['gm']) > protein):
                    proteinValue = 1
                elif (j['nutrient_id'] == '205' and float(j['gm']) > carbs): 
                    carbValue = 1
                elif (j['nutrient_id'] == '204' and float(j['gm']) > fat):
                    fatValue = 1
                elif (j['nutrient_id'] == '269' and float(j['gm']) > sugar):
                    sugarValue = 1


                if (proteinValue == 1) and (carbValue == 1) and (fatValue == 1) and (sugarValue == 1):     
                    listAppend.append(j)
                    counter = counter + 1

    # return using jsonify
    if counter == 0:
        listAppend.pop()
        listAppend.append("There are no meals for your inputs.")

        
    return jsonify(listAppend)


# Running the actual application
if __name__ == "__main__":
    app.run(debug=True) # Debug = true only when developing, take it off