import time
import pyautogui
from parameters import get_args
from computer_control import photo_shot,double_click,left_click,right_click,type,enter,local_photo_shot
from run_memory_api import communication
#我们调用三个QW大模型，让它们协同工作
#它们的system统一设置为我们的
#一个负责观察，输入屏幕截图输出下一步需要立即操作的步骤 thought
#一个负责发出指令， action
#一个负责对指令进行验证/解释说明，确保合理性 expectation
#这是根据demo进行的复现。事实上我不清楚第三个有什么意义。所以我会给它安装上判断目标是否达成的功能

def clear_history(args):
    with open(args.history_operation, 'w') as file:
        pass
    with open(args.history_location, 'w') as file:
        pass
    with open(args.history_fix, 'w') as file:
        pass

def take_action(operation,region):

    x,y,w,h=region
    loc_x,loc_y=x+w//2,y+h//2

    if operation.startswith('Double Click'):
        double_click(loc_x,loc_y)
        return 0
    if operation.startswith('Left Click'):
        left_click(loc_x,loc_y)
        return 0
    if operation.startswith('Right Click'):
        right_click(loc_x,loc_y)
        return 0
    if operation.startswith('Type'):
        left_click(loc_x,loc_y)
        type(operation.split(';')[1])
        return 0
    if operation.startswith('Enter'):
        enter()
        return 0
    if operation.startswith('END'):
        return 1

def get_region(location):
    return [int(item) for item in location[1:-1].split(',')]

def engine(goal):

    print("用户需求:",goal)
    args=get_args(goal)
    clear_history(args)
    print("5秒后程序开始运行，请调整至合适的页面，并将鼠标置于任务栏外")
    expectation=""
    time.sleep(5)

    i=0
    while True:
        if i==15:
            break
        print(f"第{i+1}轮行动开始")
        #观察电脑屏幕
        img_path=args.img_base_path+f'/screen{i}.png'
        photo_shot(img_path)
        input_operation=goal
        operation=communication(input_operation, img_path, args.history_operation, args.model,
                              args.container, args.instruction_operation, args.history_mode)
        print(operation)

        #然后，根据想法选择行动
        input_location=goal
        location=communication(input_location, img_path, args.history_location, args.model,
                              args.container, args.instruction_location, args.history_mode)
        print(location)

        region=get_region(location)
        print(region)

        status=take_action(operation,region)
        if status==1:
            print("目标已达成")
            break

        sub_img_path = args.img_base_path + f'_sub/screen{i}.png'
        local_photo_shot(sub_img_path, region)

        time.sleep(2.5)
        i+=1






if __name__ == '__main__':
    #goal="打开飞书"
    goal="用Vscode运行E:/projects/project41-LLM/7/test.py"
    #goal="打开QQ"
    # “给我的QQ好友abc发送祝福信息”
    # “登录西安交通大学思源学堂，网址https: // syxt.xjtu.edu.cn /，账号2204112910，密码 ** ** ** ”（出于信息保密，实际运行时输入为真实密码）
    # “用Vscode运行E:\projects\project41-LLM\7\test.py”
    engine(goal)

