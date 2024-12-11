import InventoryManagementSystem.AccountSystem
import os
import sys
from tkinter import *

root = Tk()
image = PhotoImage(file='images\\photoExpress-ico.png')

height = 830
width = 930
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='#93c83d')

bg_label = Label(root, image=image, bg='#93c83d')
bg_label.place(x=170, y=65)

progress_label = Label(root, text="Loading...", font=('Berlin Sans FB', 15, 'bold'), fg='black', bg='#93c83d')
progress_label.place(x=400, y=700)

exit_btn = Button(text='x', bg='#93c83d', command=lambda: exit_window(), bd=0, font=("Berlin Sans FB", 30, "bold"),
                  activebackground='#93c83d', fg='white')
exit_btn.place(x=850, y=0)


def exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    os.system("python AccountSystem.py")
    root.destroy()


i = 0


def load():
    global i
    if i <= 10:
        txt = 'LOADING'
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        i += 1
    else:
        top()


load()

load()
root.mainloop()
