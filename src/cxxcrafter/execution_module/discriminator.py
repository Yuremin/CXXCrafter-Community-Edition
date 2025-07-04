from cxxcrafter.llm.bot import GPTBot
from .utils import extract_json_content, remove_ansi_escape_sequences
import os, logging



def build_success_check_2(dockerfile_path, message, build_system_name):
    logger = logging.getLogger(__name__)
    logger.disabled = False

    logger.info(f"build_success_check executing...")
    with open(os.path.join(dockerfile_path, 'Dockerfile'), "r") as f:
        dockerfile = f.read()
    logger.info(f"THE DOCKERFILE CONTENT IS :\n{dockerfile}\n\nTHE ORIGINAL EXECUTION MESSAGE IS:\n{message}\n")

    if hasattr(message, '__len__'):
        if len(message) >= 200:
            message = message[-200:]
        message = "".join([item['stream'] for item in message if 'stream' in item])
        filtered_lines = [line for line in message.split('\n') if 'Successful' not in line]

        message = '\n'.join(filtered_lines)
        cleaned_message = remove_ansi_escape_sequences(message)

        logger.info(f"THE CLEANED EXECUTION MESSAGE IS:\n{cleaned_message}\n")

        with open(os.path.join(dockerfile_path, 'cleaned_message.txt'), 'w', encoding='utf-8') as file:
            file.write(cleaned_message)
    else:
        cleaned_message = f"build_success_check: When building {dockerfile_path}, Docker didn't return valid execution message."
        logger.error(cleaned_message)

    system_prompt = f"""
            ======Overall Requirements======
            Please verify if the Dockerfile successfully builds the project by examining both the Dockerfile and its output execution messages to confirm the success of the build.  If the build is not successful, provide the reason and advice on how to modify it.
            The build can only be determined to be successful when the following two criteria are simultaneously met:
            1. Static Criterion: The Dockerfile should actually execute build commands of {build_system_name}. 
            2. Dynamic Criterion: The execution message should contain content of build process.
            
            ======Notice======
            Please don’t be overly strict—meeting the requirements reasonably well is sufficient.
            Prioritize successful compilation and build; test outcomes are secondary, and it’s acceptable for some tests to fail.

            =======Inputs:=======
            - Dockerfile content: {dockerfile}
            - Execution message: {cleaned_message}

            ======Outputs:======
            Return a JSON tuple with two elements. The first element is a boolean indicating whether the build was successful. The second element is a string with the reason and advice if the build was not successful (or None if the build was successful).
            The output format should be:
            ```json
            (True, None)
            ```
            or
            ```json
            (False, "<Reason and Advice>")
            ```
            If the build is successful, simply return ```json\n(True, None)\n```.
            If the build is not successful, return ```json\n(False, <Reason and Advice>)\n```.
        """

    bot = GPTBot(system_prompt)
    response = bot.inference2()
    logger.info(f"THE RESPONSE IS:\n{response}\n")

    flag, message = eval(extract_json_content(response))
    return flag, message


def build_success_check_reflection(dockerfile_path, message, build_system_name):
    logger = logging.getLogger(__name__)
    logger.disabled = False

    logger.info(f"build_success_reflection executing...")
    with open(os.path.join(dockerfile_path, 'Dockerfile'), "r") as f:
        dockerfile = f.read()

    if hasattr(message, '__len__'):
        if len(message) >= 200:
            message = message[-200:]
        message = "".join([item['stream'] for item in message if 'stream' in item])
        filtered_lines = [line for line in message.split('\n') if 'Successful' not in line]

        message = '\n'.join(filtered_lines)
        cleaned_message = remove_ansi_escape_sequences(message)
    else:
        cleaned_message = f"build_success_check: When building {dockerfile_path}, Docker didn't return valid execution message."
        logger.error(cleaned_message)

    system_prompt = f"""
=======Background Knowledge=======
A software engineer is building a project. He has written and executed a Dockerfile, and based on the execution messages of the Dockerfile, he determines whether the project has indeed been successfully built.
His criteria for judgment are as follows, and only when both criteria are met simultaneously does he conclude that the Dockerfile has successfully built the project:
Static Criterion: The Dockerfile must effectively execute the build commands of {build_system_name}.
Dynamic Criterion: The execution message must include content indicative of the build process.
Based on the aforementioned criteria, he has determined that the Dockerfile has successfully built the project.

=======Requirement=======
Please evaluate whether his judgment adheres to the two criteria, taking into account the content of the Dockerfile, the execution messages, and the name of the project build system.``.
Please don’t be overly strict—meeting the requirements reasonably well is sufficient.
Prioritize successful compilation and build; test outcomes are secondary, and it’s acceptable for some tests to fail.

=======Inputs:=======
- Dockerfile content: {dockerfile}
- Execution message: {cleaned_message}
- Build system name: {build_system_name}

=======Outputs=======
Return a JSON tuple with two elements. The first element is a boolean indicating whether the build was successful. The second element is a string with the reason and advice if the build was not successful (or None if the build was successful).
The output format should be:
```json
(True, None)
```
or
```json
(False, "<Reason and Advice>")
```
If the build is successful, simply return ```json\n(True, None)\n```.
If the build is not successful, return ```json\n(False, <Reason and Advice>)\n```.
            """

    bot = GPTBot(system_prompt)
    response = bot.inference2()

    logger.info(f"THE RESPONSE IS:\n{response}\n")

    flag, message = eval(extract_json_content(response))
    return flag, message