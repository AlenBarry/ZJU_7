from argparse import ArgumentParser


def get_args(goal):

    parser = ArgumentParser(description='Arguments for controlling the computer actions.')

    parser.add_argument('--instruction-thought',
                        type=str,
                        default=(f"你是电脑的操纵者，输入的图片是你面对的电脑屏幕的截图。"
                                 f"请根据要求输出一个你马上需要执行的具体的动作。"
                                 f"如果你的输出步骤是多步的，只输出第一步。如果你判断目标已经达成，输出你的判断。"
                                 f"请着重注意你的历史决策信息，尽量不要采取重复决策。"),
                        help='Instruction for thought process.')

    parser.add_argument('--instruction-action',
                        type=str,
                        default=(f"你是一位指令发布员。输入的命令是你要执行的行动，输入的图片是你面对的电脑屏幕的截图。现在请你根据输入信息确定你要将鼠标移动到屏幕上的哪里，以及采取什么样的操作: \n"
                                 f"'Double Click;[x,y,w,h];': 表示双击，[x,y,w,h]指示鼠标的屏幕UI坐标范围，其中x,y为区域左上角UI坐标，w,h则为区域的宽度与高度\n"
                                 f"'Left Click;[x,y,w,h];': 表示左键，[x,y,w,h]指示鼠标的屏幕UI坐标范围，其中x,y为区域左上角UI坐标，w,h则为区域的宽度与高度\n"
                                 f"'Right Click;[x,y,w,h];': 表示右键，[x,y,w,h]指示鼠标的屏幕UI坐标范围，其中x,y为区域左上角UI坐标，w,h则为区域的宽度与高度\n"
                                 f"'Type;[x,y,w,h];sentence': 表示输入文字，[x,y,w,h]指示鼠标的屏幕UI坐标范围，sentence为要输入的文字段，请你生成。注意，Type操作隐含两个子动作：指定位置的左键与敲入对应的文本。\n"
                                 f"'Enter;[x,y,w,h];': 表示按下键盘回车键，[x,y,w,h]指示鼠标的屏幕UI坐标范围\n"
                                 f"'END;;': 表示任务已完成，不采取任何行动\n"
                                 f"请根据要求严格按照以上格式输出一个指令，不得输出其他任何的额外文字\n"
                                 f"注意：从桌面打开应用时需要双击"),
                        help='Instruction for actions.')

    parser.add_argument('--instruction-expectation',
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
                        default='E:/projects/project41-LLM/7/phase3_agent2/tmp',
                        help='Base path for images.')

    parser.add_argument('--history-thought',
                        type=str,
                        default='E:/projects/project41-LLM/7/phase3_agent2/log/history_thought.txt',
                        help='Path to history thought log file.')

    parser.add_argument('--history-action',
                        type=str,
                        default='E:/projects/project41-LLM/7/phase3_agent2/log/history_action.txt',
                        help='Path to history action log file.')

    parser.add_argument('--history-expectation',
                        type=str,
                        default='E:/projects/project41-LLM/7/phase3_agent2/log/history_explanation.txt',
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