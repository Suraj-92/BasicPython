'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: JSON (Convert from Python to JSON)
'''

import json

# Python object (dict)
dict1 = {
  "name": "Suraj",
  "age": 22,
  "city": "Ratnagiri"
}

# convert into JSON
result = json.dumps(dict1)

# result is a JSON string
print(result)
