from tkinter import *

window = Tk()
window.title('Mile to Kilometer converter')
window.minsize(width=300, height=5)
window.config(padx=10, pady=5)

# Logic
def convert_to_km():
    result = float(input.get()) * 1.6
    km_label_number.config(text=result)

# User Interface
input = Entry(width=10)
input.grid(column=2, row=1)

mile_label = Label(text='Mile(s)', font=("Arial", 12, "italic"))
mile_label.grid(column=3, row=1)

is_equal_label = Label(text='Is Equal to', font=("Arial", 12, "bold"))
is_equal_label.grid(column=1, row=2)

km_label_number = Label(text=0, font=("Arial", 16, "bold"))
km_label_number.grid(column=2, row=2)

km_label = Label(text='Km', font=("Arial", 12, "italic"))
km_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", padx=2, pady=1, command=convert_to_km)
calculate_button.grid(column=2, row=3)
    
window.mainloop()