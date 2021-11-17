import os
os.system('start /B start cmd.exe @cmd /k pip install tkinter')
os.system('start /B start cmd.exe @cmd /k pip install shutil')
os.system('start /B start cmd.exe @cmd /k pip install webbrowser')

os.system('start /B start cmd.exe @cmd /k python installer.py')