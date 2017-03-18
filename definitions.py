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
            win.update()
            time.sleep(0.10)
            (box).setFill("AntiqueWhite2")
            win.update()
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
            win.update()
            time.sleep(0.10)
            yes.setFill("AntiqueWhite2")
            win.update()
            return True
            time.sleep(0.25)
            break
        elif no_left < x_click < no_right and no_bottom < y_click < no_top:
            no.setFill("white")
            win.update()
            time.sleep(0.12)
            no.setFill("AntiqueWhite2")
            win.update()
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
            win.update()
            time.sleep(0.10)
            (box).setFill("AntiqueWhite2")
            win.update()
            return True

#ListAppender
def ListAppender(left, right, top, bottom, location, boxapp, appender,
                 confirmlist, boxloc, x, y, xloc, yloc):
    
    reader= open("Pickler.py", "rb")
    x_click, y_click=pickle.load(reader)
    reader.close()

    if left<x_click<right and bottom>y_click>top:

        if (appender) not in location:
            (location).append(appender)
            (boxloc).append(boxapp)
            boxapp.setFill("gray")
            xloc.append(x)
            yloc.append(y)

        elif (appender) in location and (appender) not in confirmlist:
            (location).remove(appender)
            (boxloc).remove(boxapp)
            boxapp.setFill("cyan4")
            xloc.remove(x)
            yloc.remove(y)

#Listoflistappenders1
def ListofListAppenders1():
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 60, 113, Player1_Locations,
                    boxrunner(BoxesP1A) ,stringrun(Astr), P1confirmlist,
                     P1BoxLoc, xreturn(), 1, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 113, 166, Player1_Locations,
                    boxrunner(BoxesP1B), stringrun(Bstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 2, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 166, 219, Player1_Locations,
                     boxrunner(BoxesP1C), stringrun(Cstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 3, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 219, 272, Player1_Locations,
                     boxrunner(BoxesP1D), stringrun(Dstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 4, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 272, 325, Player1_Locations,
                     boxrunner(BoxesP1E),stringrun(Estr), P1confirmlist,
                     P1BoxLoc, xreturn(), 5, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 325, 378, Player1_Locations,
                     boxrunner(BoxesP1F), stringrun(Fstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 6, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 378, 431, Player1_Locations,
                     boxrunner(BoxesP1G), stringrun(Gstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 7, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 431, 484, Player1_Locations,
                     boxrunner(BoxesP1H), stringrun(Hstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 8, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 484, 537, Player1_Locations,
                     boxrunner(BoxesP1I), stringrun(Istr), P1confirmlist,
                     P1BoxLoc, xreturn(), 9, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 537, 590, Player1_Locations,
                     boxrunner(BoxesP1J), stringrun(Jstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 10, P1x, P1y)
        
#Listoflistappenders2
def ListofListAppenders2():
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 60, 113, Player2_Locations,
                    boxrunner(BoxesP2A) ,stringrun(Astr), P2confirmlist,
                     P2BoxLoc, xreturn(), 1, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 113, 166, Player2_Locations,
                    boxrunner(BoxesP2B), stringrun(Bstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 2, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 166, 219, Player2_Locations,
                     boxrunner(BoxesP2C), stringrun(Cstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 3, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 219, 272, Player2_Locations,
                     boxrunner(BoxesP2D), stringrun(Dstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 4, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 272, 325, Player2_Locations,
                     boxrunner(BoxesP2E),stringrun(Estr), P2confirmlist,
                     P2BoxLoc, xreturn(), 5, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 325, 378, Player2_Locations,
                     boxrunner(BoxesP2F), stringrun(Fstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 6, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 378, 431, Player2_Locations,
                     boxrunner(BoxesP2G), stringrun(Gstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 7, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 431, 484, Player2_Locations,
                     boxrunner(BoxesP2H), stringrun(Hstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 8, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 484, 537, Player2_Locations,
                     boxrunner(BoxesP2I), stringrun(Istr), P2confirmlist,
                     P2BoxLoc, xreturn(), 9, P2x, P2y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 537, 590, Player2_Locations,
                     boxrunner(BoxesP2J), stringrun(Jstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 10, P2x, P2y)

#Attacker
def Attacker(left, right, top, bottom, ownbox, OPbox, OPboxconf, ownlist):
    reader= open("Pickler.py", "rb")
    x_click, y_click=pickle.load(reader)
    reader.close()

    if left<x_click<right and bottom>y_click>top:

        if OPbox in OPboxconf:
            ownbox.setFill("brown2")
            
        elif OPbox not in OPboxconf:
            ownbox.setFill("ghost white")

        if OPbox not in ownlist:
            ownlist.append(OPbox)

#Attack1
def attack1():
    for i in range(10):
        Attacker(leftatt(), rightatt(), 60, 113, boxrunner(BoxesP1ATT_A),
                 boxrunner2(BoxesP2A), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 113, 166, boxrunner(BoxesP1ATT_B),
                 boxrunner2(BoxesP2B), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 166, 219, boxrunner(BoxesP1ATT_C),
                 boxrunner2(BoxesP2C), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 219, 272, boxrunner(BoxesP1ATT_D),
                 boxrunner2(BoxesP2D), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 272, 325, boxrunner(BoxesP1ATT_E),
                 boxrunner2(BoxesP2E), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 325, 378, boxrunner(BoxesP1ATT_F),
                 boxrunner2(BoxesP2F), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 378, 431, boxrunner(BoxesP1ATT_G),
                 boxrunner2(BoxesP2G), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 431, 484, boxrunner(BoxesP1ATT_H),
                 boxrunner2(BoxesP2H), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 484, 537, boxrunner(BoxesP1ATT_I),
                 boxrunner2(BoxesP2I), P2BoxConf, P1att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 537, 590, boxrunner(BoxesP1ATT_J),
                 boxrunner2(BoxesP2J), P2BoxConf, P1att)

#Attack2
def attack2():
    for i in range(10):
        Attacker(leftatt(), rightatt(), 60, 113, boxrunner(BoxesP2ATT_A),
                 boxrunner2(BoxesP1A), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 113, 166, boxrunner(BoxesP2ATT_B),
                 boxrunner2(BoxesP1B), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 166, 219, boxrunner(BoxesP2ATT_C),
                 boxrunner2(BoxesP1C), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 219, 272, boxrunner(BoxesP2ATT_D),
                 boxrunner2(BoxesP1D), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 272, 325, boxrunner(BoxesP2ATT_E),
                 boxrunner2(BoxesP1E), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 325, 378, boxrunner(BoxesP2ATT_F),
                 boxrunner2(BoxesP1F), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 378, 431, boxrunner(BoxesP2ATT_G),
                 boxrunner2(BoxesP1G), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 431, 484, boxrunner(BoxesP2ATT_H),
                 boxrunner2(BoxesP1H), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 484, 537, boxrunner(BoxesP2ATT_I),
                 boxrunner2(BoxesP1I), P1BoxConf, P2att)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 537, 590, boxrunner(BoxesP2ATT_J),
                 boxrunner2(BoxesP1J), P1BoxConf, P2att)

#InARow
def in_a_row(ship, win):
    if ship is "Aircraft":
        
        if P1y[1]-P1y[0] is 0:
            if P1y[2]-P1y[1] is 0: 
                if P1y[3]-P1y[2] is 0: 
                    if P1y[4]-P1y[3] is 0: 
                        return True
                    
        elif P1x[1]-P1x[0] is 0:
            if P1x[2]-P1x[1] is 0:
                if P1x[3]-P1x[2] is 0:
                    if P1x[4]-P1x[3] is 0:
                        return True

    elif ship is "Battleship":

        print(P1x)
        print(P1x[4])
        
        if P1y[6]-P1y[5] is 0:
            if P1y[7]-P1y[6] is 0:
                if P1y[8]-P1y[7] is 0:
                    return True

        elif P1x[6]-P1x[5] is 0:
            if P1x[7]-P1x[6] is 0:
                if P1x[8]-P1x[7] is 0:
                    return True

    elif ship is "Frigate":

        if P1y[10]-P1y[9] is 0:
            if P1y[11]-P1y[10] is 0:
                return True

        elif P1x[10]-P1x[9] is 0:
            if P1x[11]-P1x[10] is 0:
                return True

    elif ship is "Submarine":

        if P1y[13]-P1y[12] is 0:
            if P1y[14]-P1y[13] is 0:
                return True

        elif P1x[13]-P1x[12] is 0:
            if P1x[14]-P1x[13] is 0:
                return True

    elif ship is "Patrol":

        if P1y[16]-P1y[15] is 0:
            return True

        elif P1x[16]-P1x[15] is 0:
            return True
    
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

#Numberx
def xreturn():
    global xval
    xval=xval+1
    if xval is 11:
        xval=1
    return xval

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

    for i in P1text:
        i.draw(win)

    for box in P1BoxConf:
        if box in P2att:
            box.setFill("brown2")

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

    for box in P2BoxConf:
        if box in P1att:
            box.setFill("brown2")
    
    
    
