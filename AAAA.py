from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("320x420")
root.config(bg="#1e1e2f")

root.resizable(0, 0)

# Variables
equa = ""
equation = StringVar()

# Display
display = Label(root, textvariable=equation,
                font=("Arial", 20),
                bg="#2d2d44",
                fg="white",
                width=18,
                height=2,
                anchor = "e")

equation.set("0")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Functions
def btnPress(num):
    global equa
    equa += str(num)
    equation.set(equa)

def EqualPress():
    global equa
    try:
        total = str(eval(equa))
        equation.set(total)
        equa = total
    except:
        equation.set("Error")
        equa = ""

def ClearPress():
    global equa
    equa = ""
    equation.set("0")

# Button style function
def create_btn(text, row, col, cmd, bg="#3a3a5a"):
    Button(root, text=text,
           command=cmd,
           font=("Arial", 14, "bold"),
           bg=bg,
           fg="white",
           activebackground="#5a5a8a",
           width=5,
           height=2,
           relief="ridge").grid(row=row, column=col, padx=5, pady=5)

# Buttons
create_btn("7", 1, 0, lambda: btnPress(7))
create_btn("8", 1, 1, lambda: btnPress(8))
create_btn("9", 1, 2, lambda: btnPress(9))
create_btn("/", 1, 3, lambda: btnPress("/"), "#ff9500")

create_btn("4", 2, 0, lambda: btnPress(4))
create_btn("5", 2, 1, lambda: btnPress(5))
create_btn("6", 2, 2, lambda: btnPress(6))
create_btn("*", 2, 3, lambda: btnPress("*"), "#ff9500")

create_btn("1", 3, 0, lambda: btnPress(1))
create_btn("2", 3, 1, lambda: btnPress(2))
create_btn("3", 3, 2, lambda: btnPress(3))
create_btn("-", 3, 3, lambda: btnPress("-"), "#ff9500")

create_btn("0", 4, 0, lambda: btnPress(0))
create_btn("C", 4, 1, ClearPress, "#ff3b30")
create_btn("=", 4, 2, EqualPress, "#34c759")
create_btn("+", 4, 3, lambda: btnPress("+"), "#ff9500")

root.mainloop()
