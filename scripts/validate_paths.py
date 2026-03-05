from pathlib import Path


def validate_paths(template_path: str, output_dir: str):
    template_dir = Path(template_path).parent

    if not template_dir.exists():
        print(f"⚠️  Warning: Template directory {template_dir} does not exist")

    if not Path(output_dir).exists():
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created output directory: {Path(output_dir)}")
