import openai
import tiktoken

try:
    from cxxcrafter.config import LLM_MODEL, LLM_API_KEY, LLM_BASE_URL
except Exception as e:
    raise e

global_input_token_count = 0
global_output_token_count = 0

sdk_global_input_token_count = 0
sdk_global_output_token_count = 0


def get_sdk_token_counts():
    global sdk_global_input_token_count, sdk_global_output_token_count
    return sdk_global_input_token_count, sdk_global_output_token_count


def token_count_decorator(func):
    def wrapper(self, *args, **kwargs):
        global global_input_token_count, global_output_token_count

        message = kwargs.get('message', args[0] if args else '')

        # 统计输入token数量
        input_tokens = self.calculate_message_length(message)
        global_input_token_count += input_tokens
        self.input_token_count += input_tokens

        # 调用被装饰的函数并获取返回值
        result = func(self, *args, **kwargs)

        # 统计输出token数量
        output_tokens = self.calculate_message_length(result)
        global_output_token_count += output_tokens
        self.output_token_count += output_tokens

        return result

    return wrapper


class GPTBot:
    def __init__(self, system_prompt=None):
        self.messages = [{"role": "system", "content": system_prompt}]
        if LLM_BASE_URL:
            self.client = openai.OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)
        else:
            self.client = openai.OpenAI(api_key=LLM_API_KEY)
        self.model = LLM_MODEL
        self.input_token_count = 0
        self.output_token_count = 0

    @token_count_decorator
    def inference(self, message=''):
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        content = response.choices[0].message.content
        global sdk_global_input_token_count
        sdk_global_input_token_count += response.usage.prompt_tokens
        global sdk_global_output_token_count
        sdk_global_output_token_count += response.usage.completion_tokens
        self.messages.append({"role": "assistant", "content": content})
        return content

    @token_count_decorator
    def inference2(self, context=128000, message=''):
        self.messages.append({"role": "user", "content": message})
        total_length = self.calculate_total_length(self.messages)
        while total_length >= context:
            self.messages.pop(1)
            total_length = self.calculate_total_length(self.messages)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        content = response.choices[0].message.content
        global sdk_global_input_token_count
        sdk_global_input_token_count += response.usage.prompt_tokens
        global sdk_global_output_token_count
        sdk_global_output_token_count += response.usage.completion_tokens
        self.messages.append({"role": "assistant", "content": content})
        return content

    def calculate_message_length(self, message):
        # enc = tiktoken.encoding_for_model(self.model)
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(message))

    def calculate_total_length(self, messages):
        # enc = tiktoken.encoding_for_model(self.model)
        enc = tiktoken.get_encoding("cl100k_base")
        total_length = 0
        for message in messages:
            total_length += len(enc.encode(message['content']))
        return total_length