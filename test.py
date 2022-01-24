# Author: German Parra

# Here we will test request to this test.py file
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "foods/1", {"protein": 5}) # /foods must be the same as the main.py 

# Printing message
print(response.json())