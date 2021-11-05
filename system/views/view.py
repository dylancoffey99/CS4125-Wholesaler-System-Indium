import tkinter as tk
from tkinter import ttk
from system.views.user_view import UserView
from system.views.login_view import LoginView
from system.views.admin_view import AdminView
from system.views.registration_view import RegistrationView


class View(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,  *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomeView, RegistrationView, LoginView, UserView, AdminView):
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
                                     command=lambda: controller.show_frame(RegistrationView))

        register_button.grid(row=9, column=2, padx=10, pady=10)
        login_button = ttk.Button(self, text="Login",
                                  command=lambda: controller.show_frame(LoginView))

        login_button.grid(row=9, column=3, padx=10, pady=10)


def main(self):
    self.resizable(width=False, height=False)
    self.geometry('600x500')
    self.config(bg="grey")


if __name__ == '__main__':
    root = View()
    main(root)
    root.mainloop()
