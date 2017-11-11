import json

path = "contacts.json"

with open(path) as file:
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

def get_all(myjson, key):
    if type(myjson) is dict:
        for jsonkey in myjson:
            if type(myjson[jsonkey]) in (list, dict):
                get_all(myjson[jsonkey], key)
            elif jsonkey == key:
                print(myjson[jsonkey])
    elif type(myjson) is list:
        for item in myjson:
            if type(item) in (list, dict):
                get_all(item, key)


#get_all(contacts, "WI7")
