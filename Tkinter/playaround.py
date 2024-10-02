from tkinter import *


window = Tk()
window.title("My first GUI Program")
window.minsize(500,300)

#Label

my_label = Label(text= "I am a label", font=("Arial", 24, "bold"))
my_label.config(text = "new text")
my_label.grid(column = 0, row = 0)

#Button

def button_clicked():
    my_label["text"] = input.get()
    print("Omg yes click me daddy")

button = Button(text="Click me daddy!", command=button_clicked)
button.grid(column = 1, row = 1)
button = Button(text="Hello daddy", command=button_clicked)
button.grid(column = 2, row = 0)

#Entry

input = Entry(width=10)
input.grid(column = 3, row = 3)

window.mainloop()