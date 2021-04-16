import tkinter as tk
import tkinter.messagebox as tkmb

def start_project():
   tkmb.showinfo("Repository", "Welcome to your Repository")

def main():
    class Window(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("VCS - GIT")
            label_1 = tk.Label(self, text="Welcome to GIT!", font=("Helvetica", 50, 'bold', 'italic'), fg="#1b095c", bg="#f2e15c")
            label_1.pack(fill=tk.BOTH, expand=1, padx=25, pady=15)
            push_button = tk.Button(text ="Push command", command = start_project, font=("Courier", 25, 'bold', 'underline'), fg="#1b095c", activebackground="grey", activeforeground="blue")
            push_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            log_button = tk.Button(text ="Log command", command = start_project, font=("Courier", 25, 'bold', 'underline'), fg="#1b095c", activebackground="grey", activeforeground="blue")
            log_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            select_version_button = tk.Button(text ="Select version command", command = start_project, font=("Courier", 25, 'bold', 'underline'), fg="#1b095c", activebackground="grey", activeforeground="blue")
            select_version_button.pack(side=tk.RIGHT, expand=1, padx=25, pady=25)
    window = Window()
    window.minsize(1250, 500)
    window.configure(bg='#f2e15c')
    window.mainloop()
if __name__ == "__main__":
    main()
