from typing import Dict, Any
import requests
from get_german_holidays import get_german_holidays


def fetch_holidays(
    months_in_data: set, state_code_param: str
) -> Dict[int, Dict[str, Any]]:
    years_in_data = {year for year, _ in months_in_data}
    all_holidays = {}

    for year in years_in_data:
        try:
            holidays = get_german_holidays(year, state_code_param)
            all_holidays[year] = {holiday["date"]: holiday for holiday in holidays}
        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            print(
                f"⚠️  Warning: Error fetching holidays for {year} (state: {state_code_param}): {e}"
            )

    return all_holidays
