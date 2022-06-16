#import json
import json

#inputs
json_filename=input('enter_json_file_name=')+'.json'
#with open is used to open file
with open(json_filename, 'r') as f:
 #data is used to load the json file
  data = json.load(f)

#print(data)
print(data)