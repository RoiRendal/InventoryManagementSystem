from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import InventoryManagementSystem.Employee
import InventoryManagementSystem.AccountSystem


class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 160) - (app_height / 160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file='images\\Konica-brand-logo.png')
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Welcome')

        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#ffffff')

        # ====== MENU BAR ==========
        logoIcon = Image.open('images\\Konica-brand-logo.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(homepage, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=0, y=0)

        menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        home_bgImg = Image.open('images\\home_bg.jpg')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

        brandIcon = Image.open('images\\Konica-brand-logo.png')
        photo = ImageTk.PhotoImage(brandIcon)
        brandlogo = Label(homepage, image=photo, bg='black')
        brandlogo.image = photo
        brandlogo.place(x=1085, y=83)

        admLabel = Label(homepage, text='EMPLOYEE', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#ffffff')
        admLabel.place(x=1150, y=11)

        heading = Label(homepage, text='KONICA', bg='black', fg='#FF3661', font=("yu gothic ui", 19, "bold"))
        heading.place(x=770, y=90)

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#E75373', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#E75373', activeforeground='white')
        home_button.place(x=70, y=15)

        def manage():
            dashboard_window.withdraw()
            os.system("python Employee.py")
            dashboard_window.destroy()

        # ========== MANAGE BUTTON =======
        manage_button = Button(homepage, text='Manage', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#E75373', activeforeground='#7a7a7a',
                               command=manage)
        manage_button.place(x=150, y=15)

        # ========== PRODUCTS BUTTON =======
        product_button = Button(homepage, text='Products', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                cursor='hand2', activebackground='#E75373', activeforeground='#7a7a7a',
                                command=manage)
        product_button.place(x=250, y=15)

        def logout():
            win = Toplevel()
            InventoryManagementSystem.AccountSystem.accPage(win)
            dashboard_window.withdraw()
            win.deiconify()

        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#E75373', activeforeground='#7a7a7a', command=logout)
        logout_button.place(x=350, y=15)


def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
