from pathlib import Path


def validate_paths(template_path: str, output_dir: str):
    template_dir = Path(template_path).parent
    output_dir_path = Path(output_dir)

    if not template_dir.exists():
        print(f"⚠️  Warning: Template directory {template_dir} does not exist")

    if not output_dir_path.exists():
        output_dir_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created output directory: {output_dir_path}")
