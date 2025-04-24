import os
import multiprocessing as mp
from cxxcrafter import CXXCrafter
#from llm.bot import global_input_token_count, global_output_token_count




# def get_global_token_counts():
#     return {
#         "global_input_tokens": global_input_token_count,
#         "global_output_tokens": global_output_token_count
#     }

def run_with_file_list(file_path):
    with open(file_path, "r") as f:
        lines =f.readlines()
    lines = lines
    repos = [line.strip() for line in lines if line.strip()]
    built_repos = os.listdir('build_solution_base')
    repos = [item for item in repos if os.path.basename(item) not in built_repos]
    pool = mp.Pool(processes=10)
    pool.map(build_one_repo, reversed(repos))



def build_one_repo(repo_path):
    cxxcrafter = CXXCrafter(repo_path)
    project_name, flag = cxxcrafter.run()
    #input_token_num, output_token_num = get_global_token_counts()
    #print(input_token_num)
    #print(output_token_num)

if __name__ == "__main__":
    #run_with_file_list('data/top100/filelist')
    # repo_path = "data/top100/simdjson"
    repo_path = "data/raylib"
    build_one_repo(repo_path)
