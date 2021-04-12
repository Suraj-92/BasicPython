'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: JSON (Convert from JSON to Python)
'''

import json

# JSON Format
json1 =  '{ "name":"Suraj", "age":21, "city":"Ratnagiri"}'

# parse x
result = json.loads(json1)

# the result is a Python dictionary
print(result["age"])
