from os import system, chdir
from msvcrt import getch

def YesOrNo():
    print("(Y/N)")
    while 1:
        try:
            choice = getch().decode("utf-8").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                raise
        except:
            print("Please Enter y or n")

def makeNew():
    print("1) New C++ Project")
    print("2) New Python Project")
    print("3) New Java Project")
    print("4) New web Project")
    print("5) New rust Project")
    print("6) Cancel")
    while 1:
        try:
            choice = int(getch().decode("utf-8"))
            if choice > 6:
                raise
            break
        except:
            print("enter valid number")
    name = input("Enter Name: ")
    if choice == 1:
        makeNewC(name)
    elif choice == 2:
        makeNewPython(name)
    elif choice == 3:
        makeNewJava(name)
    elif choice == 4:
        makeNewWeb(name)
    elif choice == 5:
        makeNewRust(name)

def makeNewC(name):
    pass

def makeNewPython(name):
    path = "C:\\users\\shane\\dropbox\\desktop\\coding\\python\\"+name
    system("md "+path)
    chdir(path)
    system("gvim main.py")
    system("start cmd")

def makeNewJava(name):
    pass

def makeNewWeb(name):
    pass

def makeNewrust(name):
    pass

def makeNewRust(name):
    pass

makeNew()
