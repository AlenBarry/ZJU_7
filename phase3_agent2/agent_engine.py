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

def act(action):
    info=action.split(';')
    if info[0]=='END':
        return 1,(0,0,0,0)

    info[1]=info[1][1:-1].split(',')
    x,y,w,h=[int(item) for item in info[1]]
    loc_x=int(x+w//2)
    loc_y=int(y+h//2)
    region=(x,y,h,w)

    #pyautogui.moveTo(loc_x, loc_y, duration=0.5)
    if info[0]=='Double Click':
        double_click(loc_x,loc_y)
    if info[0]=='Left Click':
        left_click(loc_x,loc_y)
    if info[0]=='Right Click':
        right_click(loc_x,loc_y)
    if info[0]=='Type':
        left_click(loc_x,loc_y)
        type(info[2])
    if info[0]=='Enter':
        enter()
    return 0,region



def clear_history(args):
    with open(args.history_thought, 'w') as file:
        pass
    with open(args.history_action, 'w') as file:
        pass
    with open(args.history_expectation, 'w') as file:
        pass


def engine(goal):

    print("用户需求:",goal)
    args=get_args(goal)
    clear_history(args)
    print("5秒后程序开始运行，请调整至合适的页面，并将鼠标置于任务栏外")
    expectation=""
    time.sleep(5)

    i=0
    while True:
        if i==25:
            break
        print(f"第{i+1}轮行动开始")
        #观察电脑屏幕
        img_path=args.img_base_path+f'/screen{i}.png'
        photo_shot(img_path)
        #首先，产生想法
        input_thought=goal+f"(上一轮操作预期状态{expectation})"
        thought=communication(input_thought, img_path, args.history_thought, args.model,
                              args.container, args.instruction_thought, args.history_mode)
        print("(Thought)",thought)

        #然后，根据想法选择行动
        input_action=thought
        action=communication(input_action, img_path, args.history_action, args.model,
                              args.container, args.instruction_action, args.history_mode)
        print("(Action)",action)
        status,region=act(action)
        if status:
            break

        sub_img_path=args.img_base_path+f'_sub/screen{i}.png'
        local_photo_shot(sub_img_path,region)

        input_expectation=f"目标:'{goal}'，采取行动:'{action}'"
        expectation=communication(input_expectation, img_path, args.history_expectation, args.model,
                                  args.container, args.instruction_expectation, args.history_mode)
        print("(Expectation)",expectation)



        time.sleep(1)
        i+=1






if __name__ == '__main__':
    #goal="打开飞书"
    goal="用Vscode运行E:\projects\project41-LLM/7/test.py"
    # “给我的QQ好友abc发送祝福信息”
    # “登录西安交通大学思源学堂，网址https: // syxt.xjtu.edu.cn /，账号2204112910，密码 ** ** ** ”（出于信息保密，实际运行时输入为真实密码）
    # “用Vscode运行E:\projects\project41-LLM\7\test.py”
    #goal="打开QQ"
    engine(goal)

