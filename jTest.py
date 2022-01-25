import json 
 
with open('food_data.json') as json_file:
    data = json.load(json_file)

for i in data['report']['foods']:
    print(i)