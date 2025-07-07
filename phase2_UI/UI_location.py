from run_memory_api import communication
import os
from PIL import Image,ImageDraw
def clear_history(path):
    with open(path, 'w',encoding='utf-8') as f:
        pass

def UI_shot(img_path,region,loc_path,name):
    region=region[1:-1].split(',')
    region=[int(item) for item in region]
    print(region)
    if len(region)!=4:
        return None,None


    x1,y1,x2,y2=region
    img=Image.open(img_path)
    print(region,img.size)
    cropped_image = img.crop((x1, y1, x1+x2, y1+y2))
    cropped_image.save(loc_path+f'/{name}.png')
    return region,loc_path+f'/{name}.png'




if __name__ == '__main__':
    img_base_path='E:/projects/project41-LLM/7/data'

    input_sentence=['给我的QQ好友abc发送祝福信息','登录西安交通大学思源学堂，网址https://syxt.xjtu.edu.cn/，账号2204112910，密码whoami@721521','用Vscode运行E:/projects/project41-LLM/7/test.py']
    instruction=(f'现假设你是一位电脑操作员，输入图片是你的电脑屏幕截图，输入语句是你想要实现的操作。\n'
                 f'请根据图片选择你接下来要用鼠标操作的区域，并输出这块区域的UI坐标。\n'
                 f'输出的格式形如：[x,y,w,h]，它们表示该区域左上角在图像中的像素坐标以及区域的宽高。\n'
                 f'要求只输出一个坐标，输出不含其他任何词句.区域可以大一些，但它的中心一定要尽可能靠近你想要用鼠标操作的地点\n')
    history_mode=True
    history_path= 'E:\projects\project41-LLM/7/phase2_UI/log/history.txt'
    container=20

    # instruction2=(f"现假设你是一位电脑操作员，输入图片是经过裁剪后的一部分屏幕截图，图片中已经包含了你需要操作的区域。\n"
    #               f"你的任务是进一步确定该区域中鼠标应该点击的位置，并提供一个更加精确的UI坐标。\n"
    #               f"请在给定的裁剪区域内，找出你认为最精确的操作区域，并输出该区域的UI坐标。\n"
    #               f"坐标应包括该区域左上角的全局UI坐标以及区域的宽高。输出的格式应为：[x,y,w,h]。\n"
    #               f"要求：输出的区域应该尽可能精确，且与操作意图的中心对齐。不要输出其他词句。\n")
    # history_path2 = 'E:\projects\project41-LLM/7/phase2_UI/log/history2.txt'
    #
    # instruction3 = (
    #     f'现假设你是一位电脑操作员，输入图片是你的电脑屏幕截图，输入语句是你想要实现的操作，请在下列指令集中选择你立刻要执行的指令\n'
    #     f'Double Click: 表示鼠标左键双击\n'
    #     f'Left Click: 表示鼠标左键单击\n'
    #     f'Right Click: 表示鼠标右键单击\n'
    #     f'Type: 表示输入文字。对于输入的内容，请用;符号与指令分隔开\n'
    #     f'Enter: 表示点击回车键\n'
    #     f'END: 表示目标已达成，无需任何操作\n'
    #     f'要求只输出一个指令，输出不含其他任何词句\n'
    #     f'注意：从桌面打开应用时需要双击；除了Type之外的指令，输出后不要附加任何文字')
    #
    # history_path3 = 'E:\projects\project41-LLM/7/phase2_UI/log/history3.txt'




    for root, dirs, files in os.walk(img_base_path):
        clear_history(history_path)
        # clear_history(history_path2)
        # clear_history(history_path3)

        if root == img_base_path:
            continue
        index=int(root[-1])-1

        for file in files:
            img_path=os.path.join(root, file)
            output=communication(input_sentence[index],img_path,history_path,
                                            "Qwen/Qwen2.5-VL-72B-Instruct",
                                            container,instruction,history_mode)
            name=f"{index+1}_{file.split('.')[0]}"
            region1,img_tmp_path=UI_shot(img_path,output,
                    'E:\projects\project41-LLM/7\phase2_UI/result_v1',name)

            # output3 = communication(input_sentence[index], img_path, history_path3,
            #                        "Qwen/Qwen2.5-VL-72B-Instruct",
            #                        container, instruction3, history_mode)
            #
            #
            # output2=communication(f'在电脑屏幕UI区间{region1}执行操作{output3}',img_tmp_path,history_path,
            #                       "Qwen/Qwen2.5-VL-72B-Instruct",
            #                       container,instruction2,history_mode)
            #
            # region2,p2=UI_shot(img_tmp_path,output2,
            #                  'E:\projects\project41-LLM/7\phase2_UI/result_v3',name)

            print(img_path,"完成")