from tkinter import *
window = Tk()
window.title("My first GUI 🥳")
window.minsize(width=150,height=150)
window.config(padx=20,pady=20)
my_label = Label(text="Miles")
my_label.grid(column = 2, row= 0)

def calculateMiles():
    milesLabel["text"] = int(int(entry.get()) * 1.60934)

button = Button(text="Calculate",command=calculateMiles)
button.grid(column = 1, row= 2)

entry = Entry(width=7)
entry.grid(column = 1, row = 0)

label = Label(text="is equal to")
label.grid(column = 0, row=1)

milesLabel = Label(text="0")
milesLabel.grid(column = 1, row=1)

kmLabel = Label(text="km")
kmLabel.grid(column = 2, row= 1)
window.mainloop()