import json
from tinydb import TinyDB, Query
db = TinyDB("db.json")


def read_json(path):
    try:
        with open(path) as file:
            data = json.load(file)
            return data
    except IOError:
        print('An error occured trying to read the JSON file.')


def write_json(path, data):
    try:
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    except IOError:
        print('An error occured trying to write the JSON file.')


contacts = read_json("address_book_max.json")


for contact in contacts:
    db.insert(contact)


