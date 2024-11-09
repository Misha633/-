import pyautogui
import time
print("1 или 2?")
ch = int(input())

if ch == 1:
    pyautogui.press('win')
    pyautogui.write('Google Chrome')
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write('hfpevty kb z?')
    pyautogui.press("enter")


if ch == 2:
    pyautogui.press('win')
    pyautogui.write('Google Chrome')
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write('Ckfdf hj,jnfv!')
    pyautogui.press("enter")



















