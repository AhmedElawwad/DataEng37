import json

car_data = {
    "make": "Tesla",
    "type": "Electric",
    "faults": 9384,
    "death_trap": True,
    "drive": None
}

# print(car_data['faults'])

dumps = json.dumps(car_data)
# print(dumps)


# with open("tesla.json", "w") as jsonfile:
#     json.dump(car_data, jsonfile)


# with open("tesla.json", "w") as jsonfile:
#     dumps =json.dump(car_data)
#     jsonfile.write(dumps)


with open("spartan.json") as jsonfile:
    spartan = json.load(jsonfile)

print(spartan, type(spartan))


