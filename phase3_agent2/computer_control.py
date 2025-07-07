import pyautogui
import pyperclip
def left_click(x,y,t=0.5):
    pyautogui.moveTo(x,y,duration=t)
    pyautogui.click(x,y,button='left')

def right_click(x,y,t=0.5):
    pyautogui.moveTo(x,y,duration=t)
    pyautogui.click(x,y,button='right')

def double_click(x,y,t=0.5):
    pyautogui.moveTo(x,y,duration=t)
    pyautogui.doubleClick(x,y)

def type(info):
    pyperclip.copy(info)
    pyautogui.hotkey('ctrl', 'v')

def enter():
    pyautogui.press('enter')

def photo_shot(path):
    screenshot = pyautogui.screenshot()
    screenshot.save(path)

def local_photo_shot(path,region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(path)