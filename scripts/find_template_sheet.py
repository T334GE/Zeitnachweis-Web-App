from typing import Optional, Any
import importlib.util


def find_template_sheet(wb) -> Optional[Any]:
    try:
        template_sheet = next(
            (sheet for sheet in wb.sheetnames if sheet.lower() == "template"), None
        )
        return wb[template_sheet]
    except (AttributeError, KeyError, IndexError, ValueError) as e:
        print(f"⚠️  Warning: Error accessing workbook sheets: {e}")
        template_sheet = wb.create_sheet(title="Template")
        spec = importlib.util.spec_from_file_location(
            "create_basic_headers", "create_basic_headers.py"
        )
        create_basic_headers_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(create_basic_headers_module)
        create_basic_headers_module.create_basic_headers(template_sheet)
        return template_sheet
