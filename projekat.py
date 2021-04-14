import os
import shutil
import log

if not os.path.exists('previousver'):
    os.makedirs('previousver')

if not os.path.exists('currentver'):
    os.makedirs('currentver')

if not os.path.exists('logver.txt'):
    f = open("logver.txt", "w")
    f.write("0")
    f.close()

x = "inic"

while x!="0":
    x = input()

    if x == "list":
        print(os.getcwd())
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            #do something
            print(f)
            
    if x == "chgdir":
        os.chdir('./previousver')
        print(os.getcwd())

    if x == "push":
        print("Unesite sta ste uradili u ovoj verziji")
        a = input()
        log.log_it(a)
        src = './'
        dest = './previousver'
        files = os.listdir(src)
        for f in files:
            if f != "projekat.py" and f!="currentver" and f!="previousver" and f!="logver.txt" and f!="log.py":
                shutil.move(src + f, dest)

print("kraj programa")

'''
TO DO
napravi var a sa porukom commita
spoji log.py sa projekat.py
python main funkcija
log funkcija
'''