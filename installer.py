import os
import sys
import winreg as reg


# Get path of current working directory and python.exe
def setting():
    cwd = os.getcwd()
    python_exe = sys.executable

    # optional hide python terminal in windows
    hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"


    # Set the path of the context menu (right-click menu)
    key_path = r'Directory\\Background\\shell\\Organiser\\' # Change 'Organiser' to the name of your project

    # Create outer key
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, '', reg.REG_SZ, '&Ustawienia kopiowania')  # Change 'Organise folder' to the function of your script

    # create inner key
    key1 = reg.CreateKey(key, r"command")
    reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\choosingDirectory.py"') # change 'file_organiser.py' to the name of your script
    reg.SetValue(key1, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\choosingDirectory.py"')  # use to to hide terminal
def copy():
    cwd = os.getcwd()
    python_exe = sys.executable

    # optional hide python terminal in windows
    hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"


    # Set the path of the context menu (right-click menu)
    key_path = r'Directory\\Background\\shell\\Copying\\' # Change 'Organiser' to the name of your project

    # Create outer key
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
    reg.SetValue(key, '', reg.REG_SZ, '&Kopiuj ze strukturą')  # Change 'Organise folder' to the function of your script

    # create inner key
    key1 = reg.CreateKey(key, r"command")
    reg.SetValue(key1, '', reg.REG_SZ, python_exe + f'"{cwd}\\copyWithPath.py"') # change 'file_organiser.py' to the name of your script
    reg.SetValue(key1, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\copyWithPath.py"')  # use to to hide terminal

setting(), copy()