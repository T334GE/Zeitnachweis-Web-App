def create_basic_headers(sheet):
    try:
        sheet["A1"] = "Date"
        sheet["B1"] = "Status"
        sheet["C1"] = "Start Time"
        sheet["D1"] = "End Time"
        sheet["E1"] = "Break"
    except (AttributeError, ValueError) as e:
        print(f"⚠️  Warning: Error creating basic headers: {e}")
