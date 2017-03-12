import time
import pickle
import zellegraphics
from var import *

#next_detector
def next_detector(ok_left, ok_right, ok_top, ok_bottom, box, win):
    while True:
        click= win.getMouse()
        x_click=click.getX()
        y_click=click.getY()
        if ok_left< x_click < ok_right and ok_bottom < y_click < ok_top:
            (box).setFill("white")
            time.sleep(0.10)
            (box).setFill("AntiqueWhite2")
            break

#Yes/No
def yes_no_detector(yes_left, yes_right, yes_top, yes_bottom, no_left, no_right
                    , no_top, no_bottom, win, yes, no):
    while True:
        click= win.getMouse()
        x_click=click.getX()
        y_click=click.getY()
        if yes_left < x_click < yes_right and yes_bottom < y_click < yes_top:
            yes.setFill("white")
            time.sleep(0.10)
            yes.setFill("AntiqueWhite2")
            return True
            time.sleep(0.25)
            break
        elif no_left < x_click < no_right and no_bottom < y_click < no_top:
            no.setFill("white")
            time.sleep(0.12)
            no.setFill("AntiqueWhite2")
            return False
            break

###########################################################################

#singledetector
def single_detector(ok_left, ok_right, ok_top, ok_bottom, box, win):
        try:
                reciever= open("Pickler.py", "rb")
                clicks=pickle.load(reciever)
                reciever.close()
                x_click, y_click= clicks
        except:
                NameError

        if ok_left< x_click < ok_right and ok_bottom < y_click < ok_top:
            (box).setFill("white")
            time.sleep(0.10)
            (box).setFill("AntiqueWhite2")
            return True

#ListAppender
def ListAppender(left, right, top, bottom, location, boxapp, appender,
                 confirmlist, boxloc):
    
    reader= open("Pickler.py", "rb")
    x_click, y_click=pickle.load(reader)
    reader.close()

    if left<x_click<right and bottom>y_click>top:

        if (appender) not in location:
            (location).append(appender)
            (boxloc).append(boxapp)
            boxapp.setFill("gray")

        elif (appender) in location and (appender) not in confirmlist:
            (location).remove(appender)
            (boxloc).remove(boxapp)
            boxapp.setFill("cyan4")

#Listoflistappenders1
def ListofListAppenders1():
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 60, 113, Player1_Locations,
                    boxrunner(BoxesP1A) ,stringrun(Astr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 113, 166, Player1_Locations,
                    boxrunner(BoxesP1B), stringrun(Bstr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 166, 219, Player1_Locations,
                     boxrunner(BoxesP1C), stringrun(Cstr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 219, 272, Player1_Locations,
                     boxrunner(BoxesP1D), stringrun(Dstr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 272, 325, Player1_Locations,
                     boxrunner(BoxesP1E),stringrun(Estr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 325, 378, Player1_Locations,
                     boxrunner(BoxesP1F), stringrun(Fstr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 378, 431, Player1_Locations,
                     boxrunner(BoxesP1G), stringrun(Gstr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 431, 484, Player1_Locations,
                     boxrunner(BoxesP1H), stringrun(Hstr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 484, 537, Player1_Locations,
                     boxrunner(BoxesP1I), stringrun(Istr), P1confirmlist, P1BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 537, 590, Player1_Locations,
                     boxrunner(BoxesP1J), stringrun(Jstr), P1confirmlist, P1BoxLoc)
        
#Listoflistappenders2
def ListofListAppenders2():
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 60, 113, Player2_Locations,
                    boxrunner(BoxesP2A) ,stringrun(Astr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 113, 166, Player2_Locations,
                    boxrunner(BoxesP2B), stringrun(Bstr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 166, 219, Player2_Locations,
                     boxrunner(BoxesP2C), stringrun(Cstr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 219, 272, Player2_Locations,
                     boxrunner(BoxesP2D), stringrun(Dstr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 272, 325, Player2_Locations,
                     boxrunner(BoxesP2E),stringrun(Estr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 325, 378, Player2_Locations,
                     boxrunner(BoxesP2F), stringrun(Fstr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 378, 431, Player2_Locations,
                     boxrunner(BoxesP2G), stringrun(Gstr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 431, 484, Player2_Locations,
                     boxrunner(BoxesP2H), stringrun(Hstr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 484, 537, Player2_Locations,
                     boxrunner(BoxesP2I), stringrun(Istr), P2confirmlist, P2BoxLoc)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 537, 590, Player2_Locations,
                     boxrunner(BoxesP2J), stringrun(Jstr), P2confirmlist, P2BoxLoc)

#Attacker
def Attacker(left, right, top, bottom, ownbox, OPbox, OPboxconf):
    reader= open("Pickler.py", "rb")
    x_click, y_click=pickle.load(reader)
    reader.close()

    if left<x_click<right and bottom>y_click>top:

        if OPbox in OPboxconf:
            ownbox.setFill("red")

        elif OPbox not in OPboxconf:
            ownbox.setFill("white")

#AttackAppender1
def attack1():
    for i in range(10):
        Attacker(leftatt(), rightatt(), 60, 113, boxrunner(BoxesP1ATT_A),
                 boxrunner2(BoxesP2A), P2BoxConf)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 113, 166, boxrunner(BoxesP1ATT_B),
                 boxrunner2(BoxesP2B), P2BoxConf)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 166, 219, boxrunner(BoxesP1ATT_C),
                 boxrunner2(BoxesP2C), P2BoxConf)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 219, 272, boxrunner(BoxesP1ATT_D),
                 boxrunner2(BoxesP2D), P2BoxConf)

        
            
#Leftbound
def leftbound():
    global xvar
    xvar=xvar+1
    if xvar is 10:
        xvar=0
    return (35+(49.5*xvar))

#Rightbound
def rightbound():
    global yvar
    yvar=yvar+1
    if yvar is 10:
        yvar=0
    return (84.5+(49.5*yvar))

#LeftboundForATT
def leftatt():
    global leftvar
    leftvar=leftvar+1
    if leftvar is 10:
        leftvar=0
    return (590+(49.5*leftvar))

#RightboundForATT
def rightatt():
    global rightvar
    rightvar=rightvar+1
    if rightvar is 10:
        rightvar=0
    return (639.5+(49.5*rightvar))

#StringLooper
def stringrun(li):
    global liststart
    liststart=liststart+1
    if liststart is 9:
        liststart=-1
    return li[liststart]

#Boxrunner
def boxrunner(li):
    global boxvar
    boxvar=boxvar+1
    if boxvar is 9:
        boxvar=-1
    return li[boxvar]

#Boxrunner2
def boxrunner2(li):
    global brun
    brun=brun+1
    if brun is 9:
        brun=-1
    return li[brun]

#clickgetter
def click_getter(win):
        click=win.getMouse()
        x_click=click.getX()
        y_click=click.getY()
        clicknames=(x_click, y_click)

        writer= open("Pickler.py", "wb")
        pickle.dump(clicknames, writer, protocol=2)
        writer.close()
        return x_click, y_click

#Drawer
def drawer1(win):
    for i in BoxesP1A:
        i.draw(win)
    for i in BoxesP1B:
        i.draw(win)
    for i in BoxesP1C:
        i.draw(win)
    for i in BoxesP1D:
        i.draw(win)
    for i in BoxesP1E:
        i.draw(win)
    for i in BoxesP1F:
        i.draw(win)
    for i in BoxesP1G:
        i.draw(win)
    for i in BoxesP1H:
        i.draw(win)
    for i in BoxesP1I:
        i.draw(win)
    for i in BoxesP1J:
        i.draw(win)
        
    for i in BoxesP1ATT_A:
        i.draw(win)
    for i in BoxesP1ATT_B:
        i.draw(win)
    for i in BoxesP1ATT_C:
        i.draw(win)
    for i in BoxesP1ATT_D:
        i.draw(win)
    for i in BoxesP1ATT_E:
        i.draw(win)
    for i in BoxesP1ATT_F:
        i.draw(win)
    for i in BoxesP1ATT_G:
        i.draw(win)
    for i in BoxesP1ATT_H:
        i.draw(win)
    for i in BoxesP1ATT_I:
        i.draw(win)
    for i in BoxesP1ATT_J:
        i.draw(win)

#Drawer2
def drawer2(win):
    for i in BoxesP2A:
        i.draw(win)
    for i in BoxesP2B:
        i.draw(win)
    for i in BoxesP2C:
        i.draw(win)
    for i in BoxesP2D:
        i.draw(win)
    for i in BoxesP2E:
        i.draw(win)
    for i in BoxesP2F:
        i.draw(win)
    for i in BoxesP2G:
        i.draw(win)
    for i in BoxesP2H:
        i.draw(win)
    for i in BoxesP2I:
        i.draw(win)
    for i in BoxesP2J:
        i.draw(win)

    for i in BoxesP2ATT_A:
        i.draw(win)
    for i in BoxesP2ATT_B:
        i.draw(win)
    for i in BoxesP2ATT_C:
        i.draw(win)
    for i in BoxesP2ATT_D:
        i.draw(win)
    for i in BoxesP2ATT_E:
        i.draw(win)
    for i in BoxesP2ATT_F:
        i.draw(win)
    for i in BoxesP2ATT_G:
        i.draw(win)
    for i in BoxesP2ATT_H:
        i.draw(win)
    for i in BoxesP2ATT_I:
        i.draw(win)
    for i in BoxesP2ATT_J:
        i.draw(win)
    
    
    
