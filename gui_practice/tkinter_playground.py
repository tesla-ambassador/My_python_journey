from tkinter import *

# Configuring the window 
window = Tk()
window.title('My First GUI program')
window.minsize(width=500, height=300)

# Configuring the label
label = Label(text="Hey you!", font=("Arial", 24, "bold"))
label.pack()

def button_clicked():
    label.configure(text=input.get())

# Button 
button = Button(text='Click me', command=button_clicked)
button.pack()

# Entry 
input = Entry(width=10)
input.insert(END, "Some placeholder")
print(input.get())
input.pack()

# Text
text = Text(width=30, height=5)
# Puts the cursor in textbox
text.focus()
# Inserts some text into the textbox
text.insert(END, "Example text")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    print(spin_box.get())
    
spin_box = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spin_box.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbox
def checkbox_used():
    print(checked_state.get())

checked_state = IntVar()
check = Checkbutton(text='Toggle 1/0', variable=checked_state, command=checkbox_used)
check.pack()   

# Radiobutton
def radiobutton_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton_1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=radiobutton_used)
radiobutton_2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=radiobutton_used)
radiobutton_1.pack()
radiobutton_2.pack()

# Listbox
def get_list_item(event):
   print(list_box.get(list_box.curselection()))

list_box = Listbox(height=4)
mc_s = ['Luffy', 'Naruto', 'Ichigo']
for mc in mc_s:
    list_box.insert(mc_s.index(mc), mc)
list_box.bind("<<ListboxSelect>>", get_list_item)
list_box.pack()
    
      
window.mainloop()