#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
from load_work_data import load_work_data
from export_with_holidays import export_with_holidays

DEFAULT_STATE_CODE = "NI"
DEFAULT_INPUT_DIR = "../input"
DEFAULT_OUTPUT_DIR = "../output"
STATE_CODE_LENGTH = 2
EXIT_CODE_ERROR = 1


def start_time_export():
    parser = argparse.ArgumentParser(
        description="Export work data to Excel files with holiday integration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Usage examples:
  python start_time_export.py BY
  python start_time_export.py NI ../input/my_data.json
  python start_time_export.py NI ../input/my_data.json""",
    )

    parser.add_argument(
        "state_code",
        nargs="?",
        default=DEFAULT_STATE_CODE,
        help="German state code (default: NI)",
    )
    parser.add_argument("data_file", nargs="?", help="Path to data file (JSON)")
    parser.add_argument(
        "--input-dir",
        default=DEFAULT_INPUT_DIR,
        help="Input directory path (default: ../input)",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory path (default: ../output)",
    )

    args = parser.parse_args()

    if len(args.state_code) != STATE_CODE_LENGTH:
        print("❌ Error: State code must be 2 characters (e.g., NI, BY, BW)")
        sys.exit(EXIT_CODE_ERROR)

    data_file = args.data_file
    if data_file is None:
        json_file = Path(args.input_dir) / "data.json"

        if json_file.exists():
            data_file = str(json_file)
        else:
            print(
                f"❌ No data file found in {args.input_dir}. Please create data.json."
            )
            print(
                "   Use: python import_data.py to create a data file from your time data."
            )
            sys.exit(EXIT_CODE_ERROR)

    print("=== Excel Export ===")
    print(f"State: {args.state_code}")
    print(f"Output: {args.output_dir}/ZEITNACHWEIS_[year]_[month].xlsx")
    print(f"Data: {data_file}")

    try:
        work_days = load_work_data(data_file)
        if not work_days:
            print("❌ No valid work data found. Exiting.")
            sys.exit(EXIT_CODE_ERROR)

        print(f"Loaded {len(work_days)} work days")

        success = export_with_holidays(
            work_days, args.state_code, output_dir=args.output_dir
        )

        if success:
            print("✅ Export completed successfully!")
        else:
            print("❌ Export failed!")
            sys.exit(EXIT_CODE_ERROR)

    except (ValueError, FileNotFoundError, RuntimeError, OSError) as e:
        print(f"❌ Error: {e}")
        sys.exit(EXIT_CODE_ERROR)
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(EXIT_CODE_ERROR)


if __name__ == "__main__":
    start_time_export()
