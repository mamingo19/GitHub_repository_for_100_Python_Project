from tkinter import *

from bokeh.layouts import column

window = Tk()
window.title("Mile to Km Converter")
window.minsize(150,100)

#Label

miles_label = Label(text= "Miles", font=("Arial", 10))
miles_label.config(text = "Miles")
miles_label.grid(column = 2, row = 1)

miles_value = Entry(width=10)
miles_value.grid(column = 1, row = 1)

label = Label(text= "is equal to", font=("Arial", 10))
label.grid(column=0,row=2)

km_label = Label(text= "km", font=("Arial", 10))
km_label.grid(column = 2, row = 2)

km_values = Label(text= " ", font=("Arial", 10))
km_values.grid(column = 1, row = 2)

def button_clicked():
    km_values["text"] = int(miles_value.get()) * 1.621371192

button = Button(text="Calculate", command=button_clicked)
button.grid(column = 1, row = 3)




window.mainloop()