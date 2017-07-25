import pygame
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
        
        elif no_left < x_click < no_right and no_bottom < y_click < no_top:
            no.setFill("white")
            win.update()
            time.sleep(0.12)
            no.setFill("AntiqueWhite2")
            win.update()
            return False

###########################################################################

#singledetectorconf
def single_detector_conf(ok_left, ok_right, ok_top, ok_bottom, box, win, ship,
                         conflist, soundvar):
    
    global P1confirmlist, P2confirmlist
    global P1x, P1y, P2x, P2y
    
    reciever= open("Pickler.py", "rb")
    clicks=pickle.load(reciever)
    reciever.close()
    x_click, y_click= clicks

    if ok_left< x_click < ok_right and ok_bottom < y_click < ok_top:
        if in_a_row(ship, conflist) is True and near(ship, conflist) is True:
            if soundvar:
                sound= pygame.mixer.Sound("confirm.ogg")
                sound.play()
            
            (box).setFill("white")
            win.update()
            time.sleep(0.30)
            (box).setFill("AntiqueWhite")
            win.update()

            if conflist is P1confirmlist:
                P1x=[]
                P1y=[]
                
            elif conflist is P2confirmlist:
                P2x=[]
                P2y=[]
                
            return True
        
        else:
            if soundvar:
                sound=pygame.mixer.Sound("error.ogg")
                sound.play()
            
            box.setFill("brown2")
            win.update()
            time.sleep(0.15)
            box.setFill("AntiqueWhite")
            win.update()

#Normal singledetector
def single_detector(ok_left, ok_right, ok_top, ok_bottom, box, win):
    
    reciever= open("Pickler.py", "rb")
    clicks=pickle.load(reciever)
    reciever.close()
    x_click, y_click= clicks

    if ok_left< x_click < ok_right and ok_bottom < y_click < ok_top:
        (box).setFill("white")
        win.update()
        time.sleep(0.10)
        (box).setFill("AntiqueWhite")
        win.update()
        return True

#musicplay
def musicplay(var, ok_left, ok_right, ok_top, ok_bottom, box, win):
    
    if single_detector(ok_left, ok_right, ok_top, ok_bottom, box, win) is True:
        if var==True:
            var=False
            pygame.mixer.music.stop()
            music_on.undraw()
            music_off.draw(win)

        else:
            var=True
            pygame.mixer.music.load("seamusic.mp3")
            pygame.mixer.music.play(-1)
            music_off.undraw()
            music_on.draw(win)
   
        return var

#soundplay
def soundplay(var, ok_left, ok_right, ok_top, ok_bottom, box, win):
    
     if single_detector(ok_left, ok_right, ok_top, ok_bottom, box, win) is True:
        if var==True:
            var=False
            sound_on.undraw()
            sound_off.draw(win)

        else:
            var=True
            sound_off.undraw()
            sound_on.draw(win)

        return var

#ListAppender
def ListAppender(left, right, top, bottom, location, boxapp, appender,
                 confirmlist, boxloc, x, y, xloc, yloc, soundvar):
    
    reader= open("Pickler.py", "rb")
    x_click, y_click=pickle.load(reader)
    reader.close()

    if left<x_click<right and bottom>y_click>top:

        if (appender) not in location:
            boxapp.setFill("gray")
            (location).append(appender)
            (boxloc).append(boxapp)
            xloc.append(x)
            yloc.append(y)

        elif (appender) in location and (appender) not in confirmlist:
            boxapp.setFill("cyan4")
            (location).remove(appender)
            (boxloc).remove(boxapp)
            xloc.remove(x)
            yloc.remove(y)

        elif appender in confirmlist:
            if soundvar:
                sound=pygame.mixer.Sound("error.ogg")
                sound.play()

#Listoflistappenders1
def ListofListAppenders1(soundvar):
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 60, 113, Player1_Locations,
                    boxrunner(BoxesP1A) ,stringrun(Astr), P1confirmlist,
                     P1BoxLoc, xreturn(), 1, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 113, 166, Player1_Locations,
                    boxrunner(BoxesP1B), stringrun(Bstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 2, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 166, 219, Player1_Locations,
                     boxrunner(BoxesP1C), stringrun(Cstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 3, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 219, 272, Player1_Locations,
                     boxrunner(BoxesP1D), stringrun(Dstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 4, P1x, P1y)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 272, 325, Player1_Locations,
                     boxrunner(BoxesP1E),stringrun(Estr), P1confirmlist,
                     P1BoxLoc, xreturn(), 5, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 325, 378, Player1_Locations,
                     boxrunner(BoxesP1F), stringrun(Fstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 6, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 378, 431, Player1_Locations,
                     boxrunner(BoxesP1G), stringrun(Gstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 7, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 431, 484, Player1_Locations,
                     boxrunner(BoxesP1H), stringrun(Hstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 8, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 484, 537, Player1_Locations,
                     boxrunner(BoxesP1I), stringrun(Istr), P1confirmlist,
                     P1BoxLoc, xreturn(), 9, P1x, P1y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 537, 590, Player1_Locations,
                     boxrunner(BoxesP1J), stringrun(Jstr), P1confirmlist,
                     P1BoxLoc, xreturn(), 10, P1x, P1y, soundvar)
        
#Listoflistappenders2
def ListofListAppenders2(soundvar):
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 60, 113, Player2_Locations,
                    boxrunner(BoxesP2A) ,stringrun(Astr), P2confirmlist,
                     P2BoxLoc, xreturn(), 1, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 113, 166, Player2_Locations,
                    boxrunner(BoxesP2B), stringrun(Bstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 2, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 166, 219, Player2_Locations,
                     boxrunner(BoxesP2C), stringrun(Cstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 3, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 219, 272, Player2_Locations,
                     boxrunner(BoxesP2D), stringrun(Dstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 4, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 272, 325, Player2_Locations,
                     boxrunner(BoxesP2E),stringrun(Estr), P2confirmlist,
                     P2BoxLoc, xreturn(), 5, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 325, 378, Player2_Locations,
                     boxrunner(BoxesP2F), stringrun(Fstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 6, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 378, 431, Player2_Locations,
                     boxrunner(BoxesP2G), stringrun(Gstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 7, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 431, 484, Player2_Locations,
                     boxrunner(BoxesP2H), stringrun(Hstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 8, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 484, 537, Player2_Locations,
                     boxrunner(BoxesP2I), stringrun(Istr), P2confirmlist,
                     P2BoxLoc, xreturn(), 9, P2x, P2y, soundvar)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 537, 590, Player2_Locations,
                     boxrunner(BoxesP2J), stringrun(Jstr), P2confirmlist,
                     P2BoxLoc, xreturn(), 10, P2x, P2y, soundvar)

#Attacker
def Attacker(left, right, top, bottom, ownbox, OPbox, OPboxconf, ownlist,
             ownmiss, ownhit, soundvar):
    
    reader= open("Pickler.py", "rb")
    x_click, y_click=pickle.load(reader)
    reader.close()

    if left<x_click<right and bottom>y_click>top:

        if OPbox in OPboxconf:
            ownbox.setFill("brown2")
            if OPbox not in ownhit:
                ownhit.append(OPbox)

                if soundvar:
                    sound= pygame.mixer.Sound("hit.ogg")
                    sound.play()
                
            elif OPbox in ownhit:
                if soundvar:
                    sound= pygame.mixer.Sound("error.ogg")
                    sound.play()
            
        elif OPbox not in OPboxconf:
            ownbox.setFill("ghost white")
            if OPbox not in ownmiss:
                ownmiss.append(OPbox)
                if soundvar:
                    sound= pygame.mixer.Sound("miss.ogg")
                    sound.play()

            elif OPbox in ownmiss:
                if soundvar:
                    sound= pygame.mixer.Sound("error.ogg")
                    sound.play()
                
        if OPbox not in ownlist:
            ownlist.append(OPbox)

#Attack1
def attack1(soundvar):
    for i in range(10):
        Attacker(leftatt(), rightatt(), 60, 113, boxrunner(BoxesP1ATT_A),
                 boxrunner2(BoxesP2A), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 113, 166, boxrunner(BoxesP1ATT_B),
                 boxrunner2(BoxesP2B), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 166, 219, boxrunner(BoxesP1ATT_C),
                 boxrunner2(BoxesP2C), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 219, 272, boxrunner(BoxesP1ATT_D),
                 boxrunner2(BoxesP2D), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 272, 325, boxrunner(BoxesP1ATT_E),
                 boxrunner2(BoxesP2E), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 325, 378, boxrunner(BoxesP1ATT_F),
                 boxrunner2(BoxesP2F), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 378, 431, boxrunner(BoxesP1ATT_G),
                 boxrunner2(BoxesP2G), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 431, 484, boxrunner(BoxesP1ATT_H),
                 boxrunner2(BoxesP2H), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 484, 537, boxrunner(BoxesP1ATT_I),
                 boxrunner2(BoxesP2I), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 537, 590, boxrunner(BoxesP1ATT_J),
                 boxrunner2(BoxesP2J), P2BoxConf, P1att, P1miss, P1hit
                 , soundvar)

#Attack2
def attack2(soundvar):
    for i in range(10):
        Attacker(leftatt(), rightatt(), 60, 113, boxrunner(BoxesP2ATT_A),
                 boxrunner2(BoxesP1A), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 113, 166, boxrunner(BoxesP2ATT_B),
                 boxrunner2(BoxesP1B), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 166, 219, boxrunner(BoxesP2ATT_C),
                 boxrunner2(BoxesP1C), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 219, 272, boxrunner(BoxesP2ATT_D),
                 boxrunner2(BoxesP1D), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 272, 325, boxrunner(BoxesP2ATT_E),
                 boxrunner2(BoxesP1E), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 325, 378, boxrunner(BoxesP2ATT_F),
                 boxrunner2(BoxesP1F), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 378, 431, boxrunner(BoxesP2ATT_G),
                 boxrunner2(BoxesP1G), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 431, 484, boxrunner(BoxesP2ATT_H),
                 boxrunner2(BoxesP1H), P1BoxConf, P2att, P2miss, P2hit,
                 soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 484, 537, boxrunner(BoxesP2ATT_I),
                 boxrunner2(BoxesP1I), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)
    for i in range(10):
        Attacker(leftatt(), rightatt(), 537, 590, boxrunner(BoxesP2ATT_J),
                 boxrunner2(BoxesP1J), P1BoxConf, P2att, P2miss, P2hit
                 , soundvar)

#Checker
def checker(ship, shipstring ,attacklist, ognum, comparenum, box, win, name):
    
    for point in ship:
        if point in attacklist:
            ognum=ognum+1
            
    if ognum is comparenum:
        box.setFill("#f44141")
        if (ship== Aircraft2 or ship==Bship2 or ship==Pat2 or ship==Sub2 or
            ship==Frig2):
            if shipstring in shipsP2:
                message= Text(Point(1175, 140), "%(1)s's %(2)s"
                              %{"1": name, "2": shipstring})
                message2= Text(Point(1175, 155), "has sunken!")
    
                message.draw(win)
                message2.draw(win)
                shipsP2.remove(shipstring)

        if (ship==Aircraft1 or ship==Bship1 or ship==Pat1 or ship==Sub1 or
            ship==Frig1):
            if shipstring in shipsP1:
                message= Text(Point(1175, 140), "%(1)s's %(2)s"
                              %{"1": name, "2": shipstring})
                message2= Text(Point(1175, 155), "has sunken!")
            
                message.draw(win)
                message2.draw(win)
                shipsP1.remove(shipstring)
    else:
        box.setFill("SpringGreen2")
            
    win.update()
    ognum=0

#winner
def winner():
    if len(shipsP1)==0:
        return("Player2")
    elif len(shipsP2)==0:
        return("Player1")
                
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
            
    if ship=="Aircraft":
        if repeat(y, x, [(0,1), (0,2), (0,3), (0,4)]):
            if repeat(y, x, [(1,0), (1,2), (1,3), (1,4)]):
                if repeat(y, x, [(2,0), (2,1), (2,3), (2,4)]):
                    if repeat(y, x, [(3,0), (3,1), (3,2), (3,4)]):
                        if repeat(y, x, [(4,0), (4,1), (4,2), (4,3)]):
                            return True          

    elif ship=="Battleship":
        if repeat(y, x, [(0,1), (0,2), (0,3)]):
            if repeat(y, x, [(1,0), (1,2), (1,3)]):
                if repeat(y, x, [(2,0), (2,1), (2,3)]):
                    if repeat(y, x, [(3,0), (3,1), (3,2)]):
                        return True

    elif ship=="Frigate" or ship=="Submarine":

        if repeat(y, x, [(1,0), (1,2)]):
            if repeat(y, x, [(2,0), (2,1)]): 
                return True
            
    elif ship=="Patrol":
        if repeat(y, x, [(1,0)]):
            return True
        
#Distance
def dist(y, x , i, i2):
    if (((y[i]-y[i2])**2)+((x[i]-x[i2])**2))**0.5 == 1:
        return True

#repeat
#if this doesnt work find old copy in github desktop
def repeat(xlist, ylist, op_list): 
    global badlist
    num=0
    li=[]
    
    for ele in op_list:
        x,y= ele
        if dist(xlist, ylist, x, y) is True:
            num=num+1
            li.append(ele)

    if num>1:
        return True

    if num==1:
        if li[0] not in badlist:
            x,y=li[0]
            li= (y,x)
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
def drawer1(win, music, sound):

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

    sound_box.draw(win)
    music_box.draw(win)
    
    for box in BoxesP1A:
        box.draw(win)
    for box in BoxesP1B:
        box.draw(win)
    for box in BoxesP1C:
        box.draw(win)
    for box in BoxesP1D:
        box.draw(win)
    for box in BoxesP1E:
        box.draw(win)
    for box in BoxesP1F:
        box.draw(win)
    for box in BoxesP1G:
        box.draw(win)
    for box in BoxesP1H:
        box.draw(win)
    for box in BoxesP1I:
        box.draw(win)
    for box in BoxesP1J:
        box.draw(win)
        
    for box in BoxesP1ATT_A:
        box.draw(win)
    for box in BoxesP1ATT_B:
        box.draw(win)
    for box in BoxesP1ATT_C:
        box.draw(win)
    for box in BoxesP1ATT_D:
        box.draw(win)
    for box in BoxesP1ATT_E:
        box.draw(win)
    for box in BoxesP1ATT_F:
        box.draw(win)
    for box in BoxesP1ATT_G:
        box.draw(win)
    for box in BoxesP1ATT_H:
        box.draw(win)
    for box in BoxesP1ATT_I:
        box.draw(win)
    for box in BoxesP1ATT_J:
        box.draw(win)

    for string in text:
        string.setSize(15)
    for string in nums:
        string.setSize(15)

    for string in text:
        string.draw(win)
    for string in nums:
        string.draw(win)

    for box in P1BoxConf:
        if box in P2att:
            box.setFill("brown2")

    if music:
        music_on.draw(win)
    else:
        music_off.draw(win)

    if sound:
        sound_on.draw(win)
    else:
        sound_off.draw(win)

#Drawer2
def drawer2(win, music, sound):

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

    sound_box.draw(win)
    music_box.draw(win)

    for box in BoxesP2A:
        box.draw(win)
    for box in BoxesP2B:
        box.draw(win)
    for box in BoxesP2C:
        box.draw(win)
    for box in BoxesP2D:
        box.draw(win)
    for box in BoxesP2E:
        box.draw(win)
    for box in BoxesP2F:
        box.draw(win)
    for box in BoxesP2G:
        box.draw(win)
    for box in BoxesP2H:
        box.draw(win)
    for box in BoxesP2I:
        box.draw(win)
    for box in BoxesP2J:
        box.draw(win)

    for box in BoxesP2ATT_A:
        box.draw(win)
    for box in BoxesP2ATT_B:
        box.draw(win)
    for box in BoxesP2ATT_C:
        box.draw(win)
    for box in BoxesP2ATT_D:
        box.draw(win)
    for box in BoxesP2ATT_E:
        box.draw(win)
    for box in BoxesP2ATT_F:
        box.draw(win)
    for box in BoxesP2ATT_G:
        box.draw(win)
    for box in BoxesP2ATT_H:
        box.draw(win)
    for box in BoxesP2ATT_I:
        box.draw(win)
    for box in BoxesP2ATT_J:
        box.draw(win)

    for box in text:
        box.setSize(15)
    for box in nums:
        box.setSize(15)

    for string in text:
        string.draw(win)
    for string in nums:
        string.draw(win)

    for box in P2BoxConf:
        if box in P1att:
            box.setFill("brown2")

    if music:
        music_on.draw(win)
    else:
        music_off.draw(win)

    if sound:
        sound_on.draw(win)
    else:
        sound_off.draw(win)
        


        


