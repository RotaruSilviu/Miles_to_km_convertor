from tkinter import *

FONT = ("Arial", 20, "bold")
PADDING = 10


def convertor():
    converted_miles = int(user_input.get()) * 1.61
    result.config(text=round(converted_miles, 2))


window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=500, height=400)
window.config(padx=100, pady=100)

# Labels:
equal = Label(window, text="is equal to", font=FONT)
equal.config(padx=PADDING, pady=PADDING)
equal.grid(column=0, row=1)

miles = Label(window, text="Miles", font=FONT)
miles.config(padx=PADDING, pady=PADDING)
miles.grid(column=2, row=0)

km = Label(window, text="Km", font=FONT)
km.config(padx=PADDING, pady=PADDING)
km.grid(column=2, row=1)

result = Label(window, text=0, font=FONT)
result.config(padx=PADDING, pady=PADDING)
result.grid(column=1, row=1)


# Entry
user_input = Entry(window, width=25)
user_input.grid(column=1, row=0)
to_calculate = user_input.get()
# Button

calculate_button = Button(window, text="Calculate", command=convertor)
calculate_button.config(padx=PADDING, pady=PADDING, font=FONT)
calculate_button.grid(column=1, row=2)

window.mainloop()
