import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

path = "C:/"
finall = path+"\copy"
try:
    os.path.isdir('copy')
    
except: 
    os.mkdir(finall)
finallpath = finall+"\path.txt"
finallfolder = finall+"/folder.txt"

 
class Widget:
    def DestinationBrowse(self):

        self.destinationdirectory = filedialog.askdirectory(initialdir =os.getcwd())

        root.destinationText.insert('1', self.destinationdirectory) 

    def savePath(self):

        p = open(finallpath, 'w+')
        p.write(root.destinationText.get())
        p.close()
            
    def saveFolders(self):
        f = open(finallfolder, 'w+')
        f.write(root.foldersText.get())
        f.close()

    def exitApp(self):
        exit()

w = Widget() 


def CreateWidgets():
     
    destinationLabel = Label(root, text ="Wybierz scieżkę:  ",
                            bg ="#E8D579")
    destinationLabel.grid(row = 1, column = 0,
                        pady = 5, padx = 5)
     
    root.destinationText = Entry(root, width = 50,
                                textvariable = destinationLocation)
    root.destinationText.grid(row = 1, column = 1,
                            pady = 5, padx = 5,
                            columnspan = 2)
     
    dest_browseButton = Button(root, text ="Wyszukaj",
                            command = w.DestinationBrowse, width = 15)
    dest_browseButton.grid(row = 1, column = 3,
                        pady = 5, padx = 5)

    foldersLabel = Label(root, text ="Wybierz liczbę folderów:  ",
                            bg ="#E8D579")
    foldersLabel.grid(row = 2, column = 0,
                        pady = 5, padx = 5)
     
    root.foldersText = Entry(root, width = 50,
                                textvariable = foldersLocation)
    root.foldersText.grid(row = 2, column = 1,
                            pady = 5, padx = 5,
                            columnspan = 2)
     
    acceptButton = Button(root, text ="Zatwierdź scieżkę",
                        command = w.savePath, width = 15)
    acceptButton.grid(row = 1, column = 4,
                    pady = 5, padx = 5)

    numberButton = Button(root, text ="Zatwierdź liczbę folderów",
                        command = w.saveFolders, width = 20)
    numberButton.grid(row = 2, column = 4,
                    pady = 5, padx = 5)

    exitButton = Button(root, text ="Wyjdź",
                        command = w.exitApp, width = 20)
    exitButton.grid(row = 4, column = 2,
                    pady = 5, padx = 5)

root = tk.Tk()
     
root.geometry("830x120")
root.title("Ustawienia")
root.config(background = "black")
     
# Creating tkinter variable
destinationLocation = StringVar()
foldersLocation = IntVar()
     
CreateWidgets()
     
root.mainloop()