from llm.bot import GPTBot
from .utils import extract_json_content
import os

def build_success_check(dockerfile_path, message):
    with open(os.path.join(dockerfile_path,'Dockerfile'), "r") as f:
        dockerfile = f.read()
    if len(message) >= 100:
        message = message[-100:]
    message = "".join([item['stream'] for item in message if 'stream' in item])
    
    system_prompt = f"""
        Please verify if the Dockerfile successfully builds the project by examining both the Dockerfile and its output execution messages to confirm the success of the build.  If the build is not successful, provide the reason and advice on how to modify it.
        Inputs:
        - Dockerfile content: {dockerfile}
        - Output message: {message}

        Outputs:
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
    response = bot.inference()
    flag, message = eval(extract_json_content(response))
    return flag, message
