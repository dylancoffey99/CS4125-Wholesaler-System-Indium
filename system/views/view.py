import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,  *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (RegistrationPage, LoginPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(RegistrationPage)

        # to display the current frame passed as
        # parameter

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class RegistrationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Registration Page")
        label.grid(row=0, column=0, padx=10, pady=10)

        name_label = ttk.Label(self, text="Name")
        name_label.grid(row=1, column=0)
        email_label = ttk.Label(self, text="Email")
        email_label.grid(row=2, column=0)
        phone_label = ttk.Label(self, text="Phone Number")
        phone_label.grid(row=3, column=0)
        country_label = ttk.Label(self, text="Country")
        country_label.grid(row=4, column=0)
        password_label = ttk.Label(self, text="Password")
        password_label.grid(row=5, column=0)
        re_enter_password_label = ttk.Label(self, text="Password")
        re_enter_password_label.grid(row=5, column=0)

        name_entry = ttk.Entry(self)
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        email_entry = ttk.Entry(self)
        email_entry.grid(row=2, column=1, padx=10, pady=10)
        phone_entry = ttk.Entry(self)
        phone_entry.grid(row=3, column=1, padx=10, pady=10)
        country_entry = ttk.Entry(self)
        country_entry.grid(row=4, column=1, padx=10, pady=10)
        password_entry = ttk.Entry(self)
        password_entry.grid(row=5, column=1, padx=10, pady=10)
        re_enter_password_entry = ttk.Entry(self)
        re_enter_password_entry.grid(row=5, column=1, padx=10, pady=10)

        register_button = ttk.Button(self, text="Register",
                                     command=lambda: controller.show_frame(RegistrationPage))

        register_button.grid(row=8, column=0, padx=10, pady=10)

        button2 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(LoginPage))

        button2.grid(row=8, column=1, padx=10, pady=10)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Login Page")
        label.grid(row=0, column=0, padx=10, pady=10)

        name_label = ttk.Label(self, text="Name")
        name_label.grid(row=1, column=0)
        password_label = ttk.Label(self, text="Password")
        password_label.grid(row=2, column=0)

        name_entry = ttk.Entry(self)
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        password_entry = ttk.Entry(self)
        password_entry.grid(row=2, column=1, padx=10, pady=10)

        login_button = ttk.Button(self, text="Login",
                                  command=lambda: controller.show_frame(RegistrationPage))

        login_button.grid(row=3, column=1, padx=10, pady=10)


def main(self):
    self.resizable(width=False, height=False)
    self.state('zoomed')  # To make the GUI fit the screen
    self.config(bg="grey")


if __name__ == '__main__':
    root = View()
    main(root)
    root.mainloop()