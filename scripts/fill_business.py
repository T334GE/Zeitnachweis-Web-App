BUSINESS_CELL = "D4"


def fill_business(workbook, business):
    try:
        sheet = workbook.active
        sheet[BUSINESS_CELL] = business
    except Exception as e:
        raise ValueError(f"Failed to fill Business/Geschäft in template: {e}")
