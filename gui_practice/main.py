from tkinter import *

# Configuring the window 
window = Tk()
window.title('My First GUI program')
window.minsize(width=500, height=300)
window.config(padx=10, pady=5)

# Configuring the label
label = Label(text="Hey you!", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

def button_clicked():
    label.configure(text=input.get())

# Button 
button = Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text='New Button')
new_button.grid(column=2, row=0)

# Entry 
input = Entry(width=10)
input.insert(END, "Some placeholder")
print(input.get())
input.grid(column=3, row=2)
    
      
window.mainloop()