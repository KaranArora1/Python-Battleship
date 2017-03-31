import os
import pickle
import time
import sys
from zellegraphics import *
from definitions import *
from var import *
from starter import *

#Instructions
'''player1_name, player2_name=Instructions()'''

#########################################################################
#Confirmer
def Confirmer(conflist, stringli, boxloc, boxconf,confirmbox, win, ship):
    if single_detector_conf(1100, 1260, 520, 450, confirmbox, win, ship, conflist) is True:
        for x in stringli:
            if x not in conflist:
                conflist.append(x)
        for x in boxloc:
            if x not in boxconf:
                boxconf.append(x)
        for i in boxconf:
            i.setFill("snow4")
        return True

#Looper
def Looper(length, win, location, confirmlist, boxloc, boxconf, confirmbox, ship):
    global x_click, y_click, confirmP1
    while True:
        x_click, y_click=click_getter(win)
        if len(location) is length:
            if Confirmer(confirmlist, location, boxloc, boxconf, confirmbox, win, ship) is True:
                break
        try:
            if win is winP1:
                ListofListAppenders1()
        except:
            NameError
        try:
            if win is winP2:
                ListofListAppenders2()
        except:
            NameError

        if 1100<x_click< 1260 and 450<y_click<520 and len(location) != length:
            confirmbox.setFill("brown2")
            win.update()
            time.sleep(0.15)
            confirmbox.setFill("AntiqueWhite2")
            win.update()
            
####################### PLAYER1 BOARD ######################################
#Player 1's Board
def Player1(stage):
    global winP1, click, confirmP1, Player1_Locations, confirm_title
    global Aircraft1, Pat1, Sub1, Frig1, Bship1
    
    winP1=GraphWin("Player One's Battleship Board", 1275, 650, autoflush= False)
    
    button1= Rectangle(Point(1100, 400), Point(1260, 450))
    button2= Rectangle(Point(1100, 470), Point(1260, 520))
    confirmP1= Rectangle(Point(1100, 450), Point(1260, 520))

    winP1.setBackground("cyan3")

    text_box.setFill("AntiqueWhite")
    button1.setFill("AntiqueWhite")
    button2.setFill("AntiqueWhite")
    confirmP1.setFill("AntiqueWhite2")
    
    attack.draw(winP1)
    fleet.draw(winP1)
    text_box.draw(winP1)

    airbox=Rectangle(Point(1225, 220), Point(1245, 240))
    bshipbox=Rectangle(Point(1225, 252.5), Point(1245, 272.5))
    frigbox=Rectangle(Point(1225, 285), Point(1245, 305))
    subbox=Rectangle(Point(1225, 317.5), Point(1245, 337.5))
    patbox=Rectangle(Point(1225, 350), Point(1245, 370))

    OPship_line.draw(winP1)
    dialogue_line.draw(winP1)
    turns_line.draw(winP1)
    
    other_player_ships_title.draw(winP1)
    bshiptext.draw(winP1)
    airtext.draw(winP1)
    subtext.draw(winP1)
    pattext.draw(winP1)
    frigtext.draw(winP1)

    airbox.draw(winP1)
    bshipbox.draw(winP1)
    frigbox.draw(winP1)
    subbox.draw(winP1)
    patbox.draw(winP1)
    
    turns_text.draw(winP1)
    fleet_title.draw(winP1)
    radar_title.draw(winP1)
    text_box_title.draw(winP1)
    
    drawer1(winP1)
    confirmP1.draw(winP1)

    winP1.update()

    if "1"== stage:
        airbox.setFill("SpringGreen2")
        bshipbox.setFill("SpringGreen2")
        subbox.setFill("SpringGreen2")
        frigbox.setFill("SpringGreen2")
        patbox.setFill("SpringGreen2")
        
        confirm_title.draw(winP1)
    
        Looper(5, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Aircraft")
        for i in P1BoxConf:
            Aircraft1.append(i)

        Looper(9, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Battleship")
        for i in range(5, 9):
            Bship1.append(P1BoxConf[i])

        '''Looper(12, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Frigate")
        for i in range(9, 12):
            Frig1.append(P1BoxConf[i])

        Looper(15, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Submarine")
        for i in range(12, 15):
            Sub1.append(P1BoxConf[i])

        Looper(17, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Patrol")
        for i in range(15, 17):
            Pat1.append(P1BoxConf[i])'''

        time.sleep(0.25)
        
        confirm_title.undraw()
        confirm_title= Text(Point(1180, 485), "Done!")
        confirm_title.draw(winP1)

        while True:
            click_getter(winP1)
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                winP1.close()
                break
            
    elif "2"== stage:
        confirm_title= Text(Point(1180, 485), "Done")
        confirm_title.draw(winP1)

        num=0
        for i in Aircraft2:
            if i in P1att:
                num=num+1
        if num is 5:
            airbox.setFill("#f44141")
        else:
            airbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Bship2:
            if i in P1att:
                num=num+1
        if num is 4:
            bshipbox.setFill("#f44141")
        else:
            bshipbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Pat2:
            if i in P1att:
                num=num+1
        if num is 2:
            patbox.setFill("#f44141")
        else:
            patbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Sub2:
            if i in P1att:
                num=num+1
        if num is 3:
            subbox.setFill("#f44141")
        else:
            subbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Frig2:
            if i in P1att:
                num=num+1
        if num is 3:
            frigbox.setFill("#f44141")
        else:
            frigbox.setFill("SpringGreen2")
        winP1.update()
        num=0
        
        while True:
            length= len(P1att)
            click_getter(winP1)
            attack1()
            length2= len(P1att)
            if length2==length+1:
                break

        num=0

        for i in Aircraft2:
            if i in P1att:
                num=num+1
        if num is 5:
            airbox.setFill("#f44141")
        else:
            airbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Bship2:
            if i in P1att:
                num=num+1
        if num is 4:
            bshipbox.setFill("#f44141")
        else:
            bshipbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Pat2:
            if i in P1att:
                num=num+1
        if num is 2:
            patbox.setFill("#f44141")
        else:
            patbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Sub2:
            if i in P1att:
                num=num+1
        if num is 3:
            subbox.setFill("#f44141")
        else:
            subbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Frig2:
            if i in P1att:
                num=num+1
        if num is 3:
            frigbox.setFill("#f44141")
        else:
            frigbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        while True:
            click_getter(winP1)
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                winP1.close()
                break

    winP1.close()
                        
#####################
def Player2(stage):
    global winP2, click, confirmP2, Player2_Locations, confirm_title
    global Aircraft2, Pat2, Sub2, Frig2, Bship2

    winP2=GraphWin("Player Two's Battleship Board", 1275, 650, autoflush=False)
    
    button1= Rectangle(Point(1100, 400), Point(1260, 450))
    button2= Rectangle(Point(1100, 470), Point(1260, 520))
    confirmP2= Rectangle(Point(1100, 450), Point(1260, 520))
    confirm_title= Text(Point(1180, 485), "Confirm")

    winP2.setBackground("cyan3")

    text_box.setFill("AntiqueWhite")
    button1.setFill("AntiqueWhite")
    button2.setFill("AntiqueWhite")
    confirmP2.setFill("AntiqueWhite")

    attack.draw(winP2)
    fleet.draw(winP2)
    text_box.draw(winP2)

    airbox=Rectangle(Point(1225, 220), Point(1245, 240))
    bshipbox=Rectangle(Point(1225, 252.5), Point(1245, 272.5))
    frigbox=Rectangle(Point(1225, 285), Point(1245, 305))
    subbox=Rectangle(Point(1225, 317.5), Point(1245, 337.5))
    patbox=Rectangle(Point(1225, 350), Point(1245, 370))
    
    bshiptext.draw(winP2)
    airtext.draw(winP2)
    subtext.draw(winP2)
    pattext.draw(winP2)
    frigtext.draw(winP2)

    airbox.draw(winP2)
    bshipbox.draw(winP2)
    frigbox.draw(winP2)
    subbox.draw(winP2)
    patbox.draw(winP2)

    dialogue_line.draw(winP2)
    OPship_line.draw(winP2)
    turns_line.draw(winP2)

    other_player_ships_title.draw(winP2)
    turns_text.draw(winP2)
    fleet_title.draw(winP2)
    radar_title.draw(winP2)
    text_box_title.draw(winP2)

    drawer2(winP2)
    confirmP2.draw(winP2)

    if "1"== stage:
        airbox.setFill("SpringGreen2")
        bshipbox.setFill("SpringGreen2")
        subbox.setFill("SpringGreen2")
        frigbox.setFill("SpringGreen2")
        patbox.setFill("SpringGreen2")
        confirm_title.draw(winP2)
    
        Looper(5, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Aircraft")
        for i in P2BoxConf:
            Aircraft2.append(i)
        
        Looper(9, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Battleship")
        for i in range(5, 9):
            Bship2.append(P2BoxConf[i])

        '''Looper(12, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Frigate")
        for i in range(9, 12):
            Frig2.append(P2BoxConf[i])

        Looper(15, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Submarine")
        for i in range(12, 15):
            Sub2.append(P2BoxConf[i])

        Looper(17, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Patrol")
        for i in range(15, 17):
            Pat2.append(P2BoxConf[i])'''

        time.sleep(0.25)
        
        confirm_title.undraw()
        confirm_title= Text(Point(1180, 485), "Done!")
        confirm_title.draw(winP2)

        while True:
            click_getter(winP2)
            if single_detector(1100, 1260, 520, 450, confirmP2, winP2) is True:
                winP2.close()
                break
            
    elif "2"== stage:
        confirm_title= Text(Point(1180, 485), "Done")
        confirm_title.draw(winP2)

        num=0
        for i in Aircraft2:
            if i in P1att:
                num=num+1
        if num is 5:
            airbox.setFill("#f44141")
        else:
            airbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Bship2:
            if i in P1att:
                num=num+1
        if num is 4:
            bshipbox.setFill("#f44141")
        else:
            bshipbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Pat2:
            if i in P1att:
                num=num+1
        if num is 2:
            patbox.setFill("#f44141")
        else:
            patbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Sub2:
            if i in P1att:
                num=num+1
        if num is 3:
            subbox.setFill("#f44141")
        else:
            subbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Frig2:
            if i in P1att:
                num=num+1
        if num is 3:
            frigbox.setFill("#f44141")
        else:
            frigbox.setFill("SpringGreen2")
        winP1.update()
        num=0
        
        while True:
            length= len(P2att)
            click_getter(winP2)
            attack2()
            length2= len(P2att)
            if length2==length+1:
                break

        num=0
        for i in Aircraft2:
            if i in P1att:
                num=num+1
        if num is 5:
            airbox.setFill("#f44141")
        else:
            airbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Bship2:
            if i in P1att:
                num=num+1
        if num is 4:
            bshipbox.setFill("#f44141")
        else:
            bshipbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Pat2:
            if i in P1att:
                num=num+1
        if num is 2:
            patbox.setFill("#f44141")
        else:
            patbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Sub2:
            if i in P1att:
                num=num+1
        if num is 3:
            subbox.setFill("#f44141")
        else:
            subbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        for i in Frig2:
            if i in P1att:
                num=num+1
        if num is 3:
            frigbox.setFill("#f44141")
        else:
            frigbox.setFill("SpringGreen2")
        winP1.update()
        num=0

        while True:
            click_getter(winP2)
            if single_detector(1100, 1260, 520, 450, confirmP2, winP2) is True:
                break

    winP2.close()
                    

'''os.startfile('/Users/karanarora/Desktop')'''

Player1('1')
Player2('1')
while True:
    Player1('2')
    Player2('2')

writer= open("Pickler.py", "wb")
pickle.dump("", writer, protocol=2)
writer.close()






