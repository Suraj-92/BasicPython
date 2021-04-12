'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: JSON (Writing to JSON File)
'''

import json

person_dict = {"name": "Suraj",
"languages": ["English", "Marathi"],
"married": False,
"age": 22
}

with open('person2.txt', 'w') as json_file:
  json.dump(person_dict, json_file)
