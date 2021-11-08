import tkinter as tk
from tkinter import ttk
import system.views.registration_page
from system.views.login_page import LoginPage
from system.views.user_page import UserPage
from system.views.admin_page import AdminPage


class View(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,  *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomeView, system.views.registration_page.RegistrationPage,
                  LoginPage, UserPage, AdminPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomeView)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomeView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Home Page", font='Aerial 20 bold')
        label.grid(row=0, column=3, padx=10, pady=10)

        register_button = ttk.Button(self, text="Register",
                                     command=lambda: controller.show_frame
                                     (system.views.registration_page.RegistrationPage))

        register_button.grid(row=9, column=2, padx=10, pady=10)
        login_button = ttk.Button(self, text="Login",
                                  command=lambda: controller.show_frame(LoginPage))

        login_button.grid(row=9, column=3, padx=10, pady=10)


def main(self):
    self.resizable(width=False, height=False)
    self.geometry('600x500')
    self.config(bg="grey")


if __name__ == '__main__':
    root = View()
    main(root)
    root.mainloop()
