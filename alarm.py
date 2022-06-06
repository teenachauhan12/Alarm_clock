from tkinter import*
from tkinter.ttk import Combobox
from tkinter.messagebox import*
import datetime

from playsound import playsound

root=Tk()

Clocking=PhotoImage(file="/home/teena/Downloads/alarmclock.png")
img=Label(root,image=Clocking)
img.grid(rowspan=12,column=0)

def alarm():
    h=int(c.get())
    m=int(c1.get())
    
    showinfo("alarm notication","alarm has been set")
    print(datetime.datetime.now())
    while True:
        if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
            for j in range(2):
                playsound('https://musikringtone.com//downloads//5845//')
                break
root.title(" my alaram clock")

l1=Label(root,text="set alarm hour")
l1.grid(row=0,column=0)
hour=list(range(1,25))
c=Combobox(root,values=hour)
c.grid(row=0,column=10)
 

l2=Label(root,text="set alarm minute")
l2.grid(row=1,column=0)
minute=list(range(1,61))
c1=Combobox(root,values=minute)
c1.grid(row=1,column=10)


btn=Button(root,text="set alarm",command=alarm)
btn.grid(row=2,column=2)
root.mainloop()


