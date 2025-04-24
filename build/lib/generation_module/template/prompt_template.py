from .dockerfile_template import dockerfile_template





def get_initial_prompt(project_name, user_intention, environment_requirement, dependency, docs):
    """
    Get the initial prompt.
    """
    if len(dependency) > 10:
        potential_dependency = {k: dependency[k] for k in list(dependency)[:10]}
    else:
        potential_dependency = dependency

    prompt_template = f"""
        Please generate dockerfile which build the project {project_name} from source code accordind to the dockerfile template {dockerfile_template}.
        The source code is located at {"./"+project_name}. Move it to the docker container temp directory and build.
        Requirements:
            1. Install commands must be executed one at a time.
            2. Avoid repeating identical RUN commands.
            3. Please adhere to Dockerfile syntax. For example, ensure that comments and commands are on separate lines. Comments should start with a # and be placed independently of commands.
        {user_intention}
        Some useful information:
            Environment requirement: {environment_requirement}
            Docs: {docs}
            Potential Dependencies (skip installation if useless): {potential_dependency}
    """
    return prompt_template




prompt_template_for_modification = """
    Solve the problem according to the error message and modify the dockerfile.
    The dockerfile is:\n{last_dockerfile_content}\n
    The error message is:\n{feedback_message}\n
    
    Additionally, take note of the following items:
    1. If the error message indicates a network issue, do not make any modifications to the Dockerfile. 
    2. Please return a complete dockerfile rather than just providing advice.
    3. Try to keep the beginning of the Dockerfile unchanged and make minimal modifications towards the end of the file.
    4. In the dockerfile, commands must be executed one at a time.
    5. If some unnecessary modules, such as the testing module, are causing issues, they should be disabled through build options.
    6. If required packages, tools, or dependencies are missing, proceed with installing them rather than just verifying their presence.
    7. In case errors arise due to specific dependency versions, attempt to acquire and install the exact version of the software that is required.
    8. If a 404 error occurs while attempting to download a specific dependency version, verify the correctness of the download link and make any necessary corrections.
    """