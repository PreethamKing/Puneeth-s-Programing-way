#calculator
import tkinter
from tkinter import *
#to create a window
win=tkinter.Tk()
win.title("SIMPL CALCULATOR")
e=Entry(win,bd=5,width=45,relief=GROOVE,bg="black",fg="white")
e.grid(column=0,row=0,padx=20,pady=20,columnspan=3)
#insert the text to display 
def button(number):
    e.insert(END,int(number))
#to clear the text    
def button__clear():
    e.delete(0,END)
#to perform the addition    
def button__add():
    num1=e.get()
    global f_num
    global math 
    math="addition"
    f_num=int(num1)  
    e.delete(0,END)    
#to perform the subtraction
def button__sub():
    num1=e.get()
    global f_num
    global math 
    math="subtraction"
    f_num=int(num1)  
    e.delete(0,END) 
#to perform the division          
def button__divide():
    num1=e.get()
    global f_num
    global math 
    math="division"
    f_num=int(num1)  
    e.delete(0,END)  
#to perform the multiplication     
def button__multi():
    num1=e.get()
    global f_num
    global math 
    math="multiplication"
    f_num=int(num1)  
    e.delete(0,END)    
#to get result
def button__equal():
    num2=e.get()
    f_num2=int(num2)
    e.delete(0,END)   
    if math=="addition":
        e.insert(0,f_num+f_num2)
    elif math=="subtraction":
        e.insert(0,f_num-f_num2)
    elif math=="multiplication":  
        e.insert(0,f_num*f_num2)
    elif math=="division":
        result=format(f_num/f_num2,".2f")
        e.insert(0,result)     
#for buttons    
button_1=Button(win,text="1" ,padx=40,pady=20,command=lambda:button(1),bd=5,relief=GROOVE,bg="black",fg="white")
button_2=Button(win,text="2" ,padx=40,pady=20,command=lambda:button(2),bd=5,relief=GROOVE,bg="black",fg="white")
button_3=Button(win,text="3" ,padx=40,pady=20,command=lambda:button(3),bd=5,relief=GROOVE,bg="black",fg="white")
button_4=Button(win,text="4" ,padx=40,pady=20,command=lambda:button(4),bd=5,relief=GROOVE,bg="black",fg="white")
button_5=Button(win,text="5" ,padx=40,pady=20,command=lambda:button(5),bd=5,relief=GROOVE,bg="black",fg="white")
button_6=Button(win,text="6" ,padx=40,pady=20,command=lambda:button(6),bd=5,relief=GROOVE,bg="black",fg="white")
button_7=Button(win,text="7" ,padx=40,pady=20,command=lambda:button(7),bd=5,relief=GROOVE,bg="black",fg="white")
button_8=Button(win,text="8" ,padx=40,pady=20,command=lambda:button(8),bd=5,relief=GROOVE,bg="black",fg="white")
button_9=Button(win,text="9" ,padx=40,pady=20,command=lambda:button(9),bd=5,relief=GROOVE,bg="black",fg="white")
button_0=Button(win,text="0" ,padx=40,pady=20,command=lambda:button(0),bd=5,relief=GROOVE,bg="black",fg="white")
button_add=Button(win,text="+",padx=40,pady=20,command=button__add,bd=5,relief=GROOVE,bg="black",fg="white")
button_sub=Button(win,text="-",padx=41,pady=20,command=button__sub,bd=5,relief=GROOVE,bg="black",fg="white")
button_multi=Button(win,text="X",padx=40,pady=20,command=button__multi,bd=5,relief=GROOVE,bg="black",fg="white")
button_divide=Button(win,text="/",padx=40,pady=20,command=button__divide,bd=5,relief=GROOVE,bg="black",fg="white")
button_equal=Button(win,text="  =  ",padx=82,pady=20,command=button__equal,bd=5,relief=GROOVE,bg="black",fg="white")
button_clear=Button(win,text="clear",padx=82,pady=20,command=button__clear,bd=5,relief=GROOVE,bg="black",fg="white")
#to insert the buttons in the window
button_1.grid(column=0,row=3)
button_2.grid(column=1,row=3)
button_3.grid(column=2,row=3)
button_0.grid(column=0,row=4)
button_4.grid(column=0,row=2)
button_5.grid(column=1,row=2)
button_6.grid(column=2,row=2)
button_7.grid(column=0,row=1)
button_8.grid(column=1,row=1)
button_9.grid(column=2,row=1)
button_add.grid(column=0,row=5)
button_sub.grid(column=0,row=6)
button_multi.grid(column=1,row=6)
button_divide.grid(column=2,row=6)
button_clear.grid(column=1,row=4,columnspan=3)
button_equal.grid(column=1,row=5,columnspan=3)
#looping the window
win.mainloop()