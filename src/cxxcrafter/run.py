import os
import multiprocessing as mp
import argparse

from cxxcrafter import CXXCrafter
try:
    from config import MP_POOL_SIZE
except Exception as e:
    MP_POOL_SIZE = 10


def run_with_file_list(file_path):
    with open(file_path, "r") as f:
        lines =f.readlines()
    lines = lines
    repos = [line.strip() for line in lines if line.strip()]
    built_repos = os.listdir('build_solution_base')
    repos = [item for item in repos if os.path.basename(item) not in built_repos]
    pool = mp.Pool(processes=(MP_POOL_SIZE if isinstance(MP_POOL_SIZE, int) else 10))
    pool.map(build_one_repo, reversed(repos))


def build_one_repo(repo_path):
    cxxcrafter = CXXCrafter(repo_path)
    project_name, flag = cxxcrafter.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CXXCrafter-Community Runner")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--repo', type=str, help='Specify the path of a single repo to build.')
    group.add_argument('--repo-list', type=str, help='Specify the path of a repo list file.')
    args = parser.parse_args()

    if args.repo:
        build_one_repo(args.repo)
    elif args.repo_list:
        run_with_file_list(args.repo_list)



