import openai
import tiktoken
import os

key_openai = os.getenv("OPENAI_API_KEY")
base_url_openai = os.getenv("OPENAI_BASE_URL", None)

global_input_token_count = 0
global_output_token_count = 0

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
    def __init__(self, system_prompt=None, model='gpt-4o'):
        self.messages = [{"role": "system", "content": system_prompt}]
        if base_url_openai:
            self.client = openai.OpenAI(api_key=key_openai, base_url=base_url_openai)
        else:
            self.client = openai.OpenAI(api_key=key_openai)
        self.model = model
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
        self.messages.append({"role": "assistant", "content":content})
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
        self.messages.append({"role": "assistant", "content":content})
        return content

    def calculate_message_length(self, message):
        enc = tiktoken.encoding_for_model(self.model)
        return len(enc.encode(message))
    
    def calculate_total_length(self, messages):
        enc = tiktoken.encoding_for_model(self.model)
        total_length = 0
        for message in messages:
            total_length += len(enc.encode(message['content']))
        return total_length



class TongyiBot:
    def __init__(self, system_prompt=None, model='qwen-turbo'):
        self.messages = [{"role": "system", "content":system_prompt}]
        self.client = openai.OpenAI(api_key=key_tongyi, base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
        self.model = model
    def inference(self, message):
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        content = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content":content})

        return content

class DeepSeekBot:
    def __init__(self, system_prompt=None, model='deepseek-chat'):
        self.messages = [{"role": "system", "content":system_prompt}]
        self.client = openai.OpenAI(api_key=key_deepseek, base_url="https://api.deepseek.com/v1")
        self.model = model
    def inference(self, message):
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        content = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content":content})

        return content

class GLMBot:
    def __init__(self, system_prompt=None, model='glm-4'):
        self.messages = [{"role": "system", "content":system_prompt}]
        self.client = openai.OpenAI(api_key=key_glm, base_url="https://open.bigmodel.cn/api/paas/v4/")
        self.model = model
    def inference(self, message):
        self.messages.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        content = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content":content})

        return content
