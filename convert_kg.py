# import the tkinter module and all of its functions and classes
from tkinter import *

# create a new instance of the Tkinter Tk class, which is the main window or container for the GUI
window = Tk()

# define a function named kg_to_grams that will be called when the "Convert" button is clicked
def kg_to_grams():

    # print the value entered in the entry field for debugging purposes
    print(e1_value.get())

    # calculate the converted values for grams, pounds, and ounces based on the input value
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274

    # insert the converted values into the corresponding text boxes in the GUI
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

# create a new instance of the Tkinter Button class and assign it to the variable b1
# the button is added to the window container and labeled "Convert"
# the command option specifies that the kg_to_grams function should be called when the button is clicked
b1 = Button(window, text='Convert', command=kg_to_grams)

# place the "Convert" button in the top-right corner of the GUI using the grid layout manager
b1.grid(row = 0, column = 2 )

# create a new instance of the Tkinter StringVar class and assign it to the variable e1_value
# this is used to store the value entered in the entry field
e1_value = StringVar()

# create a new instance of the Tkinter Entry class and assign it to the variable e1
# the entry field is added to the window container
# the textvariable option is set to e1_value so that the value entered can be accessed later
e1 = Entry(window, textvariable=e1_value)

# place the entry field in the top-center of the GUI using the grid layout manager
e1.grid(row=0, column=1)

# create a new instance of the Tkinter Label class and assign it to the variable e2
# the label is added to the top-left corner of the GUI using the grid layout manager
e2 = Label(text='Kg')
e2.grid(row=0, column=0)

# create new instances of the Tkinter Text class and assign them to the variables t1, t2, and t3
# the text boxes are added to the bottom row of the GUI using the grid layout manager
# each text box is assigned a width of 20 characters and a height of 1 line
t1 = Text(window, height=1,width=20)
t1.grid(row=1, column=0)
t2 = Text(window, height=1,width=20)
t2.grid(row=1, column=1)
t3 = Text(window, height=1,width=20)
t3.grid(row=1, column=2)

# start the event loop that listens for user input and updates the GUI as needed
# the mainloop() method must be called at the end of the code to keep the GUI running
window.mainloop()
