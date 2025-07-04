from .utils import pair_issues_and_solutions, remove_ansi_escape_sequences, extract_json_content
from llm.bot import GPTBot



def llm_help_summary_error_message(QA):
    system_prompt = f"""
        The following content includes error messages and modifications to a Dockerfile aimed at resolving those errors. Some modifications are effective, while others are not.
        Please summarize the key issues that were successfully resolved during this process.
        {QA}
    """

    bot = GPTBot(system_prompt)
    response = bot.inference()

    #content = eval(extract_json_content(response))
    print(response)


def extract_info(successful_path):
    """
    
    """
    issue_solutions = pair_issues_and_solutions(successful_path)
    issue_solutions.sort(key=lambda x: int(x['version'][1:]))
    llm_help_summary_error_message(issue_solutions)
    """
    for item in issue_solutions:
        print(item['error_message'])
        #print(item['dockerfile'])
    """






if __name__ == '__main__':
    extract_info('dockerfile_playground/mesa3d/history-20240826_1414')
    
