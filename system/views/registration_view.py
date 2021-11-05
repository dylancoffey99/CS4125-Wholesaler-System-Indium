import tkinter as tk
from tkinter import ttk
from system.views.login_view import LoginView
from system.views.user_view import UserView


class RegistrationView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Registration Page", font='Aerial 20 bold')
        label.grid(row=0, column=3, padx=10, pady=10)

        name_label = ttk.Label(self, text="Name", font='Aerial 12 ')
        name_label.grid(row=3, column=2)
        email_label = ttk.Label(self, text="Email", font='Aerial 12 ')
        email_label.grid(row=4, column=2)
        phone_label = ttk.Label(self, text="Phone Number", font='Aerial 12 ')
        phone_label.grid(row=5, column=2)
        country_label = ttk.Label(self, text="Country", font='Aerial 12 ')
        country_label.grid(row=6, column=2)
        password_label = ttk.Label(self, text="Password", font='Aerial 12 ')
        password_label.grid(row=7, column=2)
        re_enter_password_label = ttk.Label(self, text="Re-enter Password", font='Aerial 12 ')
        re_enter_password_label.grid(row=8, column=2)

        name_entry = ttk.Entry(self, width=27)
        name_entry.grid(row=3, column=3, padx=10, pady=10)
        email_entry = ttk.Entry(self, width=27)
        email_entry.grid(row=4, column=3, padx=10, pady=10)
        phone_entry = ttk.Entry(self, width=27)
        phone_entry.grid(row=5, column=3, padx=10, pady=10)
        country_list = tk.StringVar()
        country = ttk.Combobox(self, width=27, textvariable=country_list)
        country['values'] = ('Luxembourg',
                             'Malta',
                             'Germany',
                             'Romania',
                             'Cyprus',
                             'France',
                             'UK',
                             'Estonia',
                             'Slovakia',
                             'Bulgaria',
                             'Austria',
                             'Italy',
                             'Slovenia',
                             'Ireland',
                             'Portugal',
                             'Poland',
                             'Greece',
                             'Finland',
                             'Sweden',
                             'Denmark',
                             'Croatia',
                             'Hungary'
                             )

        country.grid(row=6, column=3, padx=10, pady=10)
        password_entry = ttk.Entry(self, width=27)
        password_entry.grid(row=7, column=3, padx=10, pady=10)
        re_enter_password_entry = ttk.Entry(self, width=27)
        re_enter_password_entry.grid(row=8, column=3, padx=10, pady=10)

        register_button = ttk.Button(self, text="Register",
                                     command=lambda: controller.show_frame(UserView))

        register_button.grid(row=9, column=2, padx=10, pady=10)
        login_button = ttk.Button(self, text="Already have an account",
                                  command=lambda: controller.show_frame(LoginView))

        login_button.grid(row=9, column=3, padx=10, pady=10)
