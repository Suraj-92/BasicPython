'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: JSON (Parse JSON File)
'''

import json

person = '{"name": "suraj", "languages": ["English", "Marathi"]}'
person_dict = json.loads(person)

print( person_dict)

print(person_dict['languages'])
