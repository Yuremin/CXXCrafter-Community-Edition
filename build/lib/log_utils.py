import os
import logging
import logging.config

def setup_logging(log_file, project_name):
    logging_config = {
        'version': 1,
        #'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': f'%(asctime)s - %(name)s -{project_name} - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': log_file,
                'formatter': 'default',
                'level': 'DEBUG'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG'
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],
        },
    }

    logging.config.dictConfig(logging_config)

def log_the_dockerfile(dockerfile_path, version, history_dir):

    dockerfile_version_name = os.path.basename(dockerfile_path)+ '-v' + str(version)
    dockerfile_version_path = os.path.join(history_dir, dockerfile_version_name)
    with open(dockerfile_path, 'r') as f:
        content = f.read()
    with open(dockerfile_version_path, 'w') as f:
        f.write(content)
        
def log_the_error_message(error_message, version, history_dir):
    error_message_version_name = "error_message"+ '-v' + str(version)
    error_message_version_path = os.path.join(history_dir, error_message_version_name)
    with open(error_message_version_path, 'w') as f:
        f.write(error_message)