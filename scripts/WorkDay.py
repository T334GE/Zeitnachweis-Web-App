from dataclasses import dataclass, fields
from typing import List


@dataclass
class WorkDay:
    date: str
    weekday: str
    status: str
    status_label: str
    start_time: str
    end_time: str
    duration_minutes: int
    duration: str
    punch_count: int
    break_minutes: int
    fallback_end_applied: bool

    @classmethod
    def get_required_fields(cls) -> List[str]:
        return [field.name for field in fields(cls)]

    @classmethod
    def find_missing_fields(cls, data: dict, required_fields: List[str]) -> List[str]:
        return [field for field in required_fields if field not in data]
