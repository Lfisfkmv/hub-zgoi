import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-c51d063620df4e3285041881ecb00673",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-vl-plus",  # 此处以qwen-vl-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[{"role": "user","content": [
            {"type": "image_url",
             "image_url": {"url": "https://img1.baidu.com/it/u=1693453968,3801821316&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=1067"}},
            {"type": "text", "text": "这是猫还是狗?"},
            ]}]
    )
print(completion.model_dump_json())