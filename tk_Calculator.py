from tkinter import *
import parser

root = Tk()
root.configure(background="Black")
root.title("Calculator")
root.geometry("327x278")

#Get input and display in input field
i = 0
def get_input(num):
    global i
    display.insert(i,num)

    i+=1

def factorial():
    global i
    inp = int(display.get())
    display.insert(i,inp)
    i+=1
    clear_all()
    fact = 1
    num = inp
    for x in range(inp):
        fact = fact * num
        num = num - 1

    display.insert(0,int(fact))


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()

def get_operator(operator):
    global i
    length = len(operator)
    display.insert(0,operator)
    i+=length

def clear_all():
    display.delete(0,END)

def backspace():
    string = display.get()
    if len(string):
        newstring = string[:-1]
        clear_all()
        display.insert(0,newstring)
    else:
        clear_all()


#adding the input field

display = Entry(root,relief=RIDGE, bd=18, bg="black", fg="white", font = ("Digital-7",20, "bold"))
display.grid(row=1, rowspan =1, columnspan=6, ipady = 6, ipadx= 6, sticky=W+E)

#adding the numbers button

Button(root, text="1", command= lambda : get_input(1),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white", padx = 10, pady = 4, font = ("Arial", 12, "bold")).grid(row=2, column=0)
Button(root, text="2", command= lambda : get_input(2),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white", padx = 10, pady = 4, font = ("Arial", 12, "bold")).grid(row=2, column=1)
Button(root, text="3", command= lambda : get_input(3),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 4, font = ("Arial", 12, "bold")).grid(row=2, column=2)

Button(root, text="4", command= lambda : get_input(4),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=3, column=0)
Button(root, text="5", command= lambda : get_input(5),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=3, column=1)
Button(root, text="6", command= lambda : get_input(6),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=3, column=2)

Button(root, text="7", command= lambda : get_input(7),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=4, column=0)
Button(root, text="8", command= lambda : get_input(8),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=4, column=1)
Button(root, text="9", command= lambda : get_input(9),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=4, column=2)

#adding the operations button

Button(root, text="AC", command= lambda : clear_all(),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 3, pady = 5, font = ("Arial", 13, "bold")).grid(row=5, column=0)
Button(root, text="0", command= lambda : get_input(0),relief=RIDGE,
       bg = "Black", bd = 7, padx = 10, fg = "white",pady = 5, font = ("Arial", 12, "bold")).grid(row=5, column=1)
Button(root, text="=", command= lambda : calculate(),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white", padx = 10, pady = 5, font = ("Arial", 13, "bold")).grid(row=5, column=2)

Button(root, text="+", command= lambda : get_input("+"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white", padx = 8, pady = 4, font = ("Arial", 12, "bold")).grid(row=2, column=3)
Button(root, text="-", command= lambda : get_input("-"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=3, column=3)
Button(root, text="*", command= lambda : get_input("*"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=4, column=3)
Button(root, text="/", command= lambda : get_input("/"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 10, pady = 5, font = ("Arial", 12, "bold")).grid(row=5, column=3)

#adding Extra operators button

Button(root, text="pi", command= lambda : get_input("*3.14"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 8, pady = 4, font = ("Arial", 12, "bold")).grid(row=2, column=4)
Button(root, text="%", command= lambda : get_input("%"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 7, pady = 5, font = ("Arial", 12, "bold")).grid(row=3, column=4)
Button(root, text="(", command= lambda : get_input("("),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 12, pady = 5, font = ("Arial", 12, "bold")).grid(row=4, column=4)
Button(root, text="exp", command= lambda : get_input("**"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 1, pady = 5, font = ("Arial", 12, "bold")).grid(row=5, column=4)

Button(root, text="<-", command= lambda : backspace(),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 8, pady = 4, font = ("Arial", 12, "bold")).grid(row=2, column=5)
Button(root, text="x!", command= lambda : factorial(),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 8, pady = 5, font = ("Arial", 12, "bold")).grid(row=3, column=5)
Button(root, text=")", command= lambda : get_input(")"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 12, pady = 5, font = ("Arial", 12, "bold")).grid(row=4, column=5)
Button(root, text="^2", command= lambda : get_input("**2"),relief=RIDGE,
       bg = "Black", bd = 7, fg = "white",padx = 5, pady = 5, font = ("Arial", 12, "bold")).grid(row=5, column=5)
root.resizable(width = False, height = False)
root.mainloop()