from typing import List, Dict, Any
import requests
import time

API_BASE_URL = "https://date.nager.at/api/v3/publicholidays"
API_TIMEOUT = 10
MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 1
MIN_YEAR = 1900
MAX_YEAR = 2100
STATE_CODE_LENGTH = 2
HTTP_NOT_FOUND = 404

VALID_STATES = {
    "BY",
    "BW",
    "BE",
    "BB",
    "HB",
    "HH",
    "HE",
    "MV",
    "NI",
    "NW",
    "RP",
    "SL",
    "SN",
    "ST",
    "SH",
    "TH",
}

_holiday_cache = {}


def get_german_holidays(year: int, state_code: str) -> List[Dict[str, Any]]:
    if not isinstance(year, int) or year < MIN_YEAR or year > MAX_YEAR:
        raise ValueError(
            f"Year must be an integer between {MIN_YEAR} and {MAX_YEAR}, got {year}"
        )

    if not isinstance(state_code, str) or len(state_code) != STATE_CODE_LENGTH:
        raise ValueError(
            f"State code must be a {STATE_CODE_LENGTH}-character string, got {state_code}"
        )

    cache_key = f"{year}_{state_code.upper()}"
    if cache_key in _holiday_cache:
        return _holiday_cache[cache_key]

    for attempt in range(MAX_RETRIES):
        try:
            state_code_upper = state_code.upper()
            if state_code_upper not in VALID_STATES:
                print(
                    f"⚠️  Warning: Unknown state code '{state_code}', using default 'DE-NI'"
                )
                api_state_code = "DE-NI"
            else:
                api_state_code = f"DE-{state_code_upper}"

            response = requests.get(
                f"{API_BASE_URL}/{year}/{api_state_code}", timeout=API_TIMEOUT
            )

            if response.status_code == HTTP_NOT_FOUND:
                print(
                    f"⚠️  Warning: State-specific holidays not available for {api_state_code}, trying country-wide..."
                )
                response = requests.get(
                    f"{API_BASE_URL}/{year}/DE", timeout=API_TIMEOUT
                )

            response.raise_for_status()
            all_holidays = response.json()

            state_holidays = []
            for holiday in all_holidays:
                if holiday["global"] or api_state_code in (holiday["counties"] or []):
                    state_holidays.append(holiday)

            _holiday_cache[cache_key] = state_holidays
            return state_holidays

        except requests.exceptions.RequestException as e:
            if attempt == MAX_RETRIES - 1:
                print(
                    f"⚠️  Warning: Network error fetching holidays after {MAX_RETRIES} attempts: {e}"
                )
                print("   Continuing without holiday data...")
                _holiday_cache[cache_key] = []
                return []
            print(f"   Retry {attempt + 1}/{MAX_RETRIES}...")
            time.sleep(INITIAL_RETRY_DELAY * (2**attempt))
        except ValueError as e:
            print(f"⚠️  Warning: Invalid JSON response from holiday API: {e}")
            _holiday_cache[cache_key] = []
            return []
        except KeyError as e:
            print(f"⚠️  Warning: Unexpected holiday data format from API: {e}")
            _holiday_cache[cache_key] = []
            return []

    return []
