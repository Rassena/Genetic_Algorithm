import json
import os

EASY_COST_PATH = "data/easy_cost.json"
EASY_FLOW_PATH = "data/easy_flow.json"
FLAT_COST_PATH = "data/flat_cost.json"
FLAT_FLOW_PATH = "data/flat_flow.json"
HARD_COST_PATH = "data/hard_cost.json"
HARD_FLOW_PATH = "data/hard_flow.json"



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


