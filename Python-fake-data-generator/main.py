from tkinter import Tk, \
    Button, \
    Entry

first_number = 0
is_stack_empty = True
math = 'addition'
root = Tk()
root.title("Simple Calculator")  # set title of core window


e = Entry(
    root,
    borderwidth=5
)

e.grid(
    row=0,
    column=0,
    columnspan=3,
    padx=10,
    pady=10
)

e.insert(0, "0")


def button_click(n):
    global is_stack_empty
    current = ''
    if is_stack_empty:
        is_stack_empty = False
    else:
        current = e.get()

    e.delete(0, "end")
    print(current)
    e.insert(0, current + str(n))


def clear_screen():
    """clear the screen"""
    e.delete(0, "end")


def add():
    """saves first number to global variable"""
    global first_number
    global math
    math = "addition"
    first_number = int(e.get())
    e.delete(0, "end")


def divide():
    """saves first number to global variable"""
    global first_number
    global math
    math = "division"
    first_number = int(e.get())
    e.delete(0, "end")


def multiply():
    """saves first number to global variable"""
    global first_number
    global math
    math = "multiplication"
    first_number = int(e.get())
    e.delete(0, "end")


def subtract():
    """saves first number to global variable"""
    global first_number
    global math
    math = "subtraction"
    first_number = int(e.get())
    e.delete(0, "end")


def evaluate():
    """shows the result of calculation"""
    global is_stack_empty
    second_number = int(e.get())
    e.delete(0, "end")

    if math == "addition":
        result = first_number + second_number
    if math == "subtraction":
        result = first_number - second_number
    if math == "multiplication":
        result = first_number * second_number
    if math == "division":
        result = first_number / second_number

    e.insert(0, str(result))
    is_stack_empty = True


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text='+', padx=39, pady=20,
                    command=add)
button_equal = Button(root, text='=', padx=91, pady=20,
                      command=evaluate)
button_clear = Button(root, text='Clear', padx=79, pady=20,
                      command=clear_screen)

button_minus = Button(root, text='-', padx=42, pady=20,
                      command=subtract)
button_mult = Button(root, text='x', padx=42, pady=20,
                     command=multiply)
button_divide = Button(root, text='/', padx=45, pady=20,
                       command=divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_minus.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
