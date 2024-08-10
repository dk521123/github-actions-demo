import tomllib
import sys

# e.g. python3 validate_toml.py test.toml
input_toml = sys.argv[1]

with open(input_toml,'rb') as file:
  output = tomllib.load(file)
  print(output)
