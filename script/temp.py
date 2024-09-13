import os
import shutil
original_path = 'dockerfile_playground'

target_path = 'dockerfile_playground_copy'

repos = os.listdir(original_path)
for repo in repos:
    repo_path = os.path.join(original_path, repo)
    os.mkdir(os.path.join(target_path, repo))
    for file in os.listdir(repo_path):
        if file != repo:
            if 'history' in file:
                shutil.copytree(os.path.join(repo_path,file), os.path.join(target_path, repo, file))
            if file == 'Dockerfile':
                shutil.copy(os.path.join(repo_path,file), os.path.join(target_path, repo, file))