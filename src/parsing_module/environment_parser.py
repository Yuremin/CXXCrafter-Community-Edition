import os, re
from .utils.build_system_parser import order_build_system

def extract_cmake_version(project_dir, entry_file):
    cmakelist_path = os.path.join(project_dir, entry_file)
    with open(cmakelist_path, "r") as f:
        content = f.read()
    pattern = r'cmake_minimum_required\s*\(.+\)'
    try:
        cmake_version = re.findall(pattern, content)[0]
    except:
        cmake_version = 'No CMake Version Requirement'
    return cmake_version



def extract_environment_requirement(project_dir):
    build_system = order_build_system(project_dir)
    build_system_name = build_system[0]
    entry_file = build_system[1]
    if 'CMake' == build_system[0]:
        build_system_name = 'CMake'
        build_system_version = extract_cmake_version(project_dir, entry_file)
    else:
        build_system_version = 'None'

    environment_requirement = f"""
    Build system's name is {build_system_name}. And the file of entry file of {build_system_name} is in {entry_file} of the project.
    And build system's version requirement is {build_system_version}
    """

    return environment_requirement

