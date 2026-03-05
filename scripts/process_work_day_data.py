from typing import List, Dict, Any
from WorkDay import WorkDay
from create_work_day_from_dict import create_work_day_from_dict
from handle_validation_error import handle_validation_error


def process_work_day_data(data: List[Dict[str, Any]], file_type: str) -> List[WorkDay]:
    valid_work_days = []

    for i, day_data in enumerate(data):
        try:
            work_day = create_work_day_from_dict(day_data)
            valid_work_days.append(work_day)
        except (TypeError, AttributeError, ValueError) as e:
            handle_validation_error(e, day_data, i, file_type)

    return valid_work_days
