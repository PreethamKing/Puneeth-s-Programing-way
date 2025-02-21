import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from math import sqrt,sin,cos,cosh,sinh

#creating main window
root = tk.Tk()
root.title("Main Page")
bg_colour = "light blue"
fg_colour = "black"

#main window
def open_unit(unit_number):
    win = tk.Toplevel(root)
    win.title(f"Unit {unit_number}")
    bg_colour = "light blue"
    fg_colour = "black"
    
    # For question
    if unit_number==1:
        # Disable the button for the current unit
        button_dec[unit_number].config(state=tk.DISABLED)
        #for question
        frame_question = LabelFrame(win, text="Question", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
        frame_question.place(x=0, y=0)
        question_text = "Two forces are applied to the construction bracket as shown. Determine the angle which makes the resultant of the two forces vertical.    \n Determine the magnitude R of the resultant."
        label_question = Label(frame_question, text=question_text, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
        label_question.pack(side=TOP, fill=X)
        # For image
        frame_image = LabelFrame(win, text="Diagram", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
        frame_image.place(x=0, y=75)
        image_label = Label(frame_image, image=my_image)
        image_label.pack(side=TOP)
        
        # Entry frame
        entry_frame = LabelFrame(win, text="Enter the asked values", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
        entry_frame.place(x=865, y=75)
        
        #importing math
        import math
        from math import sin,cos,acos,asin,sqrt
        
        # Function to check if a string is a number
        def not_num(val):
            try:
                float(val)
                return True
            except ValueError:
                return False
            
        # Defining the function check    
        def click():
            # Retrieve the values from the Entry widgets
            force1 = entries["Force1"].get()
            angle1 = entries["β"].get()
            force2 = entries["Force2"].get()
            
            # Check if any value is zero
            if force1 == "0" or angle1 == "0" or force2 == "0":
                messagebox.showerror("Error", "Values can't be zero")
            # Check if the values are numerical
            elif not not_num(force1) or not not_num(angle1) or not not_num(force2):
                messagebox.showerror("Error", "INVALID input!")
            elif float(angle1)>360:
                messagebox.showerror("Error","Angle can't be greater than 360°!")
            else:
                messagebox.showinfo("Success", "Values submitted successfully")
                # Defining the function to show result
                def show_result(): 
                    #disable result button
                    submit_btn.config(state=DISABLED)           
                    # Result frame
                    global result
                    result = LabelFrame(win, text="Result", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
                    result.place( x=250,y=70)
                    Force1_val = "F₁ : " + force1 + " N"
                    Force2_val = "F₂ : " + force2 + " N"
                    Angle1_val = "β  : " + angle1 + "°"
                    unknown_var="ϴ = ?"
                    Force1x_val="F₁ₓ = F₁cosβ"             
                    Force1x_mag="= "+force1+"cos"+(angle1)+"°"
                    Angle1=math.radians(float(angle1))
                    prod=float(force1)*(math.cos(Angle1))
                    force1x_mag="= "+str(format(prod,".2f"))
                    Force2x_val="F₂ₓ = F₂cosϴ"
                    Force2x_mag="= "+force2+"cosϴ"
                    ResultantforceX_val="Rₓ= F₁ₓ - F₂ₓ (along x-axis)\n ⇒ Rₓ= 0"
                    ResultantforceX_mag="0 ="+Force1x_mag+"-"+Force2x_mag
                    #solving for theta
                    try:
                        inter_val = float(format(prod, ".2f")) / float(force2)
                        if -1 <= inter_val <= 1:
                            result_ang_radian = math.acos(inter_val)
                            result_ang_degree = format(math.degrees(result_ang_radian), ".2f")
                            result_angle = "⇒ ϴ = " + str(result_ang_degree) + "°"
                        else:
                            result_angle = "Invalid value for cosϴ"
                    except ValueError:
                            result_angle = "Error in calculating ϴ"
                    #solve for R---> along y axis
                    inter_val = float(format(prod, ".2f")) / float(force2)
                    result_ang_radian = math.acos(inter_val)
                    result_ang_degree = format(math.degrees(result_ang_radian), ".2f")
                    Force1y_val="F₁ᵧ = F₁sinβ" 
                    Force1y_mag="= "+force1+"sin"+(angle1)+"°"           
                    prody=float(force1)*(math.sin(Angle1))
                    force1y_mag="= "+str(format(prody,".2f"))
                    Force2y_val="F₂ᵧ = F₂sinϴ"
                    Force2y_mag="= "+force2+"sin"+(result_ang_degree)+"°"
                    prod2y=float(force2)*(math.sin(float(result_ang_radian)))
                    force2y_mag="= "+str(format(prod2y,".2f"))
                    Resultantforcey_val="Rᵧ = -F₁ᵧ - F₂ᵧ "
                    Resultantforcey_mag="= "+"-"+force1+"sin"+angle1+"°"+"-"+force2+"sin"+result_ang_degree+"°"
                    var=format((prody+prod2y),".2f")
                    result_fy="⇒"+"Rᵧ = "+"-"+str(var)
                    
                    #given values
                    lab_force1 = Label(result, text=Force1_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force1.pack(side=TOP)
                    lab_angle1 = Label(result, text=Angle1_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_angle1.pack(side=TOP)
                    lab_force2 = Label(result, text=Force2_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force2.pack(side=TOP)
                    lab_unknown = Label(result, text=unknown_var, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_unknown.pack(side=TOP)
                    
                    #for x component of force-1
                    lab_force1x = Label(result, text=Force1x_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force1x.pack(side=TOP)
                    lab_force1xM = Label(result, text=Force1x_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force1xM.pack(side=TOP)
                    lab_force1xm = Label(result, text=force1x_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force1xm.pack(side=TOP)
                    
                    #for x component of force-2
                    lab_force2x = Label(result, text=Force2x_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force2x.pack(side=TOP)
                    lab_force2xM = Label(result, text=Force2x_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force2xM.pack(side=TOP)
                    
                    #for resultant of x-component
                    lab_resultant=Label(result, text=ResultantforceX_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_resultant.pack(side=TOP)
                    lab_resultant_mag=Label(result, text=ResultantforceX_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_resultant_mag.pack(side=TOP)
                    
                    #for result {thetha}
                    lab_inter_var=Label(result, text=inter_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_inter_var.pack(side=TOP)
                    lab_result_angle=Label(result, text=result_angle, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_result_angle.pack(side=TOP)
                     
                    #another frame for result
                    global result_
                    result_=LabelFrame(win,text="Result",bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
                    result_.place(x=520,y=60)
                    
                    #for y component of force-1
                    lab_force1y = Label(result_, text=Force1y_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force1y.pack(side=TOP)
                    lab_force1yM = Label(result_, text=Force1y_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force1yM.pack(side=TOP)
                    lab_force1ym = Label(result_, text=force1y_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force1ym.pack(side=TOP)
                    
                    #for y component of force-2
                    lab_force2y = Label(result_, text=Force2y_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force2y.pack(side=TOP)
                    lab_force2yM = Label(result_, text=Force2y_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force2yM.pack(side=TOP)
                    lab_force2ym = Label(result_, text=force2y_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_force2ym.pack(side=TOP)
                    
                    #for resultant of y{Rᵧ}
                    lab_resultanty=Label(result_, text=Resultantforcey_val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_resultanty.pack(side=TOP)
                    lab_resultanty_mag=Label(result_, text=Resultantforcey_mag, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_resultanty_mag.pack(side=TOP)
                    
                    #for result
                    lab_result=Label(result_, text=result_fy, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_result.pack(side=TOP) 
                                
                # Call the show_result function
                result_btn=Button(entry_frame,text="Result",font=("Bold",16),bd=5,relief=GROOVE,command=show_result)
                result_btn.grid(row=3,column=1)
                
        #to display free body diagram
        def fbd():
            fbd_label=Label(frame_image,image=fbd_image)
            fbd_label.pack(side="bottom")      
                  
        # Assuming entries dictionary and variable list are already defined
        global entries
        entries = {}
        variable = ["Force1", "β", "Force2"]
        
        row_var = 0
        col_var = 0
        for val in variable:
            lab = Label(entry_frame, text=val, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab.grid(row=row_var, column=col_var)
            row_var += 1
            
        row_var = 0
        col_var = 1
        for val in variable:
            ent = Entry(entry_frame, width=15, font=("Bold", 16), bd=5, relief=GROOVE)
            ent.grid(row=row_var, column=col_var)
            entries[val] = ent
            row_var += 1
            
        #defining clear
        def clear():
            variable=["Force1","β","Force2"]
            for var in variable:
                value=entries[var]
                value.delete(0,END)
            result.place_forget()
            result_.place_forget()
            submit_btn.config(state=NORMAL)
        
        #defining on_closing
        # Re-enable the button when the Toplevel window is closed
        def on_closing():
            button_dec[unit_number].config(state=tk.NORMAL)
            win.destroy()
            
        submit_btn=Button(entry_frame,text="Click to submit value",font=("Bold",16),bd=5,relief=GROOVE,command=click)
        submit_btn.grid(row=3,column=0)
        
        quit_btn=Button(entry_frame,text="Quit",command=on_closing,font=("Bold",16),bd=5,relief=GROOVE)
        quit_btn.grid(row=4,column=0)
        
        clear_btn=Button(entry_frame,text="Clear",command=clear,font=("Bold",16),bd=5,relief=GROOVE)
        clear_btn.grid(row=4,column=1)
        
        fbd_btn=Button(entry_frame,text="FBD",command=fbd,font=("Bold",16),bd=5,relief=GROOVE)
        fbd_btn.grid(row=5,column=0)
    elif unit_number==2:
        bg_colour="light blue"  
        fg_colour="black"
        
        # Disable the button for the current unit
        button_dec[unit_number].config(state=tk.DISABLED)
        
        #for question 
        frame_question1=LabelFrame(win,text="Question",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        frame_question1.place(x=0,y=0)
        label_question1 = Label(frame_question1, text="When on level ground, the car is placed on four individual scales-one under each tire. \nThe scale readings are Nf at each front wheel and Nr at each rear wheel. Determine the x-coordinate of the mass center G and the mass\n of the car", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
        label_question1.pack(side=TOP,fill=X)
        
        #for image
        frame_image1=LabelFrame(win,text="Diagram",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        frame_image1.place(x=0,y=95)
        image_label1=Label(frame_image1,image=my_image1)
        image_label1.pack(side=TOP)
        
        #entry frame
        entry_frame1=LabelFrame(win,text="Enter the asked values",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        entry_frame1.place(x=865,y=95)
        
        #importing math
        import math
        from math import sin,cos,acos,asin,sqrt
        
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
            
        #defining on_closing
        # Re-enable the button when the Toplevel window is closed
        def on_closing():
            button_dec[unit_number].config(state=tk.NORMAL)
            win.destroy()
            
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
                    result1 = LabelFrame(win, text="Result", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
                    result1.place(x=400,y=95)
                    Nf_val = "Nf : " + Nf + " N"
                    Nr_val = "Nr : " + Nr + " N"
                    unknown_var_x="x = ?"
                    unknown_var_wegiht="m = ?"
                    force_y="∑Fᵧ = 0"
                    result_solve="= 2Nf +2Nr - W"
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
        
        quit_btn1=Button(entry_frame1,text="Quit",command=on_closing,font=("Bold",16),bd=5,relief=GROOVE)
        quit_btn1.grid(row=4,column=0)
        
        clear_btn1=Button(entry_frame1,text="Clear",command=clear1,font=("Bold",16),bd=5,relief=GROOVE)
        clear_btn1.grid(row=4,column=1)
        
        fbd_btn1=Button(entry_frame1,text="FBD",command=fbd1,font=("Bold",16),bd=5,relief=GROOVE)
        fbd_btn1.grid(row=5,column=0)
        
        variable1=["Nf","Nr"]
        global entries1
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
            
    elif unit_number==3:
        bg_colour="light blue"  
        fg_colour="black"
        # Disable the button for the current unit
        button_dec[unit_number].config(state=tk.DISABLED)
        #for question 
        frame_question2=LabelFrame(win,text="Question",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        frame_question2.place(x=0,y=0)
        label_question2 = Label(frame_question2, text="                                                   Determine the reactions at A and B for the beam loaded as shown.                                                          ", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
        label_question2.pack(side=TOP,fill=X)
        
        #for image
        frame_image2=LabelFrame(win,text="Diagram",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        frame_image2.place(x=0,y=65)
        image_label2=Label(frame_image2,image=my_image2)
        image_label2.pack(side=TOP)
        
        #entry frame
        entry_frame2=LabelFrame(win,text="Enter the asked values",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        entry_frame2.place(x=865,y=65)
        
        # Function to check if a string is a number
        def not_num(val):
            try:
                float(val)
                return True
            except ValueError:
                return False
            
        #to display free body diagram
        def fbd2():
            fbd_label2=Label(frame_image2,image=fbd_image2)
            fbd_label2.pack(side="bottom")
            
        #defining clear    
        def clear2():
            variable2=["F1","F2"]
            for var in variable2:
                value=entries2[var]
                value.delete(0,END)
            result1.place_forget()
            submit_btn2.config(state=NORMAL)
            
        #defining on_closing
        # Re-enable the button when the Toplevel window is closed
        def on_closing():
            button_dec[unit_number].config(state=tk.NORMAL)
            win.destroy()
            
        def click2():
            # Retrieve the values from the Entry widgets
            F1 = entries2["F₁"].get()
            F2 = entries2["M₁"].get()
                # Check if any value is zero
            if F1 == "0" or F2 == "0":
                messagebox.showerror("Error", "Values can't be zero")
            # Check if the values are numerical
            elif not not_num(F1) or not not_num(F2) :
                messagebox.showerror("Error", "INVALID input!")
            else:
                messagebox.showinfo("Success", "Values submitted successfully")
                # Defining the function to show result
                def show_result(): 
                    #disable result button
                    submit_btn2.config(state=DISABLED) 
                    # Result frame
                    global result1
                    result1 = LabelFrame(win, text="Result", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
                    result1.place(x=375,y=65)
                    resultR1=format((float(F1)*4),".2f")
                    result_R1=f"R₁ = {F1} * 4 = {resultR1} KN" #
                    moment="M = "+ str(F2) +"KNm"#
                    momnent_Ma=f"∑Mₐ = 0 ⇒ {resultR1} * 2 - B * 4 = 0"
                    B=format((float(F2)+float(resultR1)*(6)/4),".2f")#
                    result_B=f"⇒ B = {B}"
                    Fx="∑Fₓ = 0 ⇒ Aₓ = 0"
                    Fy="∑Fᵧ = 0 ⇒ Aᵧ "+"+ B "+"- R₁ = 0"
                    FY=float(resultR1)-float(B)
                    result_Fy="⇒ Aᵧ ="+ str(FY)
                    #given
                    lab_R1= Label(result1, text=result_R1, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_R1.pack(side=TOP)
                    lab_M= Label(result1, text=moment, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_M.pack(side=TOP)
                    #data
                    lab_m= Label(result1, text=momnent_Ma, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_m.pack(side=TOP)
                    lab_B= Label(result1, text=result_B, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_B.pack(side=TOP)
                    lab_FX= Label(result1, text=Fx, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_FX.pack(side=TOP)
                    lab_FY= Label(result1, text=Fy, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_FY.pack(side=TOP)
                    lab_result_FY= Label(result1, text=result_Fy, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    lab_result_FY.pack(side=TOP)
                    
                # Call the show_result function
                result_btn2=Button(entry_frame2,text="Result",font=("Bold",16),bd=5,relief=GROOVE,command=show_result)
                result_btn2.grid(row=3,column=1)
                
        #to cheak result
        submit_btn2=Button(entry_frame2,text="Click to submit value",font=("Bold",16),bd=5,relief=GROOVE,command=click2)
        submit_btn2.grid(row=3,column=0)
        
        #for quit button
        quit_btn2=Button(entry_frame2,text="Quit",command=on_closing,font=("Bold",16),bd=5,relief=GROOVE)
        quit_btn2.grid(row=4,column=0)
        
        #for clear button
        clear_btn2=Button(entry_frame2,text="Clear",command=clear2,font=("Bold",16),bd=5,relief=GROOVE)
        clear_btn2.grid(row=4,column=1)
        
        #for fbd
        fbd_btn2=Button(entry_frame2,text="FBD",command=fbd2,font=("Bold",16),bd=5,relief=GROOVE)
        fbd_btn2.grid(row=5,column=0)
        
        global entries2
        variable2=["F₁","M₁"]
        entries2={}
        
        row_var2 = 0
        col_var2 = 0
        for var in variable2:
            lab = Label(entry_frame2, text=var, bg=bg_colour, fg=fg_colour, font=("Bold", 16))
            lab.grid(row=row_var2, column=col_var2)
            row_var2 += 1
            
        row_var2 = 0
        col_var2 = 1
        for val in variable2:
            ent = Entry(entry_frame2, width=15, font=("Bold", 16), bd=5, relief=GROOVE)
            ent.grid(row=row_var2, column=col_var2)
            entries2[val] = ent
            row_var2 += 1
            
    else :
        import math
        from math import cos,sin,acos,asin
        degree_to_radians=math.radians(20)
        cos_val=math.cos(degree_to_radians)
        sin_val=math.sin(degree_to_radians)
        bg_colour="light blue"  
        fg_colour="black"
        
        # Disable the button for the current unit
        button_dec[unit_number].config(state=tk.DISABLED)
        
        #for question 
        frame_question3=LabelFrame(win,text="Question",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        frame_question3.place(x=0,y=0)
        label_question3=Label(frame_question3,text="The 80-kg exerciser is repeated from Prob. 3/23. The tension TN is developed against an exercise machine (not shown) as he is about    \n to begin a biceps curl. Determine the minimum coefficient of static friction that must exist \nbetween his shoes and the floor if he is not to slip.",bg=bg_colour,fg=fg_colour,font=("Bold",16))
        label_question3.pack(side=TOP,fill=X)
        
        #for image frame
        frame_image3=LabelFrame(win,text="Diagram",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        frame_image3.place(x=0,y=95)
        
        #image as lable
        image_label3=Label(frame_image3,image=my_image3)
        image_label3.pack(side=TOP)
        
        #entry frame
        entry_frame3=LabelFrame(win,text="Enter the asked values",bg=bg_colour,fg=fg_colour,bd=5,relief=GROOVE,font=("Bold",18))
        entry_frame3.place(x=865,y=110)
        
        #to cheak is input is number or not
        def not_num(val):
            try:
                float(val)
                return True
            except ValueError:
                return False
            
        #to display free body diagram
        def fbd3():
            fbd_label1=Label(frame_image3,image=fbd_image3)
            fbd_label1.pack(side="bottom")
            
        #defining on_closing
        # Re-enable the button when the Toplevel window is closed
        def on_closing():
            button_dec[unit_number].config(state=tk.NORMAL)
            win.destroy()
            
        #defining clear    
        def clear3():
            tension_ery.delete(0,END)
            result3.place_forget()
            submit_btn3.config(state=NORMAL)
        def click3():
            # Retrieve the values from the Entry widgets
            F1 = tension_ery.get()
                # Check if any value is zero
            if F1 == "0" :
                messagebox.showerror("Error", "Values can't be zero")
            # Check if the values are numerical
            elif not not_num(F1)  :
                messagebox.showerror("Error", "INVALID input!")
            else:
                messagebox.showinfo("Success", "Values submitted successfully")
                
                # Defining the function to show result
                def show_result3(): 
                    #disable result button
                    submit_btn3.config(state=DISABLED) 
                    # Result frame
                    global result3
                    result3 = LabelFrame(win, text="Result", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18))
                    result3.place(x=375,y=100)
                    fx_label= Label(result3, text=f"∑Fₓ = 0", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    fx_label.pack(side=TOP)
                    t_label= Label(result3, text=f"T = {F1} N", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    t_label.pack(side=TOP)
                    fs_label= Label(result3, text=f"F = ?", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    fs_label.pack(side=TOP)
                    t_val_label= Label(result3, text=f"⇒Tcos20° - F = 0", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    t_val_label.pack(side=TOP)
                    F=format((float(F1)*(cos_val)),".2f")
                    f_mag_label= Label(result3, text=f"F = {F1}cos20° = {format((float(F1)*(cos_val)),".2f")}", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    f_mag_label.pack(side=TOP)
                    fy_label= Label(result3, text=f"∑Fᵧ = 0 ⇒ N - W + Tsin20° =0", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    fy_label.pack(side=TOP)
                    N=format((80*9.81)-(float(F1)*sin_val),".2f")
                    fx_label= Label(result3, text=f"N=((80)(9.81))-{(F1)}sin20° = {format((80*9.81)-(float(F1)*sin_val),".2f")}", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    fx_label.pack(side=TOP)
                    f_label= Label(result3, text=f"F = μN", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    f_label.pack(side=TOP)
                    mue=format(float(F)/float(N),".2f")
                    f_mag_label= Label(result3, text=f"μ = {F}/{N} = {mue}", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
                    f_mag_label.pack(side=TOP)
                    
                #button to activate show_result
                result_btn=Button(entry_frame3,text="Result",font=("Bold",16),bd=5,relief=GROOVE,command=show_result3)
                result_btn.grid(row=3,column=1)
                
        #submit button
        submit_btn3=Button(entry_frame3,text="Click to submit value",font=("Bold",16),bd=5,relief=GROOVE,command=click3)
        submit_btn3.grid(row=3,column=0)
        
        #quit button
        quit_btn3=Button(entry_frame3,text="Quit",command=on_closing,font=("Bold",16),bd=5,relief=GROOVE)
        quit_btn3.grid(row=4,column=0)
        
        #after quit
        
        #clear button
        clear_btn3=Button(entry_frame3,text="Clear",command=clear3,font=("Bold",16),bd=5,relief=GROOVE)
        clear_btn3.grid(row=4,column=1)
        
        #for fbd
        fbd_btn3=Button(entry_frame3,text="FBD",command=fbd3,font=("Bold",16),bd=5,relief=GROOVE)
        fbd_btn3.grid(row=5,column=0)
        
        #input name
        tension_lab=Label(entry_frame3, text="Tension", bg=bg_colour, fg=fg_colour, font=("Bold", 16))
        tension_lab.grid(row=0, column=0)
        
        #entry window
        global tension_ery
        tension_ery=Entry(entry_frame3, width=15, font=("Bold", 16), bd=5, relief=GROOVE)
        tension_ery.grid(row=0, column=1)
        
        #looping sub window
        win.mainloop()
        

# Load images
my_image = ImageTk.PhotoImage(Image.open("Statics.png"))
fbd_image = ImageTk.PhotoImage(Image.open("fbds2.png"))
my_image1=ImageTk.PhotoImage(Image.open("Statics1.png"))
fbd_image1=ImageTk.PhotoImage(Image.open("fbds1.png"))
my_image2=ImageTk.PhotoImage(Image.open("Statics2.png"))
fbd_image2=ImageTk.PhotoImage(Image.open("fbds3.png"))
my_image3=ImageTk.PhotoImage(Image.open("Statics3.png"))
fbd_image3=ImageTk.PhotoImage(Image.open("fbds4.png"))

# Create buttons for each unit
button_dec={}
for i in range(1,5):
    button = tk.Button(root, text=f"Unit {i}", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18), command=lambda i=i: open_unit(i))
    button.pack(pady=10)
    button_dec[i] = button
    
#creat quit button
closebutton = tk.Button(root, text="Close", bg=bg_colour, fg=fg_colour, bd=5, relief=GROOVE, font=("Bold", 18), command=root.quit)
closebutton.pack(pady=10)

#looping window
root.mainloop()