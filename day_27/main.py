import tkinter

def convert_miles_to_km():
    conversion.config(text=(round(float(input.get()) * 1.609344,3)))


window = tkinter.Tk()
window.title("Mile to km Converter")
window.minsize(width=300,height=150)
window.config(padx=20, pady=20)

# labls
miles = tkinter.Label(text = "Miles", font=("consolas", 14))
miles.grid(column=2, row=0)

eq = tkinter.Label(text = "is equal to:", font=("consolas", 14))
eq.grid(column=0, row=1)

km = tkinter.Label(text = "km", font=("consolas", 14))
km.grid(column=2, row=1)

conversion = tkinter.Label(text = "0", font=("consolas", 14))
conversion.grid(column=1, row=1)

# button
button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)

# entry
input = tkinter.Entry(width=15)
input.grid(column=1, row=0)

window.mainloop()