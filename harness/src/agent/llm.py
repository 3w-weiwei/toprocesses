import logging
from dotenv import load_dotenv
from langchain_core.language_models import ModelProfile

# 配置日志
logger = logging.getLogger(__name__)
qwen_api_key = "sk-3af0625d1a754b429a3855372f21db16"
qwen_model = "qwen3.6-plus"
base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"

def create_model():
    """
    创建图片处理模型（火山引擎 / 豆包视觉模型）
    
    使用环境变量中的 VISION_API_KEY 和 VISION_MODEL 配置
    """
    from langchain_openai import ChatOpenAI

        
    return ChatOpenAI(
        base_url=base_url,
        api_key=qwen_api_key,
        model=qwen_model,
    )

# 预创建的模型实例
model = create_model()
