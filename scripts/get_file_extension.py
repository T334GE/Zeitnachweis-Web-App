import os


SUPPORTED_EXTENSIONS = {".json"}


def get_file_extension(data_file_path: str) -> str:
    file_ext = os.path.splitext(data_file_path)[1].lower()

    if file_ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file format: {file_ext}. Please use .json files."
        )

    return file_ext
