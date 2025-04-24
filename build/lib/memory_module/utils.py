import os
import re



def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def remove_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


def pair_issues_and_solutions(directory):
    dockerfiles = {}
    error_messages = {}

    for filename in os.listdir(directory):
        if filename.startswith("Dockerfile"):
            version = filename.split('-')[-1]
            dockerfiles[version] = read_file(os.path.join(directory, filename))
        elif filename.startswith("error_message"):
            version = filename.split('-')[-1]
            error_messages[version] = read_file(os.path.join(directory, filename))

    paired_data = []
    for version in dockerfiles:
        if version in error_messages:
            paired_data.append({
                "version": version,
                "error_message": error_messages[version],
                "dockerfile": dockerfiles[version]
            })
    
    return paired_data
    
def extract_json_content(text):

    pattern = r"```json(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        return match.group(1).strip().replace('\n','')
    else:
        return "No json content found"