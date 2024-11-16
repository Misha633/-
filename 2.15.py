import time
import pyautogui

print("Что мне нарисовать: круг, квадрат или домик?")
sl = input()

if sl != "круг" or "квадрат" or "домик":
    pass

if sl == "круг":
    print("Сейчас начнём!")
    pyautogui.press('win')
    pyautogui.hotkey('p', 'a', 'i', 'n', 't')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(1, 1)
    time.sleep(1)
    pyautogui.moveTo(400, 30)
    pyautogui.click(button = "right")
 







