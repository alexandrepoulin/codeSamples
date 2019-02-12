import win32api
import win32console
import win32gui
import pythoncom,pyHook
import time
import math
import matplotlib.pyplot as plt
 
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
start=time.time()

f=open(r"C:\Users\AlexandrePoulin\Documents\cool python programs\output.txt",'w')
f.write("")
f.close()
data=[]
start = False
step=0.001

def graph():
    global data
    print(len(data))
    if len(data)==0:
        print("data is empty")
        return
    start = data[0]
    end = data[-1]
    numOfBins = math.ceil((end-start)/step)
    x = [step+step*i for i in range(numOfBins)]
    biny = [0 for i in range(numOfBins)]
    for i in data:
        biny[math.floor((i-start)/step)]+=1
    y = [sum(biny[max(0,i-int(1/step+1)):i+1]) for i in range(numOfBins)]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x,y,axes= ax,c='b') ##the points
    plt.grid(True)
    plt.show()
    data=[]
        
    

def OnKeyboardEvent(event):
    global data
    global start
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
        #open output.txt to read current keystrokes
        keylogs=chr(event.Ascii)
        if keylogs=='p':
            graph()
        elif keylogs=='c':
            data = []
        elif keylogs=='e':
            exit()
        elif keylogs=='s':
            start= not start
            print("Recording ON" if start else "Recording OFF")
        else:
            if start:
                data.append(time.time()-start)

print("Instructions: \nStart/Stop recording : s \nClear recording: c \nPlot the data: p \nExit:e")




# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
