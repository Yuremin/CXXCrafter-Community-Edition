import os

# === Config ===
CONFIG_LLM_MODEL = ""
CONFIG_API_KEY = ""
CONFIG_BASE_URL = ""

MP_POOL_SIZE = 10







# === Automaic Check ===

LLM_MODEL = CONFIG_LLM_MODEL

if not LLM_MODEL:
    raise ValueError("LLM_MODEL is not configured. Please specify it in src/cxxcrafter/config.py")

if "gpt" in LLM_MODEL.lower():
    LLM_API_KEY = CONFIG_API_KEY or os.getenv("OPENAI_API_KEY")
    LLM_BASE_URL = CONFIG_BASE_URL or os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

elif "deepseek" in LLM_MODEL.lower():
    LLM_API_KEY = CONFIG_API_KEY or os.getenv("DEEPSEEK_API_KEY")
    LLM_BASE_URL = CONFIG_BASE_URL or os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
elif "qwen" in LLM_MODEL.lower():
    LLM_API_KEY = CONFIG_API_KEY or os.getenv("DASHSCOPE_API_KEY")
    LLM_BASE_URL = CONFIG_BASE_URL or os.getenv("DASHSCOPE_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")

else:
    raise ValueError(f"Unknown model type for '{LLM_MODEL}'. CXXCrafter only supports OpenAI, Deepseek or Qwen model series so far.")

if not LLM_API_KEY:
    raise ValueError(f"API key for '{LLM_MODEL}' is not configured. Please check src/cxxcrafter/config.py or environment variables.")

if not LLM_BASE_URL:
    raise ValueError(f"Base URL for '{LLM_MODEL}' is not configured. Please check src/cxxcrafter/config.py or environment variables.")
