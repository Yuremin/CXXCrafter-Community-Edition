import os,re
from cxxcrafter.llm.bot import GPTBot
import logging

def extract_json_content(text):

    pattern = r"```json(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        return match.group(1).strip().replace('\n','')
    else:
        return "No json content found"


def remove_prefix(path, prefix):
    if path.startswith(prefix):
        return path[len(prefix):]
    return path



def llm_help_choose_build_system(build_system_dict, project_name):
    system_prompt = f"""
        I am working on the project '{project_name}', which can be built using one of the identified build systems listed below. Each build system includes an associated entry file:
        {build_system_dict}
        Please select the most appropriate build system and its corresponding entry file that is most likely to successfully build the entire project. The output should be formatted as a tuple like ```json ('{{build_system_name}}', '{{entry_file_path}}')```.
        Do not include any additional output.
        """
    bot = GPTBot(system_prompt)
    response = bot.inference()
    build_system = eval(extract_json_content(response))
    return build_system


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
        'Make': [],
        'CMake': [],
        'Autotools': [],
        'Bazel': [],
        'Ninja': [],
        'MSBuild': [],
        'Meson': [],
        'Bazel': [],
        'Xmake': [],
        'Build2': [],
        'Python': [],
        'Vcpkg': [],
        'Shell': [],
        'Scons': [],
        'Premake5': []
    }
    for root, dirs, files in os.walk(project_dir):
        for build_system, build_file in BUILD_FILES.items():
            if isinstance(build_file, list):
                for bf in build_file:
                    if bf in files:
                        build_system_info[build_system].append(os.path.join(root, bf))
            else:
                if build_file in files:
                    build_system_info[build_system].append(os.path.join(root, build_file))
    
    not_empty_build_system_info = {k: v for k, v in build_system_info.items() if v}


    for k,v in not_empty_build_system_info.items():
        relative_path = [remove_prefix(v_item, project_dir+'/') for v_item in v]
        sorted_v = sorted(relative_path, key=lambda path: path.count('/'))
        not_empty_build_system_info[k] = sorted_v[0]

    return not_empty_build_system_info

def order_build_system(project_dir):
    logger = logging.getLogger(__name__)
    
    build_system_info = extract_build_system(project_dir)
    sorted_build_system_info =dict(sorted(build_system_info.items(), key=lambda item: item[1].count('/')))

    if sorted_build_system_info:
        no_1_build_system = next(iter(sorted_build_system_info.items()))
        if  no_1_build_system[1].count('/') == 0:
            return no_1_build_system
            
        else:
            llm_choose_build_system = llm_help_choose_build_system(sorted_build_system_info, os.path.basename(project_dir))
            return llm_choose_build_system
    else:
        logger.error(f'There are no build system detected in {project_dir}.')
        return (None, None)