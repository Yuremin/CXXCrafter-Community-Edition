import os

def _ensure_dir(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path


def get_base_dir() -> str:
    return _ensure_dir(os.path.expanduser("~/.cxxcrafter"))


def get_log_dir() -> str:
    return _ensure_dir(os.path.join(get_base_dir(), "logs"))


def get_playground_dir() -> str:
    return _ensure_dir(os.path.join(get_base_dir(), "dockerfile_playground"))


def ensure_all_directories_exist():
    get_log_dir()
    get_playground_dir()