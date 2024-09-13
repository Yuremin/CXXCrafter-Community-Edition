def get_repo_from_oss_fuzz():
    """
    Extract repo from oss-fuzz project
    """
    projects = os.listdir('oss-fuzz/projects')
    projects_link = []
    for project in projects:
        with open(os.path.join('oss-fuzz/projects',project,'project.yaml'), 'r') as f:
            content = f.read()
            pattern = re.compile(r"main_repo:\s*[\"\']?(https:\/\/github.com\/[a-zA-Z0-9_\-]+\/[a-zA-Z0-9_\-\.\/]+)[\"\']?")
            try:
                main_repo = re.findall(pattern, content)[0]
            except:
                continue
            try:
                pattern = r'language:\s*(.+)'
                language = re.findall(pattern, content)[0]
                if language.strip().lower() == 'c++' or language.strip().lower() == 'c':
                    print(main_repo)
                #print(main_repo, language)
            except:
                #print(main_repo)
                pass
