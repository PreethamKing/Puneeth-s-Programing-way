#Image viewer using tkinter
import tkinter
from tkinter import *
from PIL import ImageTk,Image  #python image library--->PIL
win=tkinter.Tk()
win.title("Image")
#calling the image
my_image1=ImageTk.PhotoImage(Image.open("1.png"))
my_image2=ImageTk.PhotoImage(Image.open("2.png"))
my_image3=ImageTk.PhotoImage(Image.open("3.png"))
my_image4=ImageTk.PhotoImage(Image.open("4.png"))
my_image5=ImageTk.PhotoImage(Image.open("5.png"))
my_image6=ImageTk.PhotoImage(Image.open("6.png"))
my_image9=ImageTk.PhotoImage(Image.open("9.png"))
#image list
image_list=[my_image1,my_image2,my_image3,my_image4,my_image5,my_image6,my_image9 ]
#function to display
def forward(image_number):
    global my_label_image
    global button_forward
    global button_backward
    my_label_image.grid_forget()
    my_label_image=Label(image=image_list[image_number-1])
    button_forward=Button(win,text=">>",command=lambda: forward(image_number+1))#recusive function
    button_backward=Button(win,text="<<",command=lambda: backward(image_number-1))  
    #to disable the forward button when the last image is reached
    if image_number==len(image_list):
        button_forward=Button(win,text=">>",state=DISABLED)
    my_label_image.grid(row=0,column=0,columnspan=3)   
    button_backward.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    #status bar
    status=Label(win,text="Image "+str(image_number)+" of "+str(len(image_list)))
    status.grid(row=2,column=2,columnspan=3,sticky=W+E) 
def backward(image_number):
    global my_label_image
    global button_forward
    global button_backward
    my_label_image.grid_forget()
    my_label_image=Label(image=image_list[image_number-1])
    button_forward=Button(win,text=">>",command=lambda: forward(image_number+1))
    button_backward=Button(win,text="<<",command=lambda: backward(image_number-1))  
    #to disable the forward button when the last image is reached
    if image_number==1:
        button_forward=Button(win,text=">>",state=DISABLED)
    my_label_image.grid(row=0,column=0,columnspan=3)   
    button_backward.grid(row=1,column=0)
    button_forward.grid(row=1,column=2) 
    #status bar
    status=Label(win,text="Image "+str(image_number)+" of "+str(len(image_list)))  
    status.grid(row=2,column=2,columnspan=3,sticky=W+E)  
#status bar
status=Label(win,text="Image 1 of "+str(len(image_list)))   
#label to display the image
my_label_image=Label(image=my_image1)
#button to quit the window
button_quit=Button(win,text="Exit",command=win.quit,bd=5,fg="red",bg="black",font=("Bold",16),relief=RAISED,activebackground="red",activeforeground="black")
#forward button
button_forward=Button(win,text=">>",command=lambda: forward(2),bd=5,fg="red",bg="black",font=("Bold",16),relief=RAISED,activebackground="red",activeforeground="black")
button_backward=Button(win,text="<<",command=backward,state=DISABLED,bd=5,fg="red",bg="black",font=("Bold",16),relief=RAISED ,activebackground="red",activeforeground="black")
#adding the buttons to the window
status.grid(row=2,column=2,columnspan=3,sticky=W+E)
my_label_image.grid(row=0,column=0,columnspan=3)
button_quit.grid(row=1,column=1)    
button_backward.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
#looping the window
win.mainloop()  