import os
build_system_count = {
    'Make': 0,
    'CMake': 0,
    'Autotools': 0,
    'Bazel': 0,
    'Ninja': 0,
    'MSBuild': 0,
    'Meson': 0,
    'Bazel': 0,
    'Xmake': 0,
    'Build2': 0,
    'Python': 0,
    'Vcpkg': 0,
    'Shell': 0,
    'Scons': 0,
    'Premake5': 0
}

def read_file_items(file_path):
    try:
        with open(file_path, 'r') as file:
            # 读取文件中的每一行，并去除换行符
            to_build_projects = [line.strip() for line in file]
        return to_build_projects
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
        return []

def subdir_extractor(folder):
    subdir = []
    project = os.listdir(folder)
    for item in project:
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path):
            subdir.append(item_path)
    return subdir

def extract_build_system(project_dir):
    BUILD_FILES = {
        'Make': ['Makefile', 'GNUmakefile', 'makefile'],
        'CMake': 'CMakeLists.txt',
        'Autotools': ['configure', 'configure.in', 'configure.ac', 'Makefile.am'],
        'Ninja': 'build.ninja',
        'Meson': 'meson.build',
        'Bazel': ['BUILD', 'BUILD.bazel'],
        'Xmake': 'xmake.lua',
        'Build2': 'manifest',
        'Python': 'setup.py',
        'Vcpkg': 'vcpkg.json',
        'Shell': 'build.sh',
        'Scons': ['SConstruct', 'SConscript'],
        'Premake5': 'premake5.lua'
        
    }

    build_system_info = {
        'Make': 0,
        'CMake': 0,
        'Autotools': 0,
        'Bazel': 0,
        'Ninja': 0,
        'MSBuild': 0,
        'Meson': 0,
        'Bazel': 0,
        'Xmake': 0,
        'Build2': 0,
        'Python': 0,
        'Vcpkg': 0,
        'Shell': 0,
        'Scons': 0,
        'Premake5': 0
    }
    for root, dirs, files in os.walk(project_dir):
        for build_system, build_file in BUILD_FILES.items():
            if isinstance(build_file, list):
                for bf in build_file:
                    if bf in files:
                        if build_system_info[build_system] == 0:
                            build_system_count[build_system] += 1
                        build_system_info[build_system] = 1

            else:
                if build_file in files:
                    if build_system_info[build_system] == 0:
                        build_system_count[build_system] += 1
                    build_system_info[build_system] += 1
    
    not_empty_build_system_info = {k: v for k, v in build_system_info.items() if v}


    # for k,v in not_empty_build_system_info.items():
    #     relative_path = [remove_prefix(v_item, project_dir+'/') for v_item in v]
    #     sorted_v = sorted(relative_path, key=lambda path: path.count('/'))
    #     not_empty_build_system_info[k] = sorted_v[0]

    return not_empty_build_system_info

def main():
    projects_collection_path_1 = 'data/awesome'
    subdir = [os.path.join('data/awesome', i) for i in os.listdir(projects_collection_path_1)]

    with open('script/count_for_build_system.txt', 'a') as f:
        for project_path in subdir:
            project = os.path.basename(project_path)
            build_system_info = extract_build_system(project_path)
            if not build_system_info:
                f.write("{} have no build system\n".format(project))
            else:
                f.write("{} build with:".format(project))
                for key in build_system_info.keys():
                    f.write("{} ".format(key))
                f.write("\n")

        f.write("\n")
        f.write("count_results:\n")
        for k,v in build_system_count.items():
            f.write("{} : {}\n".format(k,v))

    


main()