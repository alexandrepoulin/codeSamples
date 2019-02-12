import win32con
from win32 import win32api
import time

topLeft = (1353,534)
bottomRight = (1466,681)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


while True:
    pos = win32api.GetCursorPos()
    if pos[0] > topLeft[0] and pos[0] < bottomRight[0] and pos[1] > topLeft[1] and pos[1]<bottomRight[1]:
        click(pos[0],pos[1])
##        time.sleep(0.1)


