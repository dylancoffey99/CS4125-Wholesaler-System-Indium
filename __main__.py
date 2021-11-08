import tkinter as tk


class MainApplication(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
