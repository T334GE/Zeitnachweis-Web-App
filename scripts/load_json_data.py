import json
from typing import List, Dict, Any


def load_json_data(data_file_path: str) -> List[Dict[str, Any]]:
    with open(data_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("JSON data must be a list of work day objects")

    return data
