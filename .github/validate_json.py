import json
import sys

# e.g. python3 demo.py test.json
#  => {'Key1': 'value1', 'Key2': 'value2', 'Key3': 'value3'}

input_json = sys.argv[1]

with open(input_json, 'r') as json_file:
  output = json.load(json_file)
  print(output)
