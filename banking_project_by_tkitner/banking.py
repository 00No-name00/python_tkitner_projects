from tkinter import *
from tkinter import messagebox

bank=Tk()
bank.title("Gitbank")
bank.geometry("905x613")

#adding the background image
renderer=PhotoImage(file="background.png")
bground=Label(bank,image=renderer)
bground.place(x=0,y=0)




#using transparracy
bank.wm_attributes('-transparentcolor',"grey")

def adding_labels():
    label1=Label(bank,text="Annual Rate : ",bg="grey",fg="white",font=10)
    label1.place(x=100,y=200)
    
    label2=Label(bank,text="Number Of Payments : ",bg="grey",fg="white",font=10)
    label2.place(x=100,y=250)

    label3=Label(bank,text="Loan principle : ",bg="grey",fg="white",font=10)
    label3.place(x=100,y=300)

    label4=Label(bank,text="Monthly Payment : ",bg="grey",fg="white",font=10)
    label4.place(x=100,y=350)

    label5=Label(bank,text="Remaining Loan : ",bg="grey",fg="white",font=10)
    label5.place(x=100,y=400)
    


    welcome_label1 =Label(bank,text="Welcome To GitBank",font=50,bg="grey",fg="#0066ff")
    welcome_label1.place(x=300,y=20)
    welcome_label1 =Label(bank,text="Transparacy is our motto",bg="grey",fg="#0099ff")
    welcome_label1.place(x=320,y=50)

    return

def create_entry():
    global entry_label1,entry_label2,entry_label3,entry_label4,entry_label5
    entry_label1=Entry(bank,borderwidth=5)
    entry_label1.place(x=500,y=200)
    
    entry_label2=Entry(bank,borderwidth=5)
    entry_label2.place(x=500,y=250)
    
    entry_label3=Entry(bank,borderwidth=5)
    entry_label3.place(x=500,y=300)

    entry_label4=Entry(bank,borderwidth=5)
    entry_label4.place(x=500,y=350)

    entry_label5=Entry(bank,borderwidth=5)
    entry_label5.place(x=500,y=400)

    return 



def create_button():
    def calc_function():
        final_calculation=float(float(float(entry_label4.get())*float(float(1-float(1+float(float(float(entry_label1.get())/float(entry_label3.get())))))))/float(float(entry_label1.get())/float(entry_label2.get())))+float(entry_label5.get())

        messagebox.showinfo("RESULT !!","the remaining loan  is "+str(final_calculation))
        return
    def del_functions():
        create_entry()
        return
    def quit_function():
        bank.destroy()
        return



    calc_button=Button(bank,text="submit",font=50,command=calc_function,padx=40,pady=20)
    calc_button.place(x=500,y=500)
    del_button=Button(bank,text="clear",font=50,command=del_functions,padx=40,pady=20)
    del_button.place(x=100,y=500)
    quit_button=Button(bank,text="Quit",font=50,command=quit_function,padx=40,pady=20)
    quit_button.place(x=300,y=520)

    return








adding_labels()
create_entry()
create_button()


bank.mainloop()