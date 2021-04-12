'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: JSON (Read JSON File)
'''
import json

with open('person.json') as file1:
  data = json.load(file1)
print(data)
