import re, os
from shutil import copy

def find_latest_dockerfile(directory):
    files = os.listdir(directory)
    max_number = -1
    latest_file = None

    pattern = re.compile(r'Dockerfile-v(\d+)')

    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            if number > max_number:
                max_number = number
                latest_file = file

    return latest_file

def find_latest_error_message(directory):
    files = os.listdir(directory)
    max_number = -1
    latest_file = None

    pattern = re.compile(r'error_message-v(\d+)')

    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            if number > max_number:
                max_number = number
                latest_file = file

    return latest_file, max_number

def save_successful_dockerfile(dockerfile_path, project_name, solution_dir):
    target_dir = os.path.join(solution_dir, project_name)
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    copy(dockerfile_path, target_dir)