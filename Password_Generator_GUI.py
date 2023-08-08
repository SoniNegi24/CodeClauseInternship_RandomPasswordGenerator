import random
import string
from tkinter import *

root=Tk()
root.config(bg='black')
root.title('Password Generator')
root.geometry("350x350")


label_title = Label(root, text="Generate a Random Password ", fg="black", bg="silver",font=('Helvtica', 15, "bold"))
label_title.pack(pady=5)


label_st = Label(root, text="Choose the strenght of your password: ", fg="silver",bg='black', font=('Helvtica', 12, 'bold'))
label_st.pack(pady=5)

weak = string.ascii_letters
average = string.ascii_letters + string.digits
strong = string.ascii_letters + string.digits + '!@#$%^&*_-+=/'

def select():
    select = choice.get()

choice = IntVar()
r1=Radiobutton(root, text="Weak Password", variable=choice, value=1, font=('Helvtica', 11, 'bold'),bg="silver", command=select)
r1.pack(anchor=CENTER,pady=5)
r2=Radiobutton(root, text="Average Password", variable=choice, value=2, font=('Helvtica', 11, 'bold'), bg="silver", command=select)
r2.pack(anchor=CENTER,pady=5)
r3=Radiobutton(root, text="Strong Password", variable=choice, value=3, font=('Helvtica', 11, 'bold'), bg="silver", command=select)
r3.pack(anchor=CENTER,pady=5)

label_len = Label(root, text="Choose the lenght of your password: ", fg="silver",bg='black' ,font=('Helvtica', 12, 'bold'))
label_len.pack(pady=5)

spin = IntVar()
spin_len = Spinbox(root, from_=4, to_=30, textvariable=spin, width= 14, font= ('arial', 13, 'bold'), bg="silver")
spin_len.pack(pady=5)

def call():
    output.config(text=Pass())

button = Button(root, text="Generate Password", command=call, font=('arial', 12, 'bold'),bd=5 ,bg="silver")
button.pack(pady=5)

def Pass():
    if choice.get() == 1:
        return "".join(random.sample(weak, spin.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, spin.get()))
    else:
        return "".join(random.sample(strong, spin.get()))

output = Message(root, text="", relief=SUNKEN, width=300, font=('arial', 20, 'bold'), bg="silver")
output.pack(pady=5)
    
root.mainloop()