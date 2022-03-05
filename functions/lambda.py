people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

"""
# This is the equivalent to lambda function below:

def f(person):
    return person["name"]
"""

people.sort(key=lambda person: person['name'])

print(people)
