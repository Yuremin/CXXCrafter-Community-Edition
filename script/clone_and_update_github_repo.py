import os,sys,re
from git import Repo
import multiprocessing as mp



def clone_repo(repo_link, target_dir):
    """
    
    """
    repo_link = repo_link.strip()
    assert repo_link ,"Repo link should not be empty"
    pattern = r'https:\/\/github\.com\/([a-zA-Z0-9_\-]+)\/([a-zA-Z0-9_\-\.]+)'
    try:
        repo_owner, repo_name = re.findall(pattern, repo_link)[0]
        target_path = os.path.join(target_dir, repo_name)
    except Exception as e:
        with open("NotFound", "a") as f:
            f.write(repo_link+'\n')
        return

    if not os.path.exists(target_path):
        print(repo_name+'  clone')
        #link = link.replace('github', 'gitcode')
        try:
            repo = Repo.clone_from(repo_link, target_path)
            repo.git.submodule('update', '--init', '--recursive')
        except Exception as e:
            print(e)
            with open('script/gitcloneerror.txt', 'a') as f:
                f.write(repo_link+'\n')
    else:
        try:
            print(repo_name+'  update')
            repo = Repo(target_path)
            repo.git.submodule('update', '--init', '--recursive')
        except Exception as e:
            print(e)
            with open('script/gitcloneerror.txt', 'a') as f:
                f.write(repo_link+'\n')







def main():
    repolink_filepath = "data/awesome/repo_link.txt"
    target_dir = "data/awesome"
    with open(repolink_filepath, "r") as f:
        lines = f.readlines()
    pool = mp.Pool(processes=10)
    pool.map(clone_repo,lines)
           

main()
