import tkinter as tk

def start_project():
    class Window2(tk.Tk):
         def __init__(self):
            super().__init__()
            self.title("Repository")
            label_2 = tk.Label(self, text="Welcome to your Repository", font=("Calibri", 30, 'italic'), bg="#f2e15c", fg="#1b095c")
            label_2.pack(expand=1, padx=25, pady=15)
            push_button = tk.Button(self, text ="Push command", font=("Cambria", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue")
            push_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            log_button = tk.Button(self, text ="Log command", font=("Cambria", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue")
            log_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            select_version_button = tk.Button(self, text ="Select version command", font=("Cambria", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue")
            select_version_button.pack(side=tk.RIGHT, expand=1, padx=25, pady=25)
    window_project = Window2()
    window_project.minsize(1250, 500)
    window_project.configure(bg='#f2e15c')
    window_project.mainloop()

def main():
    class Window(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("VCS - GIT")
            label_1 = tk.Label(self, text="Welcome to GIT!", font=("Helvetica", 50, 'bold', 'italic'), fg="#1b095c", bg="#f2e15c")
            label_1.pack(fill=tk.BOTH, expand=1, padx=25, pady=15)
            load_repository_button = tk.Button(text ="Load your Repository", font=("Courier", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue")
            load_repository_button.pack(side = tk.LEFT, expand=1, pady = 100)
            create_repository_button = tk.Button(text ="Create new Repository", font=("Courier", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue")
            create_repository_button.pack(side = tk.RIGHT, expand=1, pady = 100)
    window_opening = Window()
    window_opening.minsize(1250, 500)
    window_opening.configure(bg='#f2e15c')
    window_opening.mainloop()

if __name__ == "__main__":
    main()
