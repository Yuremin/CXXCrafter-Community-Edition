import json,tqdm



def transform_to_json(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
    new_lines = []
    for line in tqdm.tqdm(lines):
        new_lines.append(json.loads(line))
    unique_repos = list({json.dumps(d): d for d in new_lines}.values())
    with open('script/repos.json', 'w') as f:
        json.dump(unique_repos, f)






def main():
    #file_path = 'script/repositories.json'
    #transform_to_json(file_path) #Use oncy for the non-standard json file
    file_path = 'script/repos.json'
    with open(file_path, 'r') as f:
        repos = json.load(f)
    sorted_repos = sorted(repos, key=lambda item: item['stargazers_count'], reverse=True)
    repo_link = []
    for repo in sorted_repos:
        repo_link.append(repo['url'])
    with open("repo_full_name", 'w') as f:
        f.write(str(repo_link))


main()
