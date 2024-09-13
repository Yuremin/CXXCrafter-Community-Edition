import os
import shutil

def remove_files_from_oss():
    oss_repo_link_path = "data/oss100/repo_link.txt"
    with open(oss_repo_link_path, "r") as f:
        lines = f.readlines()
    repo_list = []
    for line in lines:
        repo_list.append(line.split("/")[-1].strip())
    
    for file in os.listdir("build_solution_base/oss100"):
        if file == 'repo_link.txt' or file == 'oss100' or file =='top100': continue
        if file not in repo_list:
            file_path = os.path.join('build_solution_base/oss100', file)
            print(file)
            shutil.rmtree(file_path)




if __name__=='__main__':
    remove_files_from_oss()

