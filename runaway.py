##plays http://www.hacker.org/runaway/

import math, time, win32con
from PIL import ImageFile, Image, ImageTk, ImageGrab
from win32 import win32api

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def recurse(sol):
    res=testSolution(sol)
    if res == 2:
        return sol
    if res == 1:
        if len(sol)<MAXLEN:
            case1 = recurse(sol + [True])
            if case1 != 0:
                return case1
            case2 = recurse(sol + [False])
            if case2 != 0:
                return case2
    return 0
        
def testSolution(sol):
    solLen=len(sol)
    pos=[0,0]
    counter =-1
    while True:
        counter+=1
        if sol[counter%solLen]:
            pos[0]+=1
        else:
            pos[1]+=1
        if max(pos)==SIZE:
            return 2
        if pos in TRAPS:
            if counter >=solLen:
                return 1
            else:
                return 0

def solve():
    case1 = recurse([True])
    if case1 != 0:
        return case1
    return recurse([False])

def printTRAPS():
    breakline = "".join(" -" for i in range(SIZE))
    print(breakline)
    for i in range(SIZE):
        line = "|"
        for j in range(SIZE):
            if [j,i] in TRAPS:
                line+="X|"
            else:
                line+=" |"
        print(line)
        print(breakline)

redo=False
redoAnswer= ""
redoList=[]
while True:
    #image= Image.open('runaway.png')
    image= ImageGrab.grab()
    image.save(r"C:\Users\AlexandrePoulin\Documents\cool python programs\lastScreen.png")

    rgb_im = image.convert('RGB')

    modifiedCopy=rgb_im.copy()

    MAXLEN=15

    pixelCorner = (12,311)
    lengthPixel=457
    pixelCounter = 0
    cellSize=-1
    step1=False
    while True:
        pixelCounter+=1
        r,g,b=rgb_im.getpixel((pixelCorner[0]+pixelCounter,pixelCorner[1]))
        if r+g+b>=3*245:
            step1=True
        if r+g+b<=3*241 and step1:
            cellSize=pixelCounter
            break

    SIZE=round((lengthPixel-pixelCorner[0])/cellSize)
    if redo:
        for i in redoList:
            if i=='1':
                SIZE+=1
            else:
                SIZE-=1
    redo=False
    cellSize=(lengthPixel-pixelCorner[0])/SIZE
    offset=0.6*cellSize
    TRAPS=[]
    for row in range(SIZE):
        for col in range(SIZE):
            if row == 0 and col == 0:
                continue
            r,g,b=rgb_im.getpixel((round(pixelCorner[0]+offset+col*cellSize),round(pixelCorner[1]+offset+row*cellSize)))
            modifiedCopy.putpixel((round(pixelCorner[0]+offset+col*cellSize),round(pixelCorner[1]+offset+row*cellSize)),(0,0,0))
            if b<200:
                TRAPS.append([col,row])
    modifiedCopy.save(r"C:\Users\AlexandrePoulin\Documents\cool python programs\modifiedCopy.png")
    printTRAPS()
    
    sol = solve()

    if sol ==0:
        MAXLEN +=1
        print("failed, increasing maxlen")
        continue
    else:
        temp=len(sol)*math.floor(MAXLEN/len(sol))
        for i in range(temp):
            if sol[i%len(sol)]:
                click(50,200)
            else:
                click(120,200)
        click(270,200)
        print("solved")
        print(sol)

    print("Did it work? Had the following:")
    print("SIZE: ", SIZE)
    print("MAXLEN: ", MAXLEN)
    redoAnswer=input("(0:y,1:SIZE+,2:SIZE-)")
    if redoAnswer != '0':
        redoList.append(redoAnswer)
        redo=True
        click(50,200)
        for i in range(2*temp):
            click(200,200)
    else:
        redoList=[]
        click(50,200)
        
    time.sleep(1)
    

        




print(solve())
            
