from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import math
from math import sin,cos,tan,sqrt

win1=Tk()
my_image1=ImageTk.PhotoImage(Image.open("Statics1.png"))
fbd_image1=ImageTk.PhotoImage(Image.open("fbds1.png"))

win1.title("Statics")
bg_colour="light blue"  
fg_colour="black"
#for question 
frame_question1=LabelFrame(win1,text="Question",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
frame_question1.place(x=0,y=0)
label_question1 = Label(frame_question1, text="When on level ground, the car is placed on four individual scales-one under each tire. \nThe scale readings are Nf at each front wheel and Nr at each rear wheel. Determine the x-coordinate of the mass center G and the mass\n of the car", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
label_question1.pack(side=TOP,fill=X)
#for image
frame_image1=LabelFrame(win1,text="Diagram",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
frame_image1.place(x=0,y=95)
image_label1=Label(frame_image1,image=my_image1)
image_label1.pack(side=TOP)
#entry frame
entry_frame1=LabelFrame(win1,text="Enter the asked values",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
entry_frame1.place(x=865,y=95)
# Function to check if a string is a number
def not_num(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

#to display free body diagram
def fbd1():
    fbd_label1=Label(frame_image1,image=fbd_image1)
    fbd_label1.pack(side="bottom")
#defining clear    
def clear1():
    variable1=["Nf","Nr"]
    for var in variable1:
        value=entries1[var]
        value.delete(0,END)
    result1.place_forget()
    submit_btn1.config(state=NORMAL)
def click1():
    # Retrieve the values from the Entry widgets
    Nr = entries1["Nf"].get()
    Nf = entries1["Nr"].get()
        # Check if any value is zero
    if Nr == "0" or Nf == "0":
        messagebox.showerror("Error", "Values can't be zero")
    # Check if the values are numerical
    elif not not_num(Nr) or not not_num(Nf) :
        messagebox.showerror("Error", "INVALID input!")
    else:
        messagebox.showinfo("Success", "Values submitted successfully")
        # Defining the function to show result
        def show_result(): 
            #disable result button
            submit_btn1.config(state=DISABLED) 
            # Result frame
            global result1
            result1 = LabelFrame(win1, text="Result", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
            result1.place(x=400,y=95)
            Nf_val = "Nf : " + Nf + " N"
            Nr_val = "Nr : " + Nr + " N"
            unknown_var_x="x = ?"
            unknown_var_wegiht="m = ?"
            force_y="∑Fᵧ = 0"
            result_solve="2Nf +2Nr - W"
            result1__=format(2*(float(Nf)+float(Nr)),".2f")
            result_weight="⇒ W = "+str(result1__) + "N"
            result__mass=format((float(result1__)/9.81),".2f")
            st_mass="for mass divide wegiht from g{9.81}"
            result_mass="⇒ m = "+str(result__mass) +"Kg"
            Moment=str(result1__)+"x" + "+" + "-" "2"+str(Nr)+"(2640)"
            sol_x=format((2*float(Nr)*(2640))/float(result1__),".2f")
            result_x="x = "+str(sol_x)
            #given value
            lab_Nf = Label(result1, text=Nf_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_Nf.pack(side=TOP)
            lab_force2 = Label(result1, text=Nr_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_force2.pack(side=TOP)
            lab_unknown_x = Label(result1, text=unknown_var_x, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_unknown_x.pack(side=TOP)
            lab_unknown_weight = Label(result1, text=unknown_var_wegiht, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_unknown_weight.pack(side=TOP)
            #for fy=0
            lab_fy=Label(result1, text=force_y, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_fy.pack(side=TOP)
            #solve for w
            lab_sol=Label(result1, text=result_solve, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_sol.pack(side=TOP)
            #solve for m
            lab_st=Label(result1, text=st_mass, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_st.pack(side=TOP)
            lab_sol_mass=Label(result1, text=result_mass, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_sol_mass.pack(side=TOP)
            #result
            lab_result_w=Label(result1, text=result_weight, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab_result_w.pack(side=TOP)
            #for x coordinate
            lab_sum_m=Label(result1,text="∑Mf = 0",bg=bg_colour, fg=fg_colour, font=("Bold", 18))
            lab_sum_m.pack(side=TOP)
            lab_moment=Label(result1,text=Moment,bg=bg_colour, fg=fg_colour, font=("Bold", 18))
            lab_moment.pack(side=TOP)
            lab_result_x=Label(result1,text=result_x,bg=bg_colour, fg=fg_colour,  font=("Bold", 18))
            lab_result_x.pack(side=TOP)
            
            
            
        # Call the show_result function
        result_btn1=Button(entry_frame1,text="Result",font=("Bold",16),bd=5,relief=GROOVE,command=show_result)
        result_btn1.grid(row=3,column=1)
            
                       

submit_btn1=Button(entry_frame1,text="Click to submit value",font=("Bold",16),bd=5,relief=GROOVE,command=click1)
submit_btn1.grid(row=3,column=0)
quit_btn1=Button(entry_frame1,text="Quit",command=win1.quit,font=("Bold",16),bd=5,relief=GROOVE)
quit_btn1.grid(row=4,column=0)
clear_btn1=Button(entry_frame1,text="Clear",command=clear1,font=("Bold",16),bd=5,relief=GROOVE)
clear_btn1.grid(row=4,column=1)
fbd_btn1=Button(entry_frame1,text="FBD",command=fbd1,font=("Bold",16),bd=5,relief=GROOVE)
fbd_btn1.grid(row=5,column=0)

variable1=["Nf","Nr"]
entries1={}
row_var1 = 0
col_var1 = 0
for var in variable1:
    lab = Label(entry_frame1, text=var, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
    lab.grid(row=row_var1, column=col_var1)
    row_var1 += 1
row_var1 = 0
col_var1 = 1
for val in variable1:
    ent = Entry(entry_frame1, width=15, font=("Bold", 16), bd=5, relief=GROOVE)
    ent.grid(row=row_var1, column=col_var1)
    entries1[val] = ent
    row_var1 += 1
    
    




win1.mainloop()