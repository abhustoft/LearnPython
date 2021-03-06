import json 
import pickle

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
print(json.loads(json_string))

def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary
    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)

print("Pickled:")
print(new_salaries)

print("Dumped:")
print(json.dumps(new_salaries))

decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])