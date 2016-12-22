import json
from pprint import pprint
import os.path
import argparse


def load_data(filepath):
    '''reads data from json file'''
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding="utf8") as json_file:
        return json.load(json_file)

def pretty_print_json(data):
    '''takes data, prints to console in a readable format'''
    pprint(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Данная программа принимает от пользователя путь к файлу json и выводит содержимое файла в консоль в читаемом виде')
    args = parser.parse_args()

    while True:
        json_path = input("Укажите путь к существующему файлу json: ")
        data = load_data(json_path)
        if data is not None:
            break

    pretty_print_json(data)
