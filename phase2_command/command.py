from run_memory_api import communication
import os

def clear_history(path):
    with open(path, 'w',encoding='utf-8') as f:
        pass

if __name__ == '__main__':
    img_base_path='E:/projects/project41-LLM/7/data'

    input_sentence=['给我的QQ好友abc发送祝福信息','登录西安交通大学思源学堂，网址https://syxt.xjtu.edu.cn/，账号2204112910，密码whoami@721521','用Vscode运行E:/projects/project41-LLM/7/test.py']
    instruction=(f'现假设你是一位电脑操作员，输入图片是你的电脑屏幕截图，输入语句是你想要实现的操作，请在下列指令集中选择你立刻要执行的指令\n'
                f'Double Click: 表示鼠标左键双击\n'
                f'Left Click: 表示鼠标左键单击\n'
                f'Right Click: 表示鼠标右键单击\n'
                f'Type: 表示输入文字。对于输入的内容，请用;符号与指令分隔开\n'
                f'Enter: 表示点击回车键\n'
                f'END: 表示目标已达成，无需任何操作\n'
                f'要求只输出一个指令，输出不含其他任何词句\n'
                f'注意：从桌面打开应用时需要双击；除了Type之外的指令，输出后不要附加任何文字')
    history_mode=True
    history_path= 'E:\projects\project41-LLM/7/phase2_command/log/history.txt'
    container=10

    for root, dirs, files in os.walk(img_base_path):

        if root == img_base_path:
            continue
        answer={}
        index=int(root[-1])-1

        for file in files:
            img_path=os.path.join(root, file)
            answer[img_path]=communication(input_sentence[index],img_path,history_path,
                                            "Qwen/Qwen2.5-VL-72B-Instruct",
                                            container,instruction,history_mode)
            print(img_path,"完成")
        with open(f"command{root[-1]}.txt", 'w', encoding='utf-8') as f:
            for key, value in answer.items():
                print("Input Sentence:", input_sentence[index], file=f)
                print("Input Picture:", key, file=f)
                print("Output:", value, file=f)
                print('\n', file=f)
        clear_history(history_path)



