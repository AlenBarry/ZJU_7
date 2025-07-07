from openai import OpenAI
import base64
client = OpenAI(
    api_key="2af2f9ee-cd25-4fcf-ba82-c76498919938",
    base_url="https://api-inference.modelscope.cn/v1"
)

# 读取图片文件并转换为 base64 编码
image_path = "E:/projects/project41-LLM/7/test.png"  # 替换为你的图片路径
with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")




response = client.chat.completions.create(
    model="Qwen/Qwen2.5-VL-72B-Instruct",
    messages=[{"role": "user","content": [

                #{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_string}"}},
                {"type": "text","text": "你好"}
            ]
        }
    ]
)
print(response.choices[0].message.content)