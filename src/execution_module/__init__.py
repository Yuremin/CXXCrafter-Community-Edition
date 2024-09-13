from .docker_manager import build_docker_image_by_api
from .discriminator import build_success_check



def executor(dockerfile_path):
    flag_sucecess, message = build_docker_image_by_api(dockerfile_path)
    if flag_sucecess == True:
        flag_success_llm,message = build_success_check(dockerfile_path, message)
        flag_sucecess = flag_success_llm
    return flag_sucecess, message




