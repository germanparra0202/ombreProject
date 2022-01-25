import json
from flask import jsonify
 
'''with open('food_data.json') as json_file:
    data = json.load(json_file)

counter = 0

for i in data['report']['foods']:
    # if i['nutrient_id'] == 203:
    for j in i['nutrients']:
        if j['nutrient'] == 'Protein':
            print(j)
            counter = counter + 1
            
            
print(counter)'''

def starting_url():

    listAppend = []
    
    with open('food_data.json') as json_file:
        data = json.load(json_file)

    for i in data['report']['foods']:
    # if i['nutrient_id'] == 203:
        for j in i['nutrients']:
            if j['nutrient'] == 'Protein':
                listAppend.append(j)

    # return using jsonify
    # print(listAppend)
    return listAppend

value = starting_url()

for i in value:
    print(i)