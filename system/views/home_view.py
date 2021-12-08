from tkinter import ttk
from system.views.abstract_view import AbstractView


class HomeView(AbstractView):
    def __init__(self, root, frame, controller):
        self.root = root
        self.frame = frame
        self.controller = controller
        self.setup_view()

    def setup_view(self):
        self.root.geometry("600x500")
        self.root.title("Wholesaler System")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.resizable(width=False, height=False)
        self.frame.grid(row=0, column=0)
        self.load_labels()
        self.load_interactions()

    def load_labels(self):
        system_label = ttk.Label(self.frame, text="Wholesaler System", font=(None, 20))
        system_label.grid(row=0, column=0, pady=10)

    def load_interactions(self):
        login_button = ttk.Button(self.frame, text="Login",
                                  command=self.controller.login_view())
        login_button.grid(row=1, column=0, pady=10)
        register_button = ttk.Button(self.frame, text="Register",
                                     command=self.controller.register_view())
        register_button.grid(row=2, column=0, pady=10)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
