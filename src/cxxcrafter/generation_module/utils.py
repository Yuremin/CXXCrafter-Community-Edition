import re, os
import logging

def extract_dockerfile_content(text):

    pattern = r"```[dD]ockerfile(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    else:
        raise "No Dockerfile content found"
    


def save_dockerfile(project_dir, dockerfile_content):
    logger = logging.getLogger(__name__)
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
    with open(os.path.join(project_dir, 'Dockerfile'), 'w') as f:
        f.write(dockerfile_content)
    
    logger.info(f"Dockerfile generated successfully in {project_dir}")

def resave_dockerfile(dockerfile_path, dockerfile_content):
    logger = logging.getLogger(__name__)
    with open(dockerfile_path, 'w') as f:
        f.write(dockerfile_content)
        logger.info(f"Dockerfile modified successfully")


    
