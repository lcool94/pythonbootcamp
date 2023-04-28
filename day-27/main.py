# import playground as pg
#
# print(pg.add(1, 2, 3, 4, 5))

from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=500, height=300)
label_Miles = Label(text="Miles", font=("Arial", 20))
label_Miles.grid(column=2, row=0)

label_is_equal_to = Label(text="is equal to:", font=("Arial", 20,))
label_is_equal_to.grid(column=0, row=1)

label_result = Label(text="0", font=("Arial", 20,))
label_result.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 20,))
label_km.grid(column=2, row=1)


def miles_to_km(miles):
    return float(int(miles) * 1.609344)


def button_click():
    result = miles_to_km(input_miles.get())
    label_result.config(text=result)


button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

# Entry

input_miles = Entry(width=20)
input_miles.grid(column=1, row=0)

window.mainloop()
