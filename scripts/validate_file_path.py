import os


def validate_file_path(data_file_path: str) -> None:
    if not isinstance(data_file_path, str) or not data_file_path.strip():
        raise ValueError("Data file path must be a non-empty string")

    if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"Data file {data_file_path} not found")
