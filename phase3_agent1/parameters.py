from argparse import ArgumentParser


def get_args(goal):

    parser = ArgumentParser(description='Arguments for controlling the computer actions.')

    parser.add_argument('--instruction-operation',
                        type=str,
                        default=(f'现假设你是一位电脑操作员，输入图片是你的电脑屏幕截图，输入语句是你想要实现的操作，请在下列指令集中选择你立刻要执行的指令\n'
                                 f'Double Click: 表示鼠标左键双击\n'
                                 f'Left Click: 表示鼠标左键单击\n'
                                 f'Right Click: 表示鼠标右键单击\n'
                                 f'Type: 表示输入文字。对于输入的内容，请用;符号与指令分隔开\n'
                                 f'Enter: 表示点击回车键\n'
                                 f'END: 表示目标已达成，无需任何操作\n'
                                 f'要求只输出一个指令，输出不含其他任何词句\n'
                                 f'注意：从桌面打开应用时需要双击；除了Type之外的指令，输出后不要附加任何文字'),
                        help='Instruction for thought process.')

    parser.add_argument('--instruction-location',
                        type=str,
                        default=(f'现假设你是一位电脑操作员，输入图片是你的电脑屏幕截图，输入语句是你想要实现的操作。\n'
                                 f'请根据图片选择你接下来要用鼠标操作的区域，并输出这块区域的UI坐标。\n'
                                 f'输出的格式形如：[x,y,w,h]，它们表示该区域左上角在图像中的像素坐标以及区域的宽高。\n'
                                 f'要求只输出一个坐标，输出不含其他任何词句.区域可以大一些，但它的中心一定要尽可能靠近你想要用鼠标操作的地点\n'),
                        help='Instruction for actions.')

    parser.add_argument('--instruction-fix',
                        type=str,
                        default=f"你是电脑的操纵者，输入的图片是你面对的电脑屏幕的截图，输入的动作是你即将采取的指令，它们的含义如下：\n"
                                f"'Double Click;[x,y,w,h];': 表示双击，[x,y,w,h]指示鼠标的屏幕UI坐标范围，其中x,y为区域左上角UI坐标，w,h则为区域的宽度与高度\n"
                                f"'Left Click;[x,y,w,h];': 表示左键，[x,y,w,h]指示鼠标的屏幕UI坐标范围，其中x,y为区域左上角UI坐标，w,h则为区域的宽度与高度\n"
                                f"'Right Click;[x,y,w,h];': 表示右键，[x,y,w,h]指示鼠标的屏幕UI坐标范围，其中x,y为区域左上角UI坐标，w,h则为区域的宽度与高度\n"
                                f"'Type;[x,y,w,h];sentence': 表示输入文字，[x,y,w,h]指示鼠标的屏幕UI坐标范围，sentence为要输入的文字段，请你生成。注意，Type操作隐含两个子动作：指定位置的左键与敲入对应的文本。\n"
                                f"'Enter;[x,y,w,h];': 表示按下键盘回车键，[x,y,w,h]指示鼠标的屏幕UI坐标范围\n"
                                f"'END;;': 表示任务已完成，不采取任何行动\n"
                                f"请结合以上信息，对你采取行动的结果做出预期，描述采取动作后处在一个什么样的状态。要求一句话即可，切忌冗余。\n",
                        help='Explanation of actions.')

    parser.add_argument('--img-base-path',
                        type=str,
                        default='E:/projects/project41-LLM/7/phase3_agent1/tmp',
                        help='Base path for images.')

    parser.add_argument('--history-operation',
                        type=str,
                        default='E:/projects/project41-LLM/7/phase3_agent1/log/history_operation.txt',
                        help='Path to history thought log file.')

    parser.add_argument('--history-location',
                        type=str,
                        default='E:/projects/project41-LLM/7/phase3_agent1/log/history_location.txt',
                        help='Path to history action log file.')

    parser.add_argument('--history-fix',
                        type=str,
                        default='E:/projects/project41-LLM/7/phase3_agent1/log/history_fix.txt',
                        help='Path to history explanation log file.')

    parser.add_argument('--model',
                        type=str,
                        default="Qwen/Qwen2.5-VL-72B-Instruct",
                        help='Model name or path.')

    parser.add_argument('--container',
                        type=int,
                        default=100,
                        help='Container size.')

    parser.add_argument('--history-mode',
                        action='store_true',
                        default=True,
                        help='Enable history mode.')

    args = parser.parse_args()
    return args