# Clark Creations Simple Calculator
# Supports mouse input and keybaord input (pressing enter will give the result of the calculation)

from tkinter import *

root=Tk() #creates window
root.title("Clark Creations Simple Calculator") #sets the title of the window
root.configure(bg="#5B2333") #sets the background color of the window
root.geometry("370x510") #sets the size of the window
root.resizable(False, False) #prevents the window from being resized

e = Entry(root, width=35, borderwidth=3) #creates text box for user input

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #places the text box on the grid


def button_click(number): #def mean define a function, button_click is the name of the function, number is the parameter that we will pass in when we call the function
    e.insert(END, number) 


def button_clear():
    e.delete(0, END)

def button_add():
    e.insert(END, "+") #inserts the + symbol into the text box
    

def button_equal():
    result=eval(e.get())
    e.delete(0, END)
    e.insert(0, result) #inserts the result of the calculation into the text box
    equal_action = button_equal 

def button_subtract():
    e.insert(END, "-") #inserts the - symbol into the text box

def button_multiply():
    e.insert(END, "*") #inserts the * symbol into the text box
    
def button_divide():
    e.insert(END, "/") #inserts the / symbol into the text box
     


#Defining Buttons

button_1 = Button(root, text="1", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(1)) #creates button with text and padding
button_2 = Button(root, text="2", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(2))
button_3 = Button(root, text="3", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(3))
button_4 = Button(root, text="4", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(4))
button_5 = Button(root, text="5", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(5))
button_6 = Button(root, text="6", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(6))
button_7 = Button(root, text="7", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(7))
button_8 = Button(root, text="8", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(8))
button_9 = Button(root, text="9", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(9))
button_0 = Button(root, text="0", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command=lambda: button_click(0))
button_add = Button(root, text="+", font=("Avenir", 14), padx=39, pady=20, bg="light gray", fg="black", command= button_add)
button_equal = Button(root, text="=", font=("Avenir", 14), padx=91, pady=20, bg="light gray", fg="black", command= button_equal) 

button_clear = Button(root, text="Clear", font=("Avenir", 14), padx=79, pady=20, bg="light gray", fg="black", command = button_clear)

button_subtract = Button(root, text="-", font=("Avenir", 14), padx=41, pady=20, bg="light gray", fg="black", command= button_subtract)
button_multiply  = Button(root, text="*", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command= button_multiply)
button_divide  = Button(root, text="/", font=("Avenir", 14), padx=40, pady=20, bg="light gray", fg="black", command= button_divide)


e.bind("<Return>", lambda event: button_equal.invoke()) 

# Putting the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop() #keeps the window open until we close it.