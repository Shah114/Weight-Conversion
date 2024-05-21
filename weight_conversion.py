# Modules
from tkinter import *

# Creating GUI window
window = Tk()
window.geometry('550x250')
window.title('Weight Converter')

# Function to convert weight in kg to grams, pounds, ounces
def from_kg():
    '''This function is for converting kg to gram, pound and ounce'''
    # Kg to gram
    gram = float(e2_value.get()) * 1000

    # Kg to pounds
    pound = float(e2_value.get()) * 2.20462

    # Kg to ounces
    ounce = float(e2_value.get()) * 35.274

    # Enter the converted weight to the widgets
    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)

# Creating the widget label
e1 = Label(window,  text="Enter the weight in kg:", font=('ariel', 12, 'bold'))
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='gram')
e4 = Label(window, text='pound')
e5 = Label(window, text='ounce')

# Creating the text widgets
t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

# Creating the button
b1 = Button(window, text='Convert', command=from_kg)

# Grid method to place widgets at respective positions
e1.grid(row=2, column=1, padx=20, pady=50)
e2.grid(row=2, column=2)
e3.grid(row=5, column=1)
e4.grid(row=5, column=2)
e5.grid(row=5, column=3)
t1.grid(row=6, column=1)
t2.grid(row=6, column=2)
t3.grid(row=6, column=3, padx=15)
b1.grid(row=2, column=3)

# Starting the GUI
window.mainloop()