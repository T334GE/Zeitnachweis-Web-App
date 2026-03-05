from typing import Dict, Any
from WorkDay import WorkDay


def create_work_day_from_dict(data: Dict[str, Any]) -> WorkDay:
    required_fields = WorkDay.get_required_fields()
    missing_fields = WorkDay.find_missing_fields(data, required_fields)

    if missing_fields:
        raise ValueError(f"Missing required fields: {missing_fields}")

    return WorkDay(**data)
