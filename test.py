# Author: German Parra

# Here we will test request to this test.py file
from flask import request

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "ingredient/1", {"ingredient": 5})

# Printing message
print(response.json())