import json
import os

def read_from_json_file(file_path: str) -> json:
    """
    Return data from json file
    :param file_path: path to json file to read
    :return:
    """

    file_path = os.path.join(os.getcwd(), file_path)
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data


