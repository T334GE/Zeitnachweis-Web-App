MONTH_CELL = "D2"

# German month names
GERMAN_MONTHS = {
    1: "Januar",
    2: "Februar",
    3: "März",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Dezember"
}


def fill_month_name(sheet, month_number, year):
    try:
        month_name = GERMAN_MONTHS.get(month_number, "")
        if month_name:
            full_month_name = f"{month_name} {year}"
        else:
            full_month_name = f"Monat {month_number} {year}"
        sheet[MONTH_CELL] = full_month_name
    except Exception as e:
        raise ValueError(f"Failed to fill month name in sheet: {e}")
