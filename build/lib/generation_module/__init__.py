import logging, shutil, os
from .template.prompt_template import get_initial_prompt, prompt_template_for_modification
from .utils import save_dockerfile, resave_dockerfile, extract_dockerfile_content
from llm.bot import GPTBot


class DockerfileGenerator:
    def __init__(self, project_name, project_path, environment_requirement, dependency, docs):
        self.project_name = project_name
        self.project_path = project_path
        self.environment_requirement = environment_requirement
        self.dependency = dependency
        self.docs = docs
        self.logger = logging.getLogger(__name__)
        self.logger.disabled = False
    
    def generate_system_prompt(self):
        self.logger.info('Generating system prompt...')
        return get_initial_prompt(self.project_name, self.project_path, self.environment_requirement, self.dependency, self.docs)

    def perform_inference(self, system_prompt):
        self.logger.info('Performing inference...')
        bot = GPTBot(system_prompt)
        return bot.inference()

    def extract_dockerfile(self, response):
        self.logger.info('Extracting Dockerfile content...')
        return extract_dockerfile_content(response)

    def check_dockerfile(self, dockerfile_content):
        prompt = """
        Please review the Dockerfile to ensure it meets the following requirements. If it doesn't, make the necessary modifications:
        1. Each install command should be executed individually.
        2. Avoid duplicating identical RUN commands.
        3. Follow proper Dockerfile syntax, such as placing comments and commands on separate lines. Comments should begin with a # and be on their own line.
        """
        bot = GPTBot(prompt)
        dockerfile_content = self.extract_dockerfile(bot.inference(dockerfile_content))
        return dockerfile_content
    
    def generate_dockerfile(self):
        self.logger.info('Starting Dockerfile generation process...')
        system_prompt = self.generate_system_prompt()
        response = self.perform_inference(system_prompt)
        dockerfile_content = self.extract_dockerfile(response)
        dockerfile_content = self.check_dockerfile(dockerfile_content)

        # Create dockerfile playground directory
        project_dir = f"dockerfile_playground/{self.project_name}"

        save_dockerfile(project_dir, dockerfile_content)
        self.logger.info('Starting Copying the Repo to Dockerfile_Playground')
        temp = os.path.join(project_dir, self.project_name)
        if not os.path.exists(temp): shutil.copytree(self.project_path, temp)
        self.logger.info('Finish Copying')
        self.logger.info('Finish generating the initial dockerfile')
    

class DockerfileModifier:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Begin to modify the dockerfile')
        self.bot = GPTBot(prompt_template_for_modification)

    def generate_prompt(self, dockerfile_path, error_message):
        dockerfile_content = open(dockerfile_path, "r").read()
        return dockerfile_content

    
    def modify_dockerfile(self, dockerfile_path, error_message):
        """
        """
        dockerfile_content = self.generate_prompt(dockerfile_path, error_message)
        response = self.bot.inference(dockerfile_content +"\n*2" +error_message)
        if '```dockerfile' in response.lower():
            dockerfile_content = extract_dockerfile_content(response)
            resave_dockerfile(dockerfile_path, dockerfile_content)
        
    