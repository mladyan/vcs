import tkinter as tk
import tkinter.messagebox as tkmb



def start_project():
   tkmb.showinfo("Repository", "Welcome to your Repository")

def main():
    class Window(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("VCS - GIT")
            label_1 = tk.Label(self, text="Welcome to GIT!")
            label_1.pack(fill=tk.BOTH, expand=1, padx=100, pady=15)
            push_button = tk.Button(text ="Push command", command = start_project)
            push_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            log_button = tk.Button(text ="Log command", command = start_project)
            log_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            select_version_button = tk.Button(text ="Select version command", command = start_project)
            select_version_button.pack(side=tk.RIGHT, expand=1, padx=25, pady=25)
    window = Window()
    window.mainloop()
if __name__ == "__main__":
    main()
