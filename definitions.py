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

#singledetectorconf
def single_detector_conf(ok_left, ok_right, ok_top, ok_bottom, box, win, ship, conflist):
    
    global P1confirmlist, P2confirmlist, badlist
    global P1x, P1y, P2x, P2y
    
    try:
            reciever= open("Pickler.py", "rb")
            clicks=pickle.load(reciever)
            reciever.close()
            x_click, y_click= clicks
    except:
            NameError

    if ok_left< x_click < ok_right and ok_bottom < y_click < ok_top:
        if in_a_row(ship, conflist) is True and near(ship, conflist) is True:
            (box).setFill("white")
            win.update()
            time.sleep(0.15)
            (box).setFill("AntiqueWhite2")
            win.update()

            if conflist is P1confirmlist:
                P1x=[]
                P1y=[]
            elif conflist is P2confirmlist:
                P2x=[]
                P2y=[]                   
            return True
        
        else:
            badlist=[]
            box.setFill("brown2")
            win.update()
            time.sleep(0.15)
            box.setFill("AntiqueWhite2")
            win.update()

#Normal singledetector
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

#Checker
def checker(ship, shipstring ,attacklist, ognum, comparenum, box, win):
    for i in ship:
        if i in attacklist:
            ognum=ognum+1
    if ognum is comparenum:
        box.setFill("#f44141")
        if ship== Aircraft2 or ship==Bship2 or ship==Pat2 or ship==Sub2 or ship==Frig2:
            if shipstring in shipsP1:
                message= Text(Point(1175, 160), "Player 2's %s" %shipstring)
                message2= Text(Point(1175, 180), "has sunken!")
                message.draw(win)
                message2.draw(win)
                shipsP1.remove(shipstring)

        if ship==Aircraft1 or ship==Bship1 or ship==Pat1 or ship==Sub1 or ship==Frig1:
            if shipstring in shipsP2:
                message= Text(Point(1175, 160), "Player 1's %s" %shipstring)
                message2= Text(Point(1175, 180), "has sunken!")
                message.draw(win)
                message2.draw(win)
                shipsP2.remove(shipstring)
    else:
        box.setFill("SpringGreen2")
            
    win.update()
    ognum=0

#InARow
def in_a_row(ship, conflist):
    global P1x, P1y, P2x, P2y
    global P1confirmlist, P2confirmlist
    
    if conflist is P1confirmlist:
        y=P1y
        x=P1x

    elif conflist is P2confirmlist:
        y=P2y
        x=P2x
        
    if ship is "Aircraft":
        
        if y[1]-y[0] is 0:
            if y[2]-y[1] is 0: 
                if y[3]-y[2] is 0: 
                    if y[4]-y[3] is 0:
                        return True
                    
        elif x[1]-x[0] is 0:
            if x[2]-x[1] is 0:
                if x[3]-x[2] is 0:
                    if x[4]-x[3] is 0:
                        return True

    elif ship is "Battleship":
        
        if y[1]-y[0] is 0:
            if y[2]-y[1] is 0:
                if y[3]-y[2] is 0:
                    return True

        elif x[1]-x[0] is 0:
            if x[2]-x[1] is 0:
                if x[3]-x[2] is 0:
                    return True

    elif ship is "Frigate":

        if y[1]-y[0] is 0:
            if y[2]-y[1] is 0:
                return True

        elif x[1]-x[0] is 0:
            if x[2]-x[1] is 0:
                return True

    elif ship is "Submarine":

        if y[1]-y[0] is 0:
            if y[2]-y[1] is 0:
                return True

        elif x[1]-x[0] is 0:
            if x[2]-x[1] is 0:
                return True

    elif ship is "Patrol":

        if y[1]-y[0] is 0:
            return True

        elif x[1]-x[0] is 0:
            return True
    
#Near
def near(ship, conflist):
    global P1x, P1y, P2x, P2y
    global P1confirmlist, P2confirmlist, badlist

    if conflist is P1confirmlist:
        y=P1y
        x=P1x

    elif conflist is P2confirmlist:
        y=P2y
        x=P2x

    badlist=[]

    if ship is "Aircraft":
    
        if repeat(y, x, 1, 0) or repeat(y, x, 1, 2) or repeat(y, x, 1, 3)  or repeat(y, x, 1, 4):
            if repeat(y, x, 2, 0) or repeat(y, x, 2, 1) or repeat(y, x, 2, 3) or repeat(y, x, 2, 4):
                if repeat(y, x, 3, 0) or repeat(y, x, 3, 1) or repeat(y, x, 3, 2) or repeat(y, x, 3, 4):
                    if repeat(y, x, 4, 0) or repeat(y, x, 4, 1) or repeat(y, x, 4, 2) or repeat(y, x, 4, 3):
                        return True           

    elif ship is "Battleship":

        if repeat(y, x, 1, 0) or repeat(y, x, 1, 2) or repeat(y, x, 1, 3):
            if repeat(y, x, 2, 0) or repeat(y, x, 2, 1) or repeat(y, x, 2, 3):
                if repeat(y, x, 3, 0) or repeat(y, x, 3, 1) or repeat(y, x, 3, 2):
                    return True

    elif ship is "Frigate":

        if repeat(y, x, 1, 0) or repeat(y, x, 1, 2):
            if repeat(y, x, 2, 0) or repeat(y, x, 2, 1):
                return True

    elif ship is "Submarine":

        if repeat(y, x, 1, 0) or repeat(y, x, 1, 2):
            if repeat(y, x, 2, 0) or repeat(y, x, 2, 1):
                return True
            
    elif ship is "Patrol":
        if repeat(y, x, 1, 0):
            return True
        
#Distance
def dist(y, x , i, i2):
    if (((y[i]-y[i2])**2)+((x[i]-x[i2])**2))**0.5 == 1:
        return True

#repeatchecker
def repeat(xlist, ylist, x,y):
    global badlist
    if (x, y) not in badlist:
        if dist(xlist, ylist, x,y) is True: 
            li=(y,x)
            badlist.append(li)
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

    OPship_line.draw(win)
    dialogue_line.draw(win)
    fleet_line.draw(win)
    radar_line.draw(win)
    
    other_player_ships_title.draw(win)
    bshiptext.draw(win)
    airtext.draw(win)
    subtext.draw(win)
    pattext.draw(win)
    frigtext.draw(win)
    
    fleet_title.draw(win)
    radar_title.draw(win)
    text_box_title.draw(win)
    
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

    for i in text:
        i.setSize(15)
    for i in nums:
        i.setSize(15)

    for i in text:
        i.draw(win)
    for i in nums:
        i.draw(win)

    for box in P1BoxConf:
        if box in P2att:
            box.setFill("brown2")

#Drawer2
def drawer2(win):

    dialogue_line.draw(win)
    OPship_line.draw(win)
    fleet_line.draw(win)
    radar_line.draw(win)

    bshiptext.draw(win)
    airtext.draw(win)
    subtext.draw(win)
    pattext.draw(win)
    frigtext.draw(win)

    other_player_ships_title.draw(win)
    fleet_title.draw(win)
    radar_title.draw(win)
    text_box_title.draw(win)

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

    for i in text:
        i.setSize(15)
    for i in nums:
        i.setSize(15)

    for i in text:
        i.draw(win)
    for i in nums:
        i.draw(win)

    for box in P2BoxConf:
        if box in P1att:
            box.setFill("brown2")


