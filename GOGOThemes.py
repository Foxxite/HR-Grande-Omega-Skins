from tkinter import *
import sys, os
from distutils.dir_util import copy_tree
import shutil

if os.path.exists("./bin/"):
    print("Bin found")
    print("99% certain this is an auto")
    version = "auto"
elif os.path.exists("./resources/"):
    print("99% certain this is manual")
    version = "manual"
else:
    version = "?"

#checkt for skins
if os.path.exists("./skins/"):
    print("skins found")
    allskins = (os.listdir("./skins/"))
    print(allskins)
else:
    print("please ensure you have a skins folder")

##################################################
#           First test                           #
##################################################

def RemovePathRecusive(path):
    #haalt de path weg
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
        except:
            pass
print(version + " Is this correct?")
def apply(Go_Thema):
    print("going to apply {} skin to grand omega".format(Go_Thema))
    if version == "?":
        print("where is your Grand omega located?")
    elif version == "auto":
        RemovePathRecusive("./bin/wwwroot/css/")
        RemovePathRecusive("./bin/wwwroot/themes/")
        RemovePathRecusive("./bin/wwwroot/assets/")
        if os.path.exists("./skins/{}/wwwroot".format(Go_Thema)):
            print("main route")
            fromdir = "./skins/{}/".format(Go_Thema)
            todir = "./bin/"
            copy_tree(fromdir, todir)
        elif os.path.exists("./skins/{}/resources/app/desktop/student/wwwroot".format(Go_Thema)):
            print("diffrent route")
            fromdir = "./skins/{}/resources/app/desktop/student/".format(Go_Thema)
            todir = "./bin/"
            copy_tree(fromdir, todir)

            fromdir = "./themes/"
            todir = "./bin/wwwroot/"
            copy_tree(fromdir, todir)
        else:
            print("waar de fk heb je alle bestanden gelaten?")
    elif version == "manual":
        RemovePathRecusive("./resources/app/desktop/Student/wwwroot/css/")
        RemovePathRecusive("./resources/app/desktop/Student/themes/")
        RemovePathRecusive("./resources/app/desktop/Student/assets/")
        if os.path.exists("./skins/{}/wwwroot".format(Go_Thema)):
            print("main route")
            fromdir = "./skins/{}/".format(Go_Thema)
            todir = "./resources/app/desktop/Student"
            copy_tree(fromdir, todir)
        elif os.path.exists("./skins/{}/resources/app/desktop/student/wwwroot".format(Go_Thema)):
            print("diffrent route")
            fromdir = "./skins/{}/resources/app/desktop/student/".format(Go_Thema)
            todir = "./resources/app/desktop/Student"
            copy_tree(fromdir, todir)

            fromdir = "./themes/"
            todir = "./skins/{}/resources/app/desktop/student/wwwroot/"
            copy_tree(fromdir, todir)

#innit root en frame voor root
root = Tk()
frame = Frame(width=500, height=400, bg="darkgrey")

themaH = 10
themaW = 10

l = Label(frame, text="momenteel werkt dit alleen \n op de auto-installer versie", bg="darkgrey")
l.place(x=90, y=10)
#thanks in een fout in tkinter doet het telkens de command voor ALLEEEN de laatste in de Array allthemes....
#for thema in allskins:
#    print(thema)
#########################################################################################################
#       Shit code, niet op letten, deed het eerst via een For loop alleen hayk's theme brak het telkens #
#   TODO: Post on r/programming Horror                                                                  #
#########################################################################################################
aLab = Label(frame, text=str(allskins[0]), bg="darkgrey")
aLab.place(x=themaW, y=themaH)

themaH += 30
aBut = Button(frame, text=str("apply"), command=lambda:apply(allskins[0]))
aBut.place(x=themaW, y=themaH)
themaH += 40

aLab = Label(frame, text=str(allskins[1]), bg="darkgrey")
aLab.place(x=themaW, y=themaH)

themaH += 30
aBut = Button(frame, text=str("apply"), command=lambda:apply(allskins[1]))
aBut.place(x=themaW, y=themaH)
themaH += 40
aLab = Label(frame, text=str(allskins[2]), bg="darkgrey")
aLab.place(x=themaW, y=themaH)

themaH += 30
aBut = Button(frame, text=str("apply"), command=lambda:apply(allskins[2]))
aBut.place(x=themaW, y=themaH)

frame.pack()
#dit voorkomt dat de frame geresized kan worden verkomt lelijkheid(synoniem = ik)
root.resizable(False, False)
root.title("GO GO Themes")
# v belangrijkste van het userform
root.mainloop()
