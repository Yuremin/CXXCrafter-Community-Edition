import os, re
from parsing_module.utils.build_system_parser import order_build_system
import platform
import psutil
import GPUtil


def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }

    cpu_info = {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
    }

    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append({
            "GPU ID": gpu.id,
            "GPU Name": gpu.name,
            "GPU Load": f"{gpu.load * 100}%",
            "GPU Free Memory": f"{gpu.memoryFree}MB",
            "GPU Used Memory": f"{gpu.memoryUsed}MB",
            "GPU Total Memory": f"{gpu.memoryTotal}MB",
            "GPU Temperature": f"{gpu.temperature}°C",
        })

    return {
        "System Info": system_info,
        "CPU Info": cpu_info,
        "GPU Info": gpu_info,
    }


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

    system_info = get_system_info()

    environment_requirement = f"""
    ==============HARDWARE AND OS INFO=============
    1. Operating system info:
    System: {system_info["System Info"]["System"]}
    Machine: {system_info["System Info"]["Machine"]}
    2. GPU info:
    GPU Name: {system_info["GPU Info"][0]["GPU Name"]}
    GPU Free Memory: {system_info["GPU Info"][0]["GPU Free Memory"]}
    
    ==============BUILD SYSTEM INFO================
    Build system's name is {build_system_name}. And the file of entry file of {build_system_name} is in {entry_file} of the project.
    And build system's version requirement is {build_system_version}
    """

    return environment_requirement, build_system_name, entry_file


if __name__ == "__main__":
    info = get_system_info()
    for category, details in info.items():
        print(f"=== {category} ===")
        if isinstance(details, list):
            for item in details:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print()
        else:
            for key, value in details.items():
                print(f"{key}: {value}")
            print()
    extract_environment_requirement(
        project_dir=r"D:\Jetbrains\PyCharm 2020.1\Pycharm Projects\pythonProject\CXXCrafter\data\aubio"
    )
