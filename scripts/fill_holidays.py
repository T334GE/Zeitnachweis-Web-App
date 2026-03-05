def fill_holidays(wb, months_in_data: set, all_holidays: dict):
    FIRST_DAY_OF_MONTH = 1
    LAST_DAY_OF_MONTH = 31
    HEADER_ROW_OFFSET = 6
    STATUS_COLUMN = 2
    START_TIME_COLUMN = 4
    END_TIME_COLUMN = 5
    BREAK_COLUMN = 6
    COMMENT_COLUMN = 7

    for year, month in sorted(months_in_data):
        sheet_name = f"{month:02d}-{year}"
        if sheet_name not in wb.sheetnames:
            continue

        ws = wb[sheet_name]
        year_holidays = all_holidays.get(year, {})

        holiday_updates = []

        for day in range(FIRST_DAY_OF_MONTH, LAST_DAY_OF_MONTH + 1):
            target_row = HEADER_ROW_OFFSET + day
            if target_row > ws.max_row:
                break

            date_str = f"{year}-{month:02d}-{day:02d}"
            if date_str in year_holidays:
                holiday_updates.extend(
                    [
                        (target_row, STATUS_COLUMN, "Feiertag"),
                        (target_row, START_TIME_COLUMN, None),
                        (target_row, END_TIME_COLUMN, None),
                        (target_row, BREAK_COLUMN, None),
                        (target_row, COMMENT_COLUMN, None),
                    ]
                )

        for row, col, value in holiday_updates:
            ws.cell(row=row, column=col, value=value)
