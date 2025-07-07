from openai import OpenAI
import base64
client = OpenAI(
    api_key="2af2f9ee-cd25-4fcf-ba82-c76498919938",
    base_url="https://api-inference.modelscope.cn/v1"
)

def create_content(type,info):
    if type=="text":
        return {"type": "text","text": info}
    if type=="image_url":
        return {"type": "image_url","image_url": {"url": f"data:image/jpeg;base64,{info}"}}

def create_message(role,sentence,image_path=''):
    message={}
    message["role"]=role
    content=[create_content("text",sentence)]
    if image_path!='':
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        content.append(create_content("image_url",encoded_string))
    message["content"]=content
    return message


def init_message(INSTRUCTIONS):
    return [create_message('system',INSTRUCTIONS)]

def str_preprocess(s):
    s=s.replace('\n','<换行符>')
    s=s.replace(' ','<空格符>')
    return s

def str_anti_preprocess(s):
    s=s.replace('<换行符>','\n')
    s=s.replace('<空格符>',' ')
    return s

def read_history(messages,history_path):
    with open(history_path,'r',encoding='utf-8') as f:
        for line in f:
            tem=line.split(' ')
            tem[-1]=tem[-1][:-1]
            if tem[0]=="assistant":
                tem.append('')
            messages.append(create_message(tem[0],str_anti_preprocess(tem[1]),tem[2]))
    return messages

def write_history(sentence,image_path,reply,history_path):
    with open(history_path,"a",encoding='utf-8') as f:
        print(f'user {sentence} {image_path}',file=f)
        print(f'assistant {reply}',file=f)

def count_history(history_path):
    count=0
    with open(history_path,'r',encoding='utf-8') as f:
        for line in f:
            count+=1
    return count

def delete_history(history_path):
    # 打开文件并读取内容
    with open(history_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 跳过前两行并将剩余的内容写回文件
    with open(history_path, 'w', encoding='utf-8') as file:
        file.writelines(lines[2:])

def communication(sentence,image_path,history_path,MODEL,CONTAINER,INSTRUCTIONS,HISTORY_MODE=True):
    #print("请输入对话文本:")
    #print("请上传图片地址：")
    model=MODEL
    messages = init_message(INSTRUCTIONS)
    if HISTORY_MODE:
        messages = read_history(messages,history_path)
    messages.append(create_message("user",sentence,image_path))
    response = client.chat.completions.create(model=model,messages=messages)
    #print("模型回复:", response.choices[0].message.content)

    if HISTORY_MODE:
        reply=str_preprocess(response.choices[0].message.content)
        sentence=str_preprocess(sentence)
        write_history(sentence,image_path,reply,history_path)
        count=count_history(history_path)
        if count>CONTAINER*2:
            delete_history(history_path)

    return response.choices[0].message.content



if __name__ == '__main__':
    sentence="这是一张电脑桌面的截图。请为我输出应用“飞书”的可点击UI坐标区域。输出格式形如‘[x1,y1,x2,y2]’。只输出坐标，不要有其他冗余文字"
    image_path='E:/projects/project41-LLM/7/computer_control/pics/screen.png'
    history_path='E:/projects/project41-LLM/7/history.txt'
    MODEL = "Qwen/Qwen2.5-VL-72B-Instruct"
    CONTAINER = 10
    INSTRUCTIONS = "你是一个助手，能够理解图像并回答相关问题。"
    HISTORY_MODE = True
    communication(sentence,image_path,history_path,MODEL,CONTAINER,INSTRUCTIONS,HISTORY_MODE)


