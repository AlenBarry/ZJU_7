from run_memory_api import communication
import os
if __name__ == '__main__':
    img_base_path='E:/projects/project41-LLM/7/data'
    input_sentence='请描述这张图片'
    history_mode=False
    answer={}
    for root, dirs, files in os.walk(img_base_path):
        if root == img_base_path:
            continue
        for file in files:
            img_path=os.path.join(root, file)
            answer[img_path]=communication(input_sentence,img_path,'',
                                           "Qwen/Qwen2.5-VL-72B-Instruct",
                                           0,"",history_mode)
            print(img_path,"完成")

    with open('caption.txt','w',encoding='utf-8') as f:
        for key,value in answer.items():
            print("Input Sentence:",input_sentence,file=f)
            print("Input Picture:",key,file=f)
            print("Output:",value,file=f)
            print('\n',file=f)




