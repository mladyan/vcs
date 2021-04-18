import os
import shutil
import log
import GUI

if not os.path.exists('previousver/.'):
    os.makedirs('previousver/.')

if not os.path.exists('currentver/.'):
    os.makedirs('currentver/.')

if not os.path.exists('./vercontrol/logver.txt'):
    f = open("./vercontrol/logver.txt", "w")
    f.write("0")
    f.close()

def main():
    x = "inic"
    while x!="0":
        x = input()

        if x == "list":                                 #current directory i njegovi fajlovi, za debug
            print(os.getcwd())
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for f in files:
                print(f)

        if x == "log":
            def logfunction():
                os.chdir('./vercontrol')
                f = open('logver.txt', 'r')
                file_contents = f.read()
                print ("Prikazuje se broj trenutne verzije i sta je uradjeno u proslim")
                print (file_contents)
                f.close()
                path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
                os.chdir(path_parent)                       #vracanje jedan dir iznad
            logfunction()
                
        if x == "push":
            def pushfunction():
                print("Unesite sta ste uradili u ovoj verziji") #saljemo poruku commita
                a = input()
                os.chdir('./vercontrol')
                log.log_it(a)                               #ubelezavamo commit, i povecavamo verzijju

                path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
                os.chdir(path_parent)                       #vracanje jedan dir iznad

                dirpath = os.path.join('./previousver', log.vernumbstring)
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)
                src = './currentver/'
                dest = dirpath                              #iz currentver u previousver

                files = os.listdir(src)                     #kopiramo
                for f in files:
                    shutil.copy(src + f, dest)
            pushfunction()

        if x == "selectversion":
            def selverfunction():
                print("Unesite verziju na koju se zelite prebaciti")
                b = input()
                b_save = b
                b = b + "/"                                 #polaz - folder izabrane verzije

                dirpath = os.path.join('./previousver', b)
                if not os.path.exists(dirpath):
                    return "Ne mozete se prebaciti na nepostojecu verziju, odnosno onu u kojoj je vracena prethodna verzija!"

                src = dirpath                               #destinacija - currentver folder
                dest = './currentver/'

                for f in os.listdir(dest):                  #brisemo sve iz destinacije pre kopiranja
                    os.remove(os.path.join(dest, f))

                files = os.listdir(src)                     #kopiramo
                for f in files:
                    shutil.copy(src + f, dest)
                
                a = "Reverted to " + b_save + ". version"
                os.chdir('./vercontrol')
                log.log_it(a)

                path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
                os.chdir(path_parent)                       #vracanje jedan dir iznad

                return "uspesno"
            selverfunction()
            

    print("kraj programa")

if __name__ == "__main__":
    main()
