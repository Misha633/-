import pyautogui
import time

v = int(input('Сколько раз мне кликнуть? '))
i = int(input('С интервалом во сколько секунд? '))
while v > 0:
    v -= 1
    pyautogui.click()
    time.sleep(i)
  
  
  
  
  
  
  





