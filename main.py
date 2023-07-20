import requests
import json
import os

aws_metadata_url = 'http://169.254.169.254/latest/'


def expand_tree(url, arr):
    output = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = expand_tree(new_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output


def get_data(path):
    initial = [path]
    result = expand_tree(aws_metadata_url, initial)
    return result


def get_data_json(path):
    aws_metadata = get_data(path)
    metadata_json = json.dumps(aws_metadata, indent=4, sort_keys=True)
    return metadata_json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(get_data_json("meta-data/"))
    print(get_data_json("dynamic/"))
    print("")
