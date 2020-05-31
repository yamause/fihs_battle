import json

with open('parameter_seeds.json') as f:
    test_dict = json.load(f)

# print(test_dict)

print(test_dict["my_status"])