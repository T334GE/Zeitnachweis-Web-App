from get_status_label import get_status_label

WORK_STATUSES = {"A", "P", "ANWESEND"}
HOLIDAY_INDICATOR = "Feiertag"
DATE_COLUMN = 1
DEFAULT_HEADER_ROW = 6
DEFAULT_STATUS_COLUMN = 2
DEFAULT_START_TIME_COLUMN = 4
DEFAULT_END_TIME_COLUMN = 5
DEFAULT_BREAK_COLUMN = 6
FIRST_SHEET_INDEX = 0
MINUTES_PER_HOUR = 60
TIME_FORMAT_HOURS = "02d"
TIME_FORMAT_MINUTES = "02d"


def write_work_data(
    wb,
    work_days_with_dates: list,
    header_row: int = DEFAULT_HEADER_ROW,
    status_column: int = DEFAULT_STATUS_COLUMN,
    start_time_column: int = DEFAULT_START_TIME_COLUMN,
    end_time_column: int = DEFAULT_END_TIME_COLUMN,
    break_column: int = DEFAULT_BREAK_COLUMN,
):
    if not wb.sheetnames:
        print("⚠️  Warning: No sheets found in workbook - cannot write work data")
        return

    ws = wb[wb.sheetnames[FIRST_SHEET_INDEX]]

    for day, date_obj in work_days_with_dates:
        target_row = header_row + date_obj.day

        if target_row > ws.max_row:
            sheet_name = (
                wb.sheetnames[FIRST_SHEET_INDEX] if wb.sheetnames else "unknown"
            )
            print(
                f"⚠️  Warning: Cannot write data for {day.date} "
                f"({date_obj.strftime('%Y-%m-%d')}) - "
                f"row {target_row} exceeds sheet '{sheet_name}' max row {ws.max_row}"
            )
            continue

        current_status = ws.cell(row=target_row, column=status_column).value
        current_start = ws.cell(row=target_row, column=start_time_column).value
        current_end = ws.cell(row=target_row, column=end_time_column).value
        current_break = ws.cell(row=target_row, column=break_column).value

        is_holiday = current_status and HOLIDAY_INDICATOR in str(current_status)

        ws.cell(row=target_row, column=DATE_COLUMN, value=date_obj)

        if (
            current_status is None
            or current_status == ""
            or (is_holiday and day.status in WORK_STATUSES)
        ):
            ws.cell(
                row=target_row,
                column=DEFAULT_STATUS_COLUMN,
                value=get_status_label(day.status),
            )

        if day.status in WORK_STATUSES:
            if (
                current_start is None
                or current_start == ""
                or (is_holiday and day.status in WORK_STATUSES)
            ):
                ws.cell(
                    row=target_row,
                    column=DEFAULT_START_TIME_COLUMN,
                    value=day.start_time,
                )

            if (
                current_end is None
                or current_end == ""
                or (is_holiday and day.status in WORK_STATUSES)
            ):
                ws.cell(
                    row=target_row, column=DEFAULT_END_TIME_COLUMN, value=day.end_time
                )

            if (
                current_break is None
                or current_break == ""
                or (is_holiday and day.status in WORK_STATUSES)
            ):
                ws.cell(
                    row=target_row,
                    column=DEFAULT_BREAK_COLUMN,
                    value=f"{day.break_minutes // MINUTES_PER_HOUR:{TIME_FORMAT_HOURS}}:{day.break_minutes % MINUTES_PER_HOUR:{TIME_FORMAT_MINUTES}}",
                )
        else:
            if current_status is None or current_status == "":
                ws.cell(
                    row=target_row,
                    column=DEFAULT_STATUS_COLUMN,
                    value=get_status_label(day.status),
                )
