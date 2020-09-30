from tkinter import *
import math


root = Tk()
root.title('Calculator')

# get the user input and place it in the textfield

i = 0


def get_variables(num):
    global i
    Input_text_field.insert(i, num)
    i += 1


def calculate():
    entire_string = Input_text_field.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        Result_text_field.insert(0, result)
    except Exception:
        clear_all()

        Result_text_field.insert(0, "Error")


def get_operation(operator):
    global i
    length = len(operator)
    Input_text_field.insert(i, operator)
    i += length


def clear_all():
    Input_text_field.delete(0, END)
    Result_text_field.delete(0, END)


def Result():
    entire_string = Input_text_field.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        return result

    except Exception:
        clear_all()
        Result_text_field.insert(0, "Error")


def factorial():
    num = int(Result())
    ans = 1
    for i in range(1, num + 1):
        ans *= i
    Result_text_field.insert(0, ans)


def undo():
    entire_string = Input_text_field.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
from tkinter import *
import math


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        # elif ((scvalue.get()).count("pow") > 0):


        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    elif text == "x^2":
        if scvalue.get().isdigit():
            val = int(scvalue.get())

            avi = math.pow(val, 2)
            scvalue.set(avi)
            screen.update()
        else:
            try:
                value = eval(screen.get())
                val=int(value)
            except Exception as e:
                print(e)
                value = "Error"
            avi = math.pow(val,2)
            scvalue.set(avi)
            screen.update() 

    elif text == "x^3":
        if scvalue.get().isdigit():
            val = int(scvalue.get())

            avi = math.pow(val, 3)
            scvalue.set(avi)
            screen.update()
        else:
            try:
                value = eval(screen.get())
                val = int(value)
            except Exception as e:
                print(e)
                value = "Error"
            avi = math.pow(val, 3)
            scvalue.set(avi)
            screen.update()

    elif text == "sqrt":
        value = eval(screen.get())
        nw = math.sqrt(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()

    elif text == "sin":
        value = eval(screen.get())
        value1 = math.radians(value)
        nw = math.sin(value1)
        # print(nw)
        scvalue.set(nw)
        screen.update()

    elif text == "cos":
        value = eval(screen.get())
        value1 = math.radians(value)
        nw = math.cos(value1)
        # print(nw)
        scvalue.set(nw)
        screen.update()

    elif text == "tan":
        value = eval(screen.get())
        value1 = math.radians(value)
        nw = math.tan(value1)
        # print(nw)
        scvalue.set(nw)
        screen.update()
    
    elif text == "n!":
        value = eval(screen.get())
        nw = math.factorial(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()

    elif text == "pi":
        value = scvalue.get()
        v = "3.141592653589"
        nw= value + v
        scvalue.set(nw)
        screen.update()
       

    elif text == "cut":
        value = scvalue.get()
        l = len(value)
        nw = value[:l-1]
        scvalue.set(nw)
        screen.update()
    
    elif text == "log":
        value = eval(screen.get())
        nw = math.log10(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()

    elif text == "exp":
        value = eval(screen.get())
        nw = math.exp(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()

    elif text == "e":
        value = scvalue.get()
        v = "2.718281"
        nw = value + v
        scvalue.set(nw)
        screen.update()

    elif text == "log 2":
        value = eval(screen.get())
        nw = math.log2(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()
    
    elif text == "round":
        value = eval(screen.get())
        nw = round(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()  

    elif text == "isin":
        value = eval(screen.get())
        nw = math.degrees(math.asin(value))
        # print(nw)
        scvalue.set(nw)
        screen.update()    
    elif text == "icos":
        value = eval(screen.get())
        nw = math.degrees(math.acos(value))
        # print(nw)
        scvalue.set(nw)
        screen.update()    
    elif text == "itan":
        value = eval(screen.get())
        nw = math.degrees(math.atan(value))
        # print(nw)
        scvalue.set(nw)
        screen.update()    
    elif text == "deg":
        value = eval(screen.get())
        nw = math.degrees(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()    
    elif text == "abs":
        value = eval(screen.get())
        nw = math.fabs(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()    
    elif text == "gamma":
        value = eval(screen.get())
        nw = math.gamma(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()    

    elif text=="trunc":
        value = eval(screen.get())
        nw = math.trunc(value)
        # print(nw)
        scvalue.set(nw)
        screen.update()  



    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.minsize(450,395)
root.maxsize(450,395)
root.title("manish's calculator")
root.configure(bg="darkgrey")

# root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 13 bold")
screen.pack(fill=X, ipadx=8,ipady=15, pady=10, padx=10)

def button1(a):
    b = Button(f, text=""+a, font="lucida 10 bold", height=2,width=8, relief=FLAT, activebackground="darkgrey",bg="lightgrey")
    b.pack(side=LEFT, padx=1, pady=1)
    b.bind("<Button-1>", click)


def button2(a):
    b = Button(f, text=""+a, font="lucida 10 bold", height=2, width=8,fg="black",activebackground="burlywood")
    b.pack(side=LEFT, padx=1, pady=1)
    b.bind("<Button-1>", click)

f = Frame(root,bg="darkgrey")
button1("exp")
button1("x^2")
button1("sin")
button1("cos")
button1("tan")
button1("rad")
f.pack()

f = Frame(root,bg="darkgrey")
button1("isin")
button1("icos")
button1("itan")
button1("deg")
button1("abs")
button1("gamma")
f.pack()

f = Frame(root,bg="darkgrey")
button1("round")
button1("log")
button1("cut")
button1("C")
button1("%")
button1("+")
f.pack()

f = Frame(root,bg="darkgrey")
button1("log 2")
button1("pi")
button2("9")
button2("8")
button2("7")
button1("-")
f.pack()

f = Frame(root,bg="darkgrey")
button1("e")
button1("n!")
button2("6")
button2("5")
button2("4")
button1("*")
f.pack()

f = Frame(root,bg="darkgrey")
button1("x^3")
button1("sqrt")
button2("3")
button2("2")
button2("1")
button1("/")
f.pack()

f = Frame(root,bg="darkgrey")
button1("trunc")
button1("(")
button1(")")
button2("0")
button1(".")
button1("=")
f.pack()

root.mainloop()
