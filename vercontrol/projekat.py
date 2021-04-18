import os
import shutil
import log

def pushfunction(a, folder):
    p = os.path.basename(os.path.normpath(folder))
    print(p)

    print(os.getcwd())

    logdir = os.path.join(os.path.abspath('vercontrol'), p)
    
    print(logdir)

    if not os.path.exists(logdir):
        os.makedirs(logdir)

    os.chdir(logdir)
    log.log_it(a,logdir)                        #ubelezavamo commit, i povecavamo verzijju

    path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
    os.chdir(path_parent)                       #vracanje jedan dir iznad
    path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
    os.chdir(path_parent)                       #vracanje jedan dir iznad


    dirpath = os.path.join('./previousver', p)
    dirpath = os.path.join(dirpath, log.vernumbstring)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    src = folder
    dest = dirpath                              #iz currentver u previousver

    files = os.listdir(src)                     #kopiramo
    for f in files:
        shutil.copy(src + f, dest)

def selverfunction(b, folder):
    b_save = b
    b = b + "/"                                 #polaz - folder izabrane verzije

    p = os.path.basename(os.path.normpath(folder))
    print(p) 

    dirpath = os.path.join('./previousver', p)
    dirpath = os.path.join(dirpath, b)
    if not os.path.exists(dirpath):
        return 0

    src = dirpath                               #destinacija - currentver folder
    dest = folder

    for f in os.listdir(dest):                  #brisemo sve iz destinacije pre kopiranja
        os.remove(os.path.join(dest, f))

    files = os.listdir(src)                     #kopiramo
    for f in files:
        shutil.copy(src + f, dest)
    
    os.chdir('./vercontrol')

    logdir = os.path.join('./', p)

    if not os.path.exists(logdir):
        os.makedirs(logdir)

    a = "Reverted to " + b_save + ". version"

    os.chdir(logdir)
    log.log_it(a, logdir)

    path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
    os.chdir(path_parent)                       #vracanje jedan dir iznad
    path_parent = os.path.dirname(os.getcwd())  #vracanje jedan dir iznad
    os.chdir(path_parent)                       #vracanje jedan dir iznad

    return 1