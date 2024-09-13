import os
import multiprocessing as mp
from cxxcrafter import cxxcrafter, cxxcrafter_continue


def run_with_one(file_path):
    with open(file_path, "r") as f:
        lines =f.readlines()
    lines = lines[50:]
    repos = [line.strip() for line in lines if line.strip()]
    for repo in repos[3:4]:
        cxxcrafter(repo)

def run_with_file_list(repos):
    built_repos = os.listdir('build_solution_base/oss100')
    repos = [item for item in repos if os.path.basename(item) not in built_repos]
    #pool = mp.Pool(processes=10)
    #pool.map(cxxcrafter, repos)   
    for repo in repos:
        cxxcrafter(repo)

if __name__ == "__main__":
    #cxxcrafter('data/top100/cquery')
    #cxxcrafter_continue('dockerfile_playground/rpcs3/history-20240726_1447')
    #run_with_one('file_list.txt')
    file_list = [os.path.join('data/oss100',f) for f in os.listdir('data/oss100') if f != '.DS_Store' and f != 'repo_link.txt']
    run_with_file_list(file_list)
