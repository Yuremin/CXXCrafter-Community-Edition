import docker
import subprocess
import logging



def build_docker_image(project_dir):
    result = subprocess.run(["docker", "build", project_dir], capture_output=False, text=True)
    if result.returncode != 0:
        return False
    return True



def build_docker_image_by_api(project_dir):

    logger = logging.getLogger(__name__)
    logger.disabled = False
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    flag_success = True
    try:
        response = client.build(path=project_dir, decode=True)
        chunk_history = []
        unexpected_chunk = []
        for chunk in response:
            if 'stream' in chunk:
                if chunk['stream'] == '\n': continue
                logger.info(chunk['stream'])
            else:
                unexpected_chunk.append(chunk)
            chunk_history.append(chunk)
        
        if 'errorDetail' in chunk_history[-1]:
            flag_success = False
            error = chunk['errorDetail']['message']
            if len(chunk_history) >=5:
                return flag_success, "".join([chunk_item['stream'] for chunk_item in chunk_history[-5:-1]])+error
            else:
                return flag_success, "".join([chunk_item['stream'] for chunk_item in chunk_history[:-1]])+error
        if 'message' in chunk:
            if 'dockerfile parse error' in chunk['message']:
                flag_success = False
                return flag_success, chunk['message']
        
        return flag_success, chunk_history
    except Exception as e:
        flag_success = False
        message = str(e)
        return flag_success, message