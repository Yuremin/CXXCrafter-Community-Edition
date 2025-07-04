import os
import logging
from datetime import datetime
from cxxcrafter.log_utils import setup_logging, log_the_dockerfile, log_the_error_message
from cxxcrafter.generation_module import DockerfileGenerator, DockerfileModifier
from cxxcrafter.utils import save_successful_dockerfile
from cxxcrafter.parsing_module import parser
from cxxcrafter.execution_module import executor
from cxxcrafter.init import get_log_dir, get_playground_dir, get_solution_base_dir
from cxxcrafter.llm.bot import get_sdk_token_counts



class CXXCrafter:
    def __init__(self, project_path):
        self.project_path = project_path
        self.start_time = datetime.now().strftime('%Y%m%d_%H%M')
        self.project_name = os.path.basename(project_path)
        self.dockerfile_path = os.path.join(get_playground_dir(), self.project_name, 'Dockerfile')
        self.log_file = f"{get_log_dir()}/{self.project_name}_{self.start_time}.log"
        self.history_dir = None
        self.flag_version = 1
        self.modifier = DockerfileModifier()

        setup_logging(self.log_file, self.project_name)
        self.logger = logging.getLogger(__name__)
        self.logger.disabled = False

    def __del__(self):
        self.logger.info(f"Building process of project <{self.project_name}> ended.\n"
                         f"Overall input tokens count: {get_sdk_token_counts()[0]}.\n"
                         f"Overall output tokens count: {get_sdk_token_counts()[1]}.")


    def parse_project(self):
        self.logger.info('Parsing Module Starts')
        (self.project_name, 
        self.project_path, 
        self.environment_requirement,
         self.build_system_name,
         self.entry_file,
        self.potential_dependency, 
        self.docs) = parser(self.project_path)
        self.logger.info('Parsing Module Finishes')

    def generate_dockerfile(self):
        self.logger.info('Generation Module Starts')
        dockerfile_generator = DockerfileGenerator(
            self.project_name, self.project_path, 
            self.environment_requirement, self.potential_dependency, 
            self.docs)
        
        dockerfile_generator.generate_dockerfile()
        self.logger.info('Generation Module Finishes')

        # Create a directory to store the history
        self.history_dir = os.path.join(os.path.dirname(self.dockerfile_path), f'history-{self.start_time}')
        os.makedirs(self.history_dir)
        log_the_dockerfile(self.dockerfile_path, self.flag_version, self.history_dir)
    
    
    def modify_dockerfile(self, error_message):
        self.logger.info('Modifier Module Starts')
        self.modifier.modify_dockerfile(self.dockerfile_path, error_message)
        self.logger.info('Modifier Module Finishes')

        self.flag_version += 1
        log_the_dockerfile(self.dockerfile_path, self.flag_version, self.history_dir)


    def execute_dockerfile(self):
        self.logger.info('Execution Module Starts')
        flag, error = executor(os.path.dirname(self.dockerfile_path), build_system_name=self.build_system_name)
        self.logger.info('Execution Module Finishes')
        return flag, error


    
    def run(self):
        self.parse_project()
        self.generate_dockerfile()
        while True:
            flag_success, error_message = self.execute_dockerfile()
            if not flag_success:
                self.logger.error(f"Execution failed with error: {error_message}")
                log_the_error_message(error_message, self.flag_version, self.history_dir)
                if self.flag_version >= 10:
                    self.logger.info("\nTry over 10 times")
                    return self.project_name, flag_success
                self.modify_dockerfile(error_message)
            else:
                save_successful_dockerfile(self.dockerfile_path, self.project_name, get_solution_base_dir())
                self.logger.info(f"{self.project_name} is good!")
                return self.project_name, flag_success
    