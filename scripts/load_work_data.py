from typing import List
import json
from WorkDay import WorkDay
from validate_file_path import validate_file_path
from get_file_extension import get_file_extension
from load_json_data import load_json_data
from process_work_day_data import process_work_day_data


DEFAULT_DATA_FILE = "../input/data.json"


def load_work_data(data_file_path: str = DEFAULT_DATA_FILE) -> List[WorkDay]:
    validate_file_path(data_file_path)

    try:
        if get_file_extension(data_file_path) == ".json":
            data = load_json_data(data_file_path)
            return process_work_day_data(data, "json")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON file: {e}") from e
    except (PermissionError, OSError) as e:
        raise RuntimeError(f"Error accessing data file: {e}") from e


__all__ = [
    "WorkDay",
    "load_work_data",
    "validate_file_path",
    "get_file_extension",
    "process_work_day_data",
]
