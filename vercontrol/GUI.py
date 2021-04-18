import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os
import shutil
import log
import projekat

def push_command(folder):
    class PushWindow(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("PUSH")
            label_1 = tk.Label(self, text="Unesite sta ste uradili u ovoj verziji")
            label_1.grid(row=0,padx=55, pady=25)
            E1 = Entry(self)
            E1.grid(row=1,padx=55, pady=25)
            def getInput():
                a = E1.get()
                projekat.pushfunction(a, folder)
                window2.destroy()
            do_push = tk.Button(self, text ="PUSH", command = getInput)
            do_push.grid(row=2,padx=55, pady=25)
    window2 = PushWindow()
    window2.mainloop()

def log_command(folder):
    class LogWindow(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("LOG")

            p = os.path.basename(os.path.normpath(folder))

            logdir = os.path.join('./vercontrol', p)

            os.chdir(logdir)

            label_1 = tk.Label(self, text="LOG", font=("Calibri", 30, 'italic'))
            label_1.grid(row=0,padx=55, pady=25)

            txtarea = Text(self, width=80, height=20)
            txtarea.grid(row=1,padx=55, pady=25)

            tf = open("logver.txt", 'r')
            data = tf.read()
            txtarea.insert(END, data)
            tf.close()

            path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
            os.chdir(path_parent)                       #vracanje jedan dir iznad
            path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
            os.chdir(path_parent)                       #vracanje jedan dir iznad

            def close():
                window2.destroy()

            close_log = tk.Button(self, text ="Close", command = close)
            close_log.grid(row=2,padx=55, pady=25)
    window2 = LogWindow()
    window2.mainloop()

def select_command(folder):
    class SelectWindow(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("SELVER")
            label_1 = tk.Label(self, text="Unesite verziju na koju zelite da se prebacite")
            label_1.grid(row=0,padx=55, pady=25)
            E1 = Entry(self)
            E1.grid(row=1,padx=55, pady=25)
            def getInput():
                b = E1.get()
                if projekat.selverfunction(b, folder) == 0:
                    tk.messagebox.showerror("Greska", "Ne mozete se prebaciti na nepostojecu verziju, odnosno onu u kojoj je vracena prethodna verzija!")
                else:
                    tk.messagebox.showinfo("Uspesno", "Verzija promenjena")
                window2.destroy()
            do_push = tk.Button(self, text ="Select", command = getInput)
            do_push.grid(row=2,padx=55, pady=25)
    window2 = SelectWindow()
    window2.mainloop()

def control(folder):
    class ControlWindow(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("VCS")
            label_2 = tk.Label(self, text="Commands", font=("Calibri", 30, 'italic'), bg="#f2e15c", fg="#1b095c")
            label_2.pack(expand=1, padx=25, pady=15)
            push_button = tk.Button(self, text ="Push command", font=("Cambria", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue", command = lambda: push_command(folder))
            push_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            log_button = tk.Button(self, text ="Log command", font=("Cambria", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue", command = lambda: log_command(folder))
            log_button.pack(side=tk.LEFT, expand=1, padx=25, pady=25)
            select_version_button = tk.Button(self, text ="Select version command", font=("Cambria", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue", command = lambda: select_command(folder))
            select_version_button.pack(side=tk.RIGHT, expand=1, padx=25, pady=25)

    if not folder:
        tk.messagebox.showerror("Greska", "Niste selektovali direktorijum!")
    else:
        window2 = ControlWindow()
        window2.minsize(850, 400)
        window2.configure(bg='#f2e15c')
        window2.mainloop()

def main():
    class Window(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("VCS")
            label_1 = tk.Label(self, text="Welcome to Version Control System!", font=("Helvetica", 36, 'bold', 'italic'), fg="#1b095c", bg="#f2e15c")
            label_1.pack(fill=tk.BOTH, expand=1, padx=25, pady=15)
        
            folder_array = [""]

            def getInput(folder_array):
                folder_array[0] = filedialog.askdirectory()
                folder_array[0]=folder_array[0]+"/"

            load_button = tk.Button(text ="Load", font=("Courier", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue", command = lambda: getInput(folder_array))
            load_button.pack(side = tk.LEFT, expand=1, pady = 100)
            control_button = tk.Button(text ="Control", font=("Courier", 25, "bold"), fg="#1b095c", activebackground="grey", activeforeground="blue", command = lambda: control(folder_array[0]))
            control_button.pack(side = tk.RIGHT, expand=1, pady = 100)

    if not os.path.exists('previousver/.'):
        os.makedirs('previousver/.')

    window = Window()
    window.minsize(1250, 500)
    window.configure(bg='#f2e15c')
    window.mainloop()

if __name__ == "__main__":
    main()

'''TO - DO
# Pre trenutnog pocetnog prozora, napraviti jedan sa CREATE/LOAD repo
# Kada se klikne create repo, izabere se lokacija, u tu lokaciju se edituju fajlovi
# Kada se klikne load repo, izabere se lokacija, i onda izađe, push, log, selver ILI se izbaci repo nije kreiran
# //Svi fajlovi se čuvaju gde i sad, znači prev/curr ver se generišu iznad vercontrol, u prevodu to znači da ako hoćemo da pokrenemo program, idealno bi bilo da se vercontrol fajl već nalazi u jednom praznom direktorijumu
# CPython, Serverska int
'''
