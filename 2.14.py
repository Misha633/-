import time
import pyautogui

print("Что мне нарисовать: круг, квадрат или домик?")
sl = input()

if sl != "круг" or "квадрат" or "домик":
    pass

if sl == "круг":
    print("Сейчас начнём!")
    pyautogui.press('win')
    pyautogui.hotkey('p', 'a', 'i', 'n', 'T')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(530, 60)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(530, 400)
    time.sleep(1)
    pyautogui.dragTo(200, 100, button='left')
    
if sl == "квадрат":
    print("Сейчас начнём!")
    pyautogui.press('win')
    pyautogui.hotkey('p', 'a', 'i', 'n', 't')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(550, 60)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(530, 400)
    time.sleep(1)
    pyautogui.dragTo(200, 100, button='left')
    

    
 







