import pyautogui
import time
import random

count = 374


def clicklocation():
    global count
    pyautogui.moveTo(1548, 336)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(random.uniform(0.1, 0.3))
    pyautogui.leftClick()
    time.sleep(2.3)
    count -= 1
    print("count", count)

while count > 0:
    clicklocation()


# print("Move the mouse to the position you want to capture...")

# # Loop to keep checking the mouse position every 1 second
# while True:
#     x, y = pyautogui.position()  # Get the current position of the mouse
#     print(f"Mouse Position: ({x}, {y})")
#     time.sleep(1)  # Pause for 1 second before checking again