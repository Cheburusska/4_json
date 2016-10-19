import json
from pprint import pprint

json_path = 'json/alcohol.json' #path to the json file


def load_data(filepath): #takes path to file, returns data in python format
    with open(filepath, encoding="utf8") as json_file:
        data = json.load(json_file)
        return data


def pretty_print_json(data): #takes data, prints to console in a readable format
    pprint(data)


def main():
    data = load_data(json_path)
    pretty_print_json(data)


if __name__ == '__main__':
    main()
