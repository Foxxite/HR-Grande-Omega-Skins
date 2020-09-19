from tkinter import *
import sys, os
from distutils.dir_util import copy_tree
import shutil

if os.path.exists("./bin"):
    print("Bin found")
    if os.path.exists("./bin/wwwroot/"):
        print("wwwroot found")
    if os.path.exists("./bin/index.html"):
        print("Index.html found")
    if os.path.exists("./bin/main.js"):
        print("main.js found")
else:
    print("is dit wel de GO directory?")

#checkt for skins
if os.path.exists("./skins/"):
    print("skins found")
    allskins = (os.listdir("./skins/"))
else:
    print("please ensure you have a skins folder")

##################################################
#           First test                           #
##################################################


def apply(Go_Thema):
    print("going {}".format(Go_Thema))
    # kijkt of de dir bestaat zoja remove
    if os.path.exists("./bin/wwwroot/css/"):
        try:
            shutil.rmtree("./bin/wwwroot/css/")
        except:
            print("Error")
        print("rm css")
    if os.path.exists("./bin/wwwroot/themes/"):
        try:
            shutil.rmtree("./bin/wwwroot/themes/")
        except:
            print("Error")
        print("rm themes")
    if os.path.exists("./bin/wwwroot/assets/"):
        try:
            shutil.rmtree("./bin/wwwroot/assets/")
        except:
            print("Error")
        print("rm assets")

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

    
    #Kamikaze
    root.destroy()


#innit root en frame voor root
root = Tk()
frame = Frame(width=500, height=400, bg="darkgrey")

themaH = 10
themaW = 10

l = Label(frame, text="momenteel werkt dit alleen \n op de auto-installer versie", bg="darkgrey")
l.place(x=90, y=10)
#thanks in een fout in tkinter doet het telkens de command voor ALLEEEN de laatste in de Array allthemes....
for thema in allskins:
    print(thema)
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
