import json

def save_data(my_dict: dict):
    with open('notebook.txt', 'w') as my_data:
        json.dump(my_dict, my_data)

def load_data():
    with open('notebook.txt') as my_data:
        return json.load(my_data)
