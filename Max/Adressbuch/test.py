import json
import csv

path1 = "Ingo.json"
path2 ="Contacts.csv"


def read(path, type):
    try:
        list_of_dicts = []
        if type == "csv":
            with open(path, "r", newline='', encoding="utf8") as file:
                reader = csv.DictReader(file)
                for v in reader:
                    list_of_dicts.append(v)
                return list_of_dicts
        elif type == "json":
            with open(path1) as file:
                list_of_dicts = json.load(file)
                return list_of_dicts
    except IOError:
        print('An error occured trying to read the file.')


print(read(path2, "csv"))


with open(path1) as file:
    global contacts
    contacts = json.load(file)


def find_value(obj, term):
    global result
    result = []

    def search(obj, term):
        if type(obj) == dict:
            for key in obj:
                #print(key)
                if key == term:
                    #print(key)
                    print(obj[key])

                    # for item in obj(key):
                    #     result.append(item)

                else:
                    search(obj[key], term)
    search(obj, term)
    return result

print(contacts)

#find_value(contacts, "dozenten")
#dozenten = find_value(contacts, "dozenten")
#print(dozenten)


def get_key(myjson, key):
    if type(myjson) is dict:
        for jsonkey in myjson:
            if jsonkey == key:
                print(myjson[jsonkey])
            elif type(myjson[jsonkey]) in (list, dict):
                get_key(myjson[jsonkey], key)
    elif type(myjson) is list:
        for item in myjson:
            if type(item) in (list, dict):
                get_key(item, key)


#get_key(contacts[0], "Rufnummern")

def get_rufnummern_and_email_range():
    largest_number = 0
    largest_email = 0
    for contact in contacts:
        number_string = ""
        for item in contact["Rufnummern"]:
            number_string = item["Type"] + item["Number"]
