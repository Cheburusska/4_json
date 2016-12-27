import json
import os, argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding="utf8") as json_file:
        return json.load(json_file)

def pretty_print_json(data_from_json):
    print (json.dumps(data_from_json, indent=4, sort_keys=True))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Данная программа принимает от пользователя путь к файлу json и выводит содержимое файла в консоль в читаемом виде')
    parser.add_argument('filepath', help='укажите файл в формате json')
    args = parser.parse_args()

    while True:
        data_from_json = load_data(args.filepath)
        if data_from_json is not None:
            break

    pretty_print_json(data_from_json)
