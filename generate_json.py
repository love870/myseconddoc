# -*- coding: utf-8 -*-

# importing the module
import json,ast


# reading the data from the file
with open('random.txt') as f:
    data = f.read()


# Convert Python Dictionary Into Json
convert_data = json.loads(data)


# Removing uni-code chars
convert_data=ast.literal_eval(json.dumps(convert_data))

print("----- Your Json Data is ----")

# Printing Json Object
print(convert_data)
  
    
