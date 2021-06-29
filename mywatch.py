import tkinter as tk 
from tkinter import ttk
from time import strftime
from tkinter import *
from tkcalendar import *
win=tk.Tk()
win.title("My Clock")
win.geometry("300x300")

###calendar
from tkinter import *
from tkcalendar import *
tit=Label(win,text="Calendar",bg="red",fg='White',font=("Times New Roman",14))
tit.grid(row=0,column=0)
cal=Calendar(win,setmode="day",date_pattern='d/m/yy')
cal.grid(row=3,column=0)
##time
####
def mytime():
    string=strftime('%H:%M:%S %p')
    showtime.config(text=string)
    showtime.after(1000,mytime)

curtime=Label(win,text="Current Time : ",bg="red",fg='White',font=("Times New Roman",14))
curtime.grid(row=4,column=0)
showtime=ttk.Label(win,font=("ds-digital,20"))
showtime.grid(row=6,column=0)
mytime()



win.mainloop()