import os
from cxxcrafter import CXXCrafter
from execution_module.docker_manager import build_docker_image_by_api
from execution_module import executor
from log_utils import setup_logging

def debug_one_project(repo_path):
    cxxcrafter = CXXCrafter(repo_path)
    project_name, flag = cxxcrafter.run()
    #cxxcrafter.debug()


def debug_execution(dockerfile_path):
    a, b = executor(dockerfile_path)
    #a, b = build_docker_image_by_api(dockerfile_path)
    print(a)
    print(b)

if __name__ == "__main__":
    repo_path = 'data/top100/DearPyGui'
    debug_one_project(repo_path)
    #dockerfile_path = 'dockerfile_playground/soloud'
    #debug_execution(dockerfile_path)