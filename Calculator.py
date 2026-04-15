from tkinter import *
import tkinter as tk




def buttonPress(num):

    global equation_text


    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        # Rounds to 5 decimal points to avoid innacuracies
        equation_text = str(float(eval(equation_text)).__round__(5))

        # Gets rid of decimal if none exists
        if (float(equation_text)%1 == 0):
            equation_text = equation_text[:equation_text.find(".")]
        else:
            pass


        equation_label.set(equation_text)
    except(SyntaxError):
        equation_label.set("SYNTAX ERROR")

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def add():
    global equation_text
    equation_text = equation_text + "+"
    equation_label.set(equation_text)

def subtract():
    global equation_text
    equation_text = equation_text + "-"
    equation_label.set(equation_text)

def multiply():
    global equation_text
    equation_text = equation_text + "*"
    equation_label.set(equation_text)

def divide():
    global equation_text
    equation_text = equation_text + "/"
    equation_label.set(equation_text)

def opposite():
    global equation_text
    try:
        if (str(eval(str(equation_text))).__contains__("-")):
            equation_text = str(eval(str(equation_text)))[1::]
        else:
            equation_text = "-" + str(eval(str(equation_text)))
        equation_label.set(equation_text)
    except (SyntaxError):
        equation_label.set("SYNTAX ERROR")

def decimal():
    global equation_text
    equation_text = equation_text + "."
    equation_label.set(equation_text)


# Create Window
window = tk.Tk()
window.title("Calculator by Abnel")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

# Create Number Display
label = Label(window, textvariable = equation_label,
              font = ('consolas', 20) , bg= "white", width = 24, height= 2 )
label.pack()

frame = Frame(window)
frame.pack()

# Create Buttons
# Numbers
button1 = Button(frame, text= 1, height= 4, width = 9, font= 35, command = lambda: buttonPress(1))
button1.grid(row = 1, column = 0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: buttonPress(2))
button2.grid(row=1, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: buttonPress(3))
button3.grid(row=1, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: buttonPress(4))
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: buttonPress(5))
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: buttonPress(6))
button6.grid(row=2, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: buttonPress(7))
button7.grid(row=3, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: buttonPress(8))
button8.grid(row=3, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: buttonPress(9))
button9.grid(row=3, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonPress(0))
button0.grid(row=4, column=1)

# Functions
buttonDiv = Button(frame, text="/", height=4, width=9, font=35, command=lambda:  divide())
buttonDiv.grid(row=0, column=3)

buttonMult = Button(frame, text="*", height=4, width=9, font=35, command=lambda:  multiply())
buttonMult.grid(row=1, column=3)

buttonMinus = Button(frame, text="-", height=4, width=9, font=35, command=lambda:  subtract())
buttonMinus.grid(row=2, column=3)

buttonPlus = Button(frame, text="+", height=4, width=9, font=35, command=lambda:  add())
buttonPlus.grid(row=3, column=3)

buttonEquals = Button(frame, text="=", height=4, width=9, font=35, command=lambda:  equals())
buttonEquals.grid(row=4, column=3)

buttonClear = Button(frame, text="clear", height=4, width=9, font=35, command=lambda:  clear())
buttonClear.grid(row=0, column=0)

buttonBackspace = Button(frame, text="del", height=4, width=9, font=35, command=lambda:  backspace())
buttonBackspace.grid(row=0, column=1)

buttonOpposite = Button(frame, text="+/-", height=4, width=9, font=35, command=lambda:  opposite())
buttonOpposite.grid(row=0, column=2)

buttonDecimal = Button(frame, text=".", height=4, width=9, font= 35, command=lambda:  decimal())
buttonDecimal.grid(row=4, column=2)

window.mainloop()




