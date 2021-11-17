from tkinter import *
import shutil         
from tkinter import filedialog
import os
import webbrowser


def copy_file():
    p = open("C:/copy/path.txt", "r")
    f = open("C:/copy/folder.txt" ,"r")
    destination1 = list(filedialog.askopenfilenames(initialdir =os.getcwd()))
    destination2 = p.read()
    path = destination1[0]
    p1 = path.split('/')
    p1.pop(-1)
    last_indexes = f.read() 
    pn = p1[-int(last_indexes):]
    p2 = "/".join(pn)
    root_path = destination2
    os.makedirs(os.path.join(root_path, p2))
    final_destination = destination2+"/"+p2
        
    for f in destination1:
        shutil.copy(f,final_destination)
    webbrowser.open(final_destination)
    p.close()
    f.close()

copy = copy_file()
print(copy)