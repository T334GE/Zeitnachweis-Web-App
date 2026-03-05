from typing import Dict, Any
from WorkDay import WorkDay


def handle_validation_error(
    error: ValueError, day_data: Dict[str, Any], index: int, file_type: str
) -> None:
    date_info = day_data.get(
        "date", f"{'index' if file_type == 'json' else 'row'} {index + 1}"
    )
    required_fields = WorkDay.get_required_fields()
    missing_fields = WorkDay.find_missing_fields(day_data, required_fields)

    if missing_fields:
        print(
            f"⚠️  Warning: Skipping {file_type} {'index' if file_type == 'json' else 'row'} {index + 1} "
            f"for {date_info} - missing required fields: {', '.join(missing_fields)}"
        )
        return

    print(
        f"⚠️  Warning: Skipping {file_type} {'index' if file_type == 'json' else 'row'} {index + 1} "
        f"for {date_info} - {error}"
    )
