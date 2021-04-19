# Import Dependencies
from tkinter import *

# declare global expression variable
expression = ""

# function to update expression in the text box
def press(num):
    # point to the global expression variable
    global expression

    # concatanate string
    expression = expression + str(num)

    # update expression
    equation.set(expression)

# function to evaluate final expression
def equalpress():
    # try and except for handling errors like zero division error
    try:
        global expression

        # eval function evaluates the expression and str converts the result into sting
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable to empty string

        expression = ""
    # if error is generated than handle bt except block
    except:
        equation.set("error")
        expression = ""

# function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# driver code

if __name__ == "__main__":
    #create a gui window
    gui = Tk()

    #set the background color of window
    gui.configure(background="light green")

    #set title
    gui.title("Simple Calculator")

    # set the configuration
    gui.geometry("270x150")

    #Create StringVar class instance
    equation = StringVar()

    #create text box for showing expression
    expression_field = Entry(gui, textvariable=equation)

    #Use grid method to place widgets at respective place
    expression_field.grid(columnspan=4,ipadx=70)

    # create buttons for grid
    button1 = Button(gui, text='1', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2,column=0)

    button2 = Button(gui, text='2', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2,column=1)

    button3 = Button(gui, text='3', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2,column=2)

    button4 = Button(gui, text='4', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3,column=0)

    button5 = Button(gui, text='5', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3,column=1)

    button6 = Button(gui, text='6', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3,column=2)

    button7 = Button(gui, text='7', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4,column=0)

    button8 = Button(gui, text='8', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4,column=1)

    button9 = Button(gui, text='9', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4,column=2)

    button0 = Button(gui, text = '0', fg='black', bg = 'red', command = lambda: press(0), height=1, width = 7)
    button0.grid(row=5,column=0)

    plus = Button(gui, text = ' + ', fg='black', bg = 'red', command = lambda: press('+'), height=1, width = 7)
    plus.grid(row=2,column=3)

    minus = Button(gui, text = ' - ', fg='black', bg = 'red', command = lambda: press('-'), height=1, width = 7)
    minus.grid(row=3,column=3)

    multiply = Button(gui, text = ' * ', fg='black', bg = 'red', command = lambda: press('*'), height=1, width = 7)
    multiply.grid(row=4,column=3)

    divide = Button(gui, text = ' / ', fg='black', bg = 'red', command = lambda: press('/'), height=1, width = 7)
    divide.grid(row=5,column=3)

    equal = Button(gui, text = ' = ', fg='black', bg = 'red', command = lambda: press('='), height=1, width = 7)
    equal.grid(row=5,column=2)

    clear = Button(gui, text = 'Clear', fg='black', bg = 'red', command = clear, height=1, width = 7)
    clear.grid(row=5,column=1)

    Decimal = Button(gui, text='.', fg='black', bg = 'red', command = lambda: press('.'), height=1, width = 7)
    Decimal.grid(row=6, column=0)

    #start the gui

    gui.mainloop()