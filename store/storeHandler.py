import json

class StoreHandler:

    def getAll():
        with open('data.json') as json_file:
            return json.load(json_file)

    def getValue(key):
        with open('data.json') as json_file:
            data = json.load(json_file)
            return data[key]

    def setValue(key, value):
        data = {}
        with open('data.json') as json_file:
            data = json.load(json_file)
            data[key] = value

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

    def removeKey(key):
        data = {}
        with open('data.json') as json_file:
            data = json.load(json_file)
            try:
                del data[key]    
            except Exception as err:
                pass

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
