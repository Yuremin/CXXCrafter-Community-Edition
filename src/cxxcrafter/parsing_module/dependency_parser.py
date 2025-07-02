import sys
from cxxcrafter.tools.ccscanner.ccscanner.scanner import scanner



def extract_dependencies(project_dir):
    scanner_result = scanner(project_dir).extractors
    dependency_dict = {}
    for item in scanner_result:
        for dependency in item['deps']:
            if dependency['confidence'] == 'High':
                dependency_dict[dependency['depname']] = dependency['version']
    return dependency_dict

def verify_dependencies(dependency_dict):
    new_dependency_dit = {}
    for item in dependency_dict:
        print(item[0], item[1])
    pass



if __name__=='__main__':
    dependency_dict = extract_dependencies('dockerfile_playground/top100/rpcs3')
    x = verify_dependencies(dependency_dict)
