from datetime import datetime
import calendar

DEFAULT_DATE_COLUMN = 1
DEFAULT_HEADER_ROW = 6
ROW_OFFSET = 1


def update_sheet_dates(
    sheet,
    year,
    month,
    date_column: int = DEFAULT_DATE_COLUMN,
    header_row: int = DEFAULT_HEADER_ROW,
):
    max_day = calendar.monthrange(year, month)[1]

    date_updates = []

    for row in range(header_row + ROW_OFFSET, sheet.max_row + ROW_OFFSET):
        try:
            cell_value = sheet.cell(row=row, column=date_column).value
            if cell_value:
                if hasattr(cell_value, "day"):
                    day_num = cell_value.day
                else:
                    day_num = row - header_row

                if 1 <= day_num <= max_day:
                    new_date = datetime(year, month, day_num)
                    date_updates.append((row, date_column, new_date))
                else:
                    print(
                        f"⚠️  Warning: Invalid day {day_num} for {year}-{month:02d} (max: {max_day}), skipping row {row} - cell value: {cell_value}"
                    )

        except (ValueError, AttributeError, TypeError) as e:
            cell_value_info = (
                f"cell value: {cell_value}"
                if "cell_value" in locals()
                else "no cell value"
            )
            print(
                f"⚠️  Warning: Error updating date for row {row} in {year}-{month:02d}: {e} ({cell_value_info})"
            )
            continue

    for row, col, value in date_updates:
        sheet.cell(row=row, column=col, value=value)
