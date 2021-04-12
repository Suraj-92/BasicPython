'''
Author: Suraj N Temkar
Date: 12/04/2021
Title: JSON (Simple Example...)
'''

import json

dict1 = {
  "name": "suraj",
  "age": 20,
  "married": False,
  "divorced": False,
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(dict1))        # convert it into a JSON string by using the json.dumps()
print(json.dumps(dict1, indent=4))  # indent parameter to define the numbers of indents
print(json.dumps(dict1, indent=4, separators=(". ", " = ")))    # separators parameter to change the default separator
print(json.dumps(dict1, indent=4, sort_keys=True))  # sort_keys parameter to specify if the result should be sorted or not
