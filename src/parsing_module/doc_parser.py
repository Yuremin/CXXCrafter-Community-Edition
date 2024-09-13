import os,re,sys
from qdrant_client import QdrantClient
from llm.bot import GPTBot
from .utils.build_system_parser import extract_json_content


def scan_project_files(directory):
    docs = []
    metadata = []
    ids = []
    id_counter = 1  # Initialize ID counter

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not file_path.endswith('.txt') or 'cmake' in file_path.lower():
                continue
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    docs.append(content)
                    metadata.append({"file_path": file_path})
                    ids.append(id_counter)
                    id_counter += 1
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

    return docs, metadata, ids



def similarity_based_match(project_directory):

    client = QdrantClient(":memory:")  # or QdrantClient(path="path/to/db")
    docs, metadata, ids = scan_project_files(project_directory)

    # Use the new add method
    client.add(
        collection_name="project_files",
        documents=docs,
        metadata=metadata,
        ids=ids
    )

    # Example query
    search_result = client.query(
        collection_name="project_files",
        query_text="Document related to install or building"
    )
    print(search_result)

    return 

def get_helpful_content(files, bot):
    prompt = f"""
    Please provide a summary of the key advice for building the project from the source code based on the content of the files. Include recommendations on which version of Ubuntu to use, necessary dependencies to install, availability of existing setup scripts, and the use of automation scripts. Exclude any Docker-related suggestions.
    """
    if not files:
        return ''
    content = ''
    for file in files[:3]:
        with open(file, 'r') as f:
            content += file+'\n'+f.read()+'\n----------------\n'
    
    response = bot.inference(prompt+'\n'+content)
    return response

    


def llm_help_choose_helpful_doc(doc_files, project_name):
    system_prompt = f"""
        I need to build the project '{project_name}', and the following documents have been identified as potential resources for this task:
        {doc_files}
        Please select the most relevant documents that are most likely to assist in successfully building the project itself. The output should be formatted as a list like ```json ['document_file1', 'document_file2', ...]```.
        Do not include any additional output.
    """
    bot = GPTBot(system_prompt, 'gpt-4o')
    response = bot.inference()
    files = eval(extract_json_content(response))
    content = get_helpful_content(files, bot)
    print(content)
    return content






def match_doc(directory):

    file_patterns = [
        r'^README(\.md|\.txt)?$',  # README文件
        r'^INSTALL(\.md|\.txt\.sh)?$', # INSTALL文件
        r'^requirements\.txt$',    # Python依赖项文件
        r'^\.env$',                # 环境配置文件
        r'^config\.yaml$',         # 配置文件
        r'^install\.sh$',          # 安装脚本
        r'^setup\.py$',            # Python安装脚本
        r'^docs/installation\.md$', # 文档中的安装文件
        r'^docs/setup\.md$',       # 文档中的设置文件
    ]

    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            for pattern in file_patterns:
                if re.match(pattern, file, re.IGNORECASE):
                    matched_files.append(os.path.join(root, file))
    
    matched_files = llm_help_choose_helpful_doc(matched_files, os.path.basename(directory))
    return matched_files




    
    