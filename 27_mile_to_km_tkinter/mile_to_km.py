from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50)

input_field = Entry(width=10)
input_field.grid(column=1, row=0)
mile_label = Label(text="Mile", font=("Arial", 15, "bold"))
mile_label.grid(column=2, row=0)
equal_label = Label(text="is equal to", font=("Arial", 15, "bold"))
equal_label.grid(column=0, row=1)
km_label_output = Label(text="0", font=("Arial", 15, "bold"))
km_label_output.grid(column=1, row=1)
km_label = Label(text="Km", font=("Arial", 15, "bold"))
km_label.grid(column=2, row=1)


def convert():
    km_label_output.config(text=round(float(input_field.get()) * 1.609))


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
