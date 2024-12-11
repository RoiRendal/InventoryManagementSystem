from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import InventoryManagementSystem.Employee
import InventoryManagementSystem.admin
import InventoryManagementSystem.Dashboard
import InventoryManagementSystem.admin_start


class accPage:
    def __init__(self, AccountSystem_window):
        self.AccountSystem_window = AccountSystem_window

        # window size & placement
        AccountSystem_window.rowconfigure(0, weight=1)
        AccountSystem_window.columnconfigure(0, weight=1)
        height = 850
        width = 900
        x = (AccountSystem_window.winfo_screenwidth() // 2) - (width // 2)
        y = (AccountSystem_window.winfo_screenheight() // 4) - (height // 4)
        AccountSystem_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        AccountSystem_window.resizable(0, 0)

        # window Icon
        icon = PhotoImage(file='images\\Konica-brand-logo.png')
        AccountSystem_window.iconphoto(True, icon)

        AccountSystem_window.title('KONICA')

        # Navigating through windows
        sign_up = Frame(AccountSystem_window)
        sign_in = Frame(AccountSystem_window)
        landing_page = Frame(AccountSystem_window)

        for frame in (landing_page, sign_in, sign_up):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(landing_page)

        # ======================================================================================
        # =================== LANDING PAGE ========================================================
        # ======================================================================================
        landing_page.config(background='#93c83d')

        # ====== LOGO ==========

        brand_name = Label(landing_page, text='KONICA PHOTO EXPRESS', bg='#93c83d', fg='#333331',
                           font=("Berlin Sans FB", 25, "bold"))
        brand_name.place(x=235, y=233)

        text = Label(landing_page, text="INVENTORY MANAGEMENT SYSTEM", bg='#93c83d', font=("Tw Cen MT", 22, "bold"))
        text.place(x=212, y=290)

        # Login Button
        login_button = Button(landing_page, text='Login', bg='#E75373', font=("Tw Cen MT", 25, "bold"), bd=0,
                              fg='white',
                              cursor='hand2', activebackground='#E75373', activeforeground='white',
                              command=lambda: show_frame(sign_in))
        login_button.place(x=387, y=450)

        def open_employee():
            win = Toplevel()
            InventoryManagementSystem.Dashboard.FirstPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()

        def open_admin():
            win = Toplevel()
            InventoryManagementSystem.admin_start.FirstPage(win)
            AccountSystem_window.withdraw()
            win.deiconify()

        # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ SIGN IN PAGE ////////////////////////////////////////////////
        sign_in.config(background='#93c83d')

        heading = Label(sign_in, text="Sign In", font=("Tw Cen MT", 25, "bold"), bg='#93c83d')
        heading.place(x=390, y=180)

        Username = StringVar()
        Password = StringVar()

        def login_all():
            # Admin
            conn1 = sqlite3.connect("./Database/PhotoExpress.db")
            cursor1 = conn1.cursor()
            find_user1 = 'SELECT * FROM Admin_Account WHERE admin_username = ? and admin_password = ?'
            cursor1.execute(find_user1, [(username_entry.get()), (password_entry.get())])

            # Employee
            conn3 = sqlite3.connect("./Database/PhotoExpress.db")
            cursor3 = conn3.cursor()
            find_user3 = 'SELECT * FROM Employee_Account WHERE employee_username = ? and employee_password = ?'
            cursor3.execute(find_user3, [(username_entry.get()), (password_entry.get())])

            result3 = cursor3.fetchall()
            result1 = cursor1.fetchall()

            if result1:
                messagebox.showinfo("Success", 'Login Success!,\n\nPress "OK" to continue.')
                open_admin()
            elif result3:
                messagebox.showinfo("Success", 'Login Success!,\n\nPress "OK" to continue.')
                open_employee()
            else:
                messagebox.showerror("Failed", "Invalid credentials. Please try again.")

        # \\\\\\\\\\\\\\\\\\\\\\\\\\\Username//////////////////////////////////////////
        username_label = Label(sign_in, text='Username', fg="#27221c", bg='#93c83d', font=("Tw Cen MT", 22, "bold"))
        username_label.place(x=295, y=280)
        username_entry = Entry(sign_in, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                               font=("Tw Cen MT", 22, 'bold'), textvariable=Username)
        username_entry.place(x=295, y=312, width=290, height=34)
        username_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        # \\\\\\\\\\\\\\\\\\\\\\\\\\\Password//////////////////////////////////////////
        password_label = Label(sign_in, text='Password', fg="#27221c", bg='#93c83d', font=("Tw Cen MT", 22, "bold"))
        password_label.place(x=295, y=380)
        password_entry = Entry(sign_in, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                               font=("Tw Cen MT", 22), show="•",
                               textvariable=Password)
        password_entry.place(x=295, y=412, width=290, height=34)
        password_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        loginButton = Button(sign_in, fg='#f8f8f8', text='Login', bg='#FF3661', font=("Tw Cen MT", 22, "bold"),
                             cursor='hand2', activebackground='#FF3661', command=login_all)
        loginButton.place(x=295, y=500, width=290, height=40)

        # =============================================================================================================
        # ================================ SIGN UP PAGE ===============================================================
        # =============================================================================================================
        sign_up.config(background='#93c83d')

        brand_name = Label(sign_up, text='KONICA PHOTO EXPRESS', bg='#93c83d', fg='#333331',
                           font=("Tw Cen MT", 15, "bold"))
        brand_name.place(x=290, y=60)

        text = Label(sign_up, text="INVENTORY MANAGEMENT SYSTEM", bg='#93c83d', font=("Tw Cen MT", 12, "bold"))
        text.place(x=320, y=140)
        txt3 = "Our vision is to be the market leader \nand innovator in the imaging industry \n\n “We strive to be the Imaging Centre of Choice” "
        text2 = Label(sign_up, text=txt3,
                      fg="#6b6a69", bg='#93c83d', font=("Tw Cen MT", 11, "bold"))
        text2.place(x=20, y=180)

        heading = Label(sign_up, text="Create Account", font=("Tw Cen MT", 13, "bold"), bg='#93c83d')
        heading.place(x=440, y=30)

        FullName = StringVar()
        Username2 = StringVar()
        Password2 = StringVar()

        def signup_all():
            check_counter = 0
            warn = ""
            if fullname_entry.get() == "":
                warn = "Please enter your full name"
            else:
                check_counter += 1

            if username_entry2.get() == "":
                warn = "Please enter your username"
            else:
                check_counter += 1

            if password_entry2.get() == "":
                warn = "Please make sure your PASSWORD, USERNAME AND FULLNAME Fields are not empty"
            else:
                check_counter += 1

        # ========================================================================
        # ============================Full name====================================
        # ========================================================================
        fullname_label = Label(sign_up, text='Fullname', fg="#27221c", bg='#93c83d', font=("Tw Cen MT", 12, "bold"))
        fullname_label.place(x=380, y=80)
        fullname_entry = Entry(sign_up, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                               font=("Tw Cen MT", 12, 'bold'), textvariable=FullName)
        fullname_entry.place(x=380, y=112, width=290, height=34)
        fullname_entry.config(highlightbackground="#6b6a69", highlightcolor="black")

        # ========================================================================
        # ============================Username====================================
        # ========================================================================
        username_label2 = Label(sign_up, text='Username', fg="#27221c", bg='#93c83d', font=("Tw Cen MT", 12, "bold"))
        username_label2.place(x=380, y=165)
        username_entry2 = Entry(sign_up, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                                font=("Tw Cen MT", 12, 'bold'), textvariable=Username2)
        username_entry2.place(x=380, y=197, width=290, height=34)
        username_entry2.config(highlightbackground="#6b6a69", highlightcolor="black")

        # ========================================================================
        # ============================Password====================================
        # ========================================================================
        password_label2 = Label(sign_up, text='Password', fg="#27221c", bg='#93c83d', font=("Tw Cen MT", 12, "bold"))
        password_label2.place(x=380, y=250)
        password_entry2 = Entry(sign_up, highlightthickness=2, relief=FLAT, bg="#fafafa", fg="#6b6a69",
                                font=("Tw Cen MT", 12), show='•',
                                textvariable=Password2)
        password_entry2.place(x=380, y=282, width=290, height=34)
        password_entry2.config(highlightbackground="#6b6a69", highlightcolor="black")

        signupButton = Button(sign_up, fg='#f8f8f8', text='Create Account', bg='#FF3661',
                              font=("Tw Cen MT", 12, "bold"),
                              cursor='hand2', activebackground='#FF3661', command=signup_all)
        signupButton.place(x=380, y=370, width=290, height=40)

        line = Canvas(sign_up, width=286, height=1.5, bg="#e6e6e6", highlightthickness=0)
        line.place(x=380, y=440)
        label = Label(sign_up, text='Already have account', bg='#93c83d')
        label.place(x=460, y=430)

        sign_inButton = Button(sign_up, fg='#f8f8f8', text='Login', bg='#4286f5', font=("Tw Cen MT", 12, "bold"),
                               cursor='hand2', activebackground='#4286f5', command=lambda: show_frame(sign_in))
        sign_inButton.place(x=380, y=470, width=290, height=40)

        # AccountSystem_window.mainloop()


def page():
    window = Tk()
    accPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
