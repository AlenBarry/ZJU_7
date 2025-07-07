from run_memory_api import communication
import os

def clear_history(path):
    with open(path, 'w',encoding='utf-8') as f:
        pass

if __name__ == '__main__':
    img_base_path='E:/projects/project41-LLM/7/data'

    input_sentence='观察输入图片有哪些变化，猜测电脑操作者的目的'
    #'观察输入图片有哪些变化，猜测电脑操作者的目的'
    history_mode=True
    history_path='E:/projects/project41-LLM/7/phase1/log/history.txt'
    container=10
    answer={}
    for root, dirs, files in os.walk(img_base_path):
        if root == img_base_path:
            continue

        for file in files:
            img_path=os.path.join(root, file)
            answer[img_path]=communication(input_sentence,img_path,history_path,
                                           "Qwen/Qwen2.5-VL-72B-Instruct",
                                           container,'',history_mode)
            print(img_path,"完成")

        clear_history(history_path)

    with open('vqa2.txt','w',encoding='utf-8') as f:
        for key,value in answer.items():
            print("Input Sentence:",input_sentence,file=f)
            print("Input Picture:",key,file=f)
            print("Output:",value,file=f)
            print('\n',file=f)