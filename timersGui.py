from tkinter import *

from urllib.request import *
import urllib.error
import time
import math
import winsound




NumBoxes = 11*4
labels = [2,3,4,5,6,9,10,11,12,13,14,18,20,22,27,28,29,30,33,34,36,38,41,42,43,44,46,50,51,52,54,58,59,62,65,67,68,69,70,74,75,76,77,86]
nums = list(range(NumBoxes))

timeDiff = 12*60

def color(r,g,b):
    return '#%02x%02x%02x' % (r, g, b)

class GUIwindow:

    def __init__(self):
        self.master = Tk()
        self.time = 0
        self.times = [0 for i in range(NumBoxes)]
  

        backFrame = Frame(self.master,bg="black",width=1024,height=759-110)
        backFrame.pack()


        inputFrame = Frame(backFrame,bg="black",width=1024,height=759)
        inputFrame.place(relx=0, rely=0)

        inputFrame.pack_propagate(0)
        rowFrames = []
        for i in range(11):
            rowFrames.append(Frame(inputFrame,bg="Black",width=1024,height=int(759/11)))
            rowFrames[i].pack(side=TOP,fill=X)
        

        self.buttons = []
        self.frames = []
        self.labels = []
        self.textVar = [StringVar(self.master) for i in range(NumBoxes)]

        colors = ["lightgreen","gold"]
        
        for i in range(NumBoxes):
            self.textVar[i].set("00:00")

            self.frames.append(Frame(rowFrames[i//4],bg="black", width=int(1024/4),height=int(759/11)))
            
            self.frames[i].pack(side=LEFT,fill=X,expand=1,padx=2, pady=2)
            
            ##self.frames[i].pack_propagate(0)
            self.labels.append(Label(self.frames[i],bg=colors[(i//4)%2],fg="black",text=str(labels[i]),))
            self.buttons.append(Button(self.frames[i],bg="lightblue",textvariable=self.textVar[i],command=lambda i=i:self.clicked(i)))
            ##,width=int(1024/4)-2,height=int(768/44-6)
            self.labels[i].pack(side=TOP,fill=X,expand=1,padx=2, pady=2)

            self.buttons[i].pack(side=TOP,fill=X,expand=1,padx=2, pady=2)

        self.update_clock()
        self.master.mainloop()

    def update_clock(self):
        self.time = time.time()
        self.master.after(100, self.update_clock)
        self.master.after(100, self.update)
        
 
    def clicked(self,i):
        if self.buttons[i].cget('bg') != "lightblue" and self.times[i] == 0:
            self.buttons[i].configure(bg="lightblue")
        else:
            self.times[i] = time.time()
        
        return
    
    def update(self):
        for i in range(NumBoxes):
            if self.times[i] == 0:
                continue
            diff = timeDiff +(self.times[i]-self.time)
            if diff > 0:
                minutes = str(int(diff//60))
                if diff//60 <10:
                    minutes = "0"+minutes
                seconds = str(int(diff%60))
                if diff%60 <10:
                    seconds = "0"+seconds
                self.textVar[i].set(minutes + ":" + seconds)

                self.buttons[i].config(bg=color(int(255*math.sqrt(1-(diff/(timeDiff))**2)),int(255*diff/(timeDiff)),0))
                if (minutes + ":" + seconds) == "00:00":
                    self.times[i] = 0
                    winsound.Beep(1400, 150)
                    winsound.Beep(1200, 150)
                    winsound.Beep(1400, 150)
                    winsound.Beep(1200, 150)
                    self.buttons[i].flash()
                    self.buttons[i].flash()
                    



if __name__ == "__main__":
    test = GUIwindow()
