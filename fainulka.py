import pyautogui as py
import time

zinute = "justeli nebenusisnekek"
count = 1

time.sleep(2)
for i in range(200):
    py.typewrite(zinute + " " + str(count))
    py.press("Enter")
    count +=1


