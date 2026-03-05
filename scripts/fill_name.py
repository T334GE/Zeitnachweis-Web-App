NAME_VALUE_CELL = "D1"


def fill_name(workbook, name):
    try:
        sheet = workbook.active
        sheet[NAME_VALUE_CELL] = name
    except Exception as e:
        raise ValueError(f"Failed to fill name in template: {e}")
