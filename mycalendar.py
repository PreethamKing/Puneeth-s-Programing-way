import tkinter 
from tkinter import *

win=tkinter.Tk()

win.title("Calendar")

def cal():
    import calendar
    year=int(year_entry.get())
    month=int(month_entry.get())
    result=(calendar.month(year,month))
    cal_lbl=Label(win,text=result,bd=5,relief=GROOVE,fg="black")
    cal_lbl.grid(row=5,column=9)

btn=Button(win,text='Click for Calendar',bd=5,relief=GROOVE,bg="plum",fg="black",command=cal)
btn.grid(row=5,column=3)
month_lbl=Label(win,text='Month',bd=5,relief=GROOVE,fg="black")
month_lbl.grid(row=2,column=0)
year_lbl=Label(win,text='Year',bd=5,relief=GROOVE,fg="black")
year_lbl.grid(row=4,column=0)
month_entry=Entry(win,width=15, font=("Bold", 16), bd=5, relief=GROOVE)
month_entry.grid(row=2,column=3)
year_entry=Entry(win,width=15, font=("Bold", 16), bd=5, relief=GROOVE)
year_entry.grid(row=4,column=3)

win.mainloop()