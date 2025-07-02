from .docker_manager import build_docker_image_by_api
from .discriminator import build_success_check, build_success_check_2, build_success_check_reflection



def executor(dockerfile_path, build_system_name):
    flag_success, message = build_docker_image_by_api(dockerfile_path)
    if flag_success == True:
        flag_success, message = build_success_check_2(dockerfile_path, message, build_system_name)
        if flag_success == True:
            flag_success, message = build_success_check_reflection(dockerfile_path, message, build_system_name)
    return flag_success, message




