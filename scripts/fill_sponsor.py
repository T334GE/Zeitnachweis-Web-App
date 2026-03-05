SPONSOR_CELL = "D3"


def fill_sponsor(workbook, sponsor):
    try:
        sheet = workbook.active
        sheet[SPONSOR_CELL] = sponsor
    except Exception as e:
        raise ValueError(f"Failed to fill Sponsor/Träger/Kundennummer in template: {e}")
