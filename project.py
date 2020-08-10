'''
Created on Jun 27, 2019

@author: cryst
'''
import random 
from tkinter import messagebox
from tkinter import *
from tkinter.constants import LEFT, TOP
from random import randrange
from collections import Counter

    
def colorme(c1):
    if c1==1:
        return "red"
    elif c1==2:
        return "yellow"
    elif c1==3:
        return "blue"
    elif c1==4:
        return "green"
    elif c1==5:
        return "orange"

def selectmax(c2):
    data=Counter(c2)
    return max(c2,key=data.get)

s1=[]
for i in range(1,10):
    s1.append(random.randrange(1,5))
print(s1)
print(selectmax(s1))
max=selectmax(s1)



def matchmax(chosen):   
    if chosen==max:
        messagebox.showinfo("correct choice", "Its a match")
    else:
        messagebox.showerror("Wrong choice", "Try again")
    
def callback1():
    selectedvalue=s1[0]
    matchmax(selectedvalue)
def callback2():
    selectedvalue=s1[1]
    matchmax(selectedvalue)
def callback3():
    selectedvalue=s1[2]
    matchmax(selectedvalue)
def callback4():
    selectedvalue=s1[3]
    matchmax(selectedvalue)
def callback5():
    selectedvalue=s1[4]
    matchmax(selectedvalue)
def callback6():
    selectedvalue=s1[5]
    matchmax(selectedvalue)
def callback7():
    selectedvalue=s1[6]
    matchmax(selectedvalue)
def callback8():
    selectedvalue=s1[7]
    matchmax(selectedvalue)
def callback9():
    selectedvalue=s1[8]
    matchmax(selectedvalue)
    
def callback():
    chosen=s1[i]
    print(chosen)
    
def newgame():
    print("New game")
    
def endgame():
    print("End game")

    

#Display part    
root=Tk()
root.title("Game")
root.geometry("300x300")

#frame to display tiles
frame1=Frame(root)
frame1.place(x=10,y=10,width=300,height=300)
b1=Button(frame1,text="",bg=colorme(s1[0]),command=callback1)
b2=Button(frame1,text="",bg=colorme(s1[1]),command=callback2)
b3=Button(frame1,text="",bg=colorme(s1[2]),command=callback3)
b4=Button(frame1,text="",bg=colorme(s1[3]),command=callback4)
b5=Button(frame1,text="",bg=colorme(s1[4]),command=callback5)
b6=Button(frame1,text="",bg=colorme(s1[5]),command=callback6)
b7=Button(frame1,text="",bg=colorme(s1[6]),command=callback7)
b8=Button(frame1,text="",bg=colorme(s1[7]),command=callback8)
b9=Button(frame1,text="",bg=colorme(s1[8]),command=callback9)

b1.place(x=60,y=60,width=60,height=60)
b2.place(x=60,y=120,width=60,height=60)
b3.place(x=60,y=180,width=60,height=60) 
b4.place(x=120,y=60,width=60,height=60)
b5.place(x=120,y=120,width=60,height=60)
b6.place(x=120,y=180,width=60,height=60)
b7.place(x=180,y=60,width=60,height=60)
b8.place(x=180,y=120,width=60,height=60)
b9.place(x=180,y=180,width=60,height=60)

#toolbar
toolbar=Frame(root)
b=Button(toolbar,text="new game",width=10,command=newgame)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(toolbar,text="end game",width=10,command=endgame)
b.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)

#Frame to display time or status bar
frame2=Frame(root)
frame2.pack(side=BOTTOM,fill=X)
mainloop()


        