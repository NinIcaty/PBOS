#The os's path
ospath = "/home/firefly/PycharmProjects/PBOS"
import os
import requests
import curses
def input_multi(prompt):
    print(prompt)
    text = ''
    while True:
        newtext = input()
        if newtext == '':
            break
        text = text + "\n" + newtext
    return text
"""
commands
cd
ls
nano
pacin
mkdir
touch
runpk
read
rdr
"""



os.chdir("Files")
VarCurrentDir = "Files"
VarPreCurdir = "Files"
I = 1
II = 2
print('welcome to PBOS\nversion pre alpha 5.2\nwebsite arul.net.in ')
while I < II:
    II += 1
    I += 1

    print(VarCurrentDir)
    VarCommand = input()
    if VarCommand == "cd":
       Varcd_dir = input("cd where\n")
       if os.path.isdir(Varcd_dir) == True:
           os.chdir(Varcd_dir)

           VarCurrentDir = VarPreCurdir+"/"+Varcd_dir
           VarPreCurdir = VarCurrentDir
           print("Changed Diretory")
       else:
            print('directory does not exsist')
    elif VarCommand == "rdr":
        VarDirR = input("Directory to delete\n")
        path = ospath+"/"+VarCurrentDir+"/"+VarDirR
        if os.path.isdir(VarDirR):
            os.rmdir(path)
            print('deleted directory')
        else: print(path +"does not exsist or is not a directory")
    elif VarCommand == "ls":
        VarlsDir = input('List Directory name\n(leave blank for All files)\n')
        if VarlsDir != '':
            VarlsDir = "/" + VarlsDir
            path = ospath+"/Files" + VarlsDir
            print(os.listdir(path))
        else:
            path = ospath+"/Files"
            print(os.listdir(path))
    elif VarCommand == "touch":
        Filename = input("file name\n")

        path = ospath+"/" + VarCurrentDir
        if os.path.isfile(Filename) == False:


            open(os.path.join(path,Filename),'x')
            print("file created")
        else:
            print('file already exsists')
    elif VarCommand == "read":
        FileShow = input('which file\n')
        path = ospath+"/Files/" + FileShow
        if os.path.isfile(FileShow) == True:

            FileShowWithFile = ospath+"/Files/"+FileShow
            file = open(FileShowWithFile)

            for n in file:
                print(n)
        else:
            print("file does not exsist")
    elif VarCommand == "nano":
        EditFile = input("Which file would you like to edit\n")

        if os.path.isfile(ospath+"/Files/"+EditFile) == True:

            fileAdd = input_multi('Data')
            with open(ospath+"/Files/"+EditFile,'a') as file:
                file.write(fileAdd)
        else:
            print(ospath+"/Files/"+EditFile)
            print("file does not exsist")
    elif VarCommand == "mkdir":
        path = ospath+"/"+VarCurrentDir
        VarNewDir = input('new directory name\n')
        if os.path.isdir(VarNewDir) == False:
            os.mkdir(os.path.join(path,VarNewDir))
        else:
            print("directory already exsists\n")
    elif VarCommand == "runpk":
        pkgname = input('package name no file extention\n')
        pkgtype = input('type\n')

        if pkgtype == 'python':
            exec(open(ospath+'/WebPacks/'+pkgname+".py").read())
        elif pkgtype == 'java':
            os.system("java -jar "+pkgname+".jar")

    elif VarCommand == "pacin":

        url = input('URL to clone from\n')
        saveas = input('\nwhat should it be saved as?\n')
        r = requests.get(url)
        path = ospath+"/WebPacks/"
        open(path+saveas,'wb').write(r.content)
        print('downloaded!\n')
    elif VarCommand == "rmf":
        VarRemove = input('What file to delete?\n')
        path = ospath + "/Files/" + VarRemove
        if os.path.isfile(path) == True:
            os.remove(path)
            print('file deleted')
        else: print(path + " is not a file")

    elif VarCommand == "off":
        print('powering off')
        break
    else:
        print("ERROR\n")
