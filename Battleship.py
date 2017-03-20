import subprocess
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
    global winP1, click, confirmP1, Player1_Locations 
    global Aircraft1, Pat1, Sub1, Frig1, Bship1
    global P1x, P1y

    winP1=GraphWin("Battleship Board", 1275, 650, autoflush= False)
    
    fleet= Rectangle(Point(35, 60), Point(530, 590))
    attack= Rectangle(Point(590, 60), Point(1085, 590))

    text_box= Rectangle(Point(1100, 80), Point(1260, 380))
    button1= Rectangle(Point(1100, 400), Point(1260, 450))
    button2= Rectangle(Point(1100, 470), Point(1260, 520))
    confirmP1= Rectangle(Point(1100, 450), Point(1260, 520))

    winP1.setBackground("cyan3")
    fleet.setFill("cyan4")
    attack.setFill("cyan4")

    text_box.setFill("AntiqueWhite")
    button1.setFill("AntiqueWhite")
    button2.setFill("AntiqueWhite")
    confirmP1.setFill("AntiqueWhite2")
    
    attack.draw(winP1)
    fleet.draw(winP1)

    text_box.draw(winP1)

    fleet_title= Text(Point(277.5, 25), "FLEET")
    radar_title= Text(Point(882.5, 25), "RADAR")
    confirm_title= Text(Point(1180, 485), "Confirm")

    fleet_title.setSize(20)

    text_box_title=Text(Point(1170, 95), "Dialogue")
    button1_text=Text(Point(1170, 425), "BUTTON1")
    button2_text=Text(Point(1170, 495), "BUTTON2")

    fleet_title.draw(winP1)
    radar_title.draw(winP1)
    text_box_title.draw(winP1)

    drawer1(winP1)

    winP1.update()

    if "1"== stage:
        confirmP1.draw(winP1)
        confirm_title.draw(winP1)
    
        Looper(5, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Aircraft")
        for i in P1confirmlist:
            Aircraft1.append(i)

        Looper(9, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Battleship")
        for i in range(5, 9):
            Bship1.append(P1confirmlist[i])

        Looper(12, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Frigate")
        for i in range(9, 12):
            Frig1.append(P1confirmlist[i])

        Looper(15, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Submarine")
        for i in range(12, 15):
            Sub1.append(P1confirmlist[i])

        Looper(17, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Patrol")
        for i in range(15, 17):
            Pat1.append(P1confirmlist[i])

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
        while True:
            length= len(P1att)
            click_getter(winP1)
            attack1()
            length2= len(P1att)
            if length2==length+1:
                break

        while True:
            click_getter(winP1)
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                winP1.close()
                break

    winP1.close()
                        
#####################
def Player2(stage):
    global winP2, click, confirmP2, Player2_Locations 
    global Aircraft2, Pat2, Sub2, Frig2, Bship2

    winP2=GraphWin("Battleship Board", 1275, 650, autoflush=False)
    
    fleet= Rectangle(Point(35, 60), Point(530, 590))
    attack= Rectangle(Point(590, 60), Point(1085, 590))

    text_box= Rectangle(Point(1100, 80), Point(1260, 380))
    button1= Rectangle(Point(1100, 400), Point(1260, 450))
    button2= Rectangle(Point(1100, 470), Point(1260, 520))
    confirmP2= Rectangle(Point(1100, 450), Point(1260, 520))

    winP2.setBackground("cyan3")
    fleet.setFill("cyan4")
    attack.setFill("cyan4")

    text_box.setFill("AntiqueWhite")
    button1.setFill("AntiqueWhite")
    button2.setFill("AntiqueWhite")
    confirmP2.setFill("AntiqueWhite")

    attack.draw(winP2)
    fleet.draw(winP2)

    text_box.draw(winP2)

    fleet_title= Text(Point(277.5, 25), "FLEET")
    radar_title= Text(Point(882.5, 25), "RADAR")
    confirm_title= Text(Point(1180, 485), "Confirm")

    fleet_title.setSize(20)

    text_box_title=Text(Point(1170, 95), "Dialogue")
    button1_text=Text(Point(1170, 425), "BUTTON1")
    button2_text=Text(Point(1170, 495), "BUTTON2")

    fleet_title.draw(winP2)
    radar_title.draw(winP2)

    text_box_title.draw(winP2)

    drawer2(winP2)

    if "1"== stage:
        confirmP2.draw(winP2)
        confirm_title.draw(winP2)
    
        Looper(5, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Aircraft")
        for i in P2confirmlist:
            Aircraft2.append(i)
        
        Looper(9, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Battleship")
        for i in range(5, 9):
            Bship2.append(P2confirmlist[i])

        Looper(12, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Frigate")
        for i in range(9, 12):
            Frig2.append(P2confirmlist[i])

        Looper(15, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Submarine")
        for i in range(12, 15):
            Sub2.append(P2confirmlist[i])

        Looper(17, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Patrol")
        for i in range(15, 17):
            Pat2.append(P2confirmlist[i])

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
        
        while True:
            length= len(P2att)
            click_getter(winP2)
            attack2()
            length2= len(P2att)
            if length2==length+1:
                break

        while True:
            click_getter(winP2)
            if single_detector(1100, 1260, 520, 450, confirmP2, winP2) is True:
                winP2.close()
                break
            
    winP2.close()
                    

'''audio_file="/Users/karanarora/Desktop/Music/New/Sandmang.wav"
subprocess.call(["afplay", audio_file])
Player2()'''

Player1('1')
Player2('1')
while True:
    Player1('2')
    Player2('2')

writer= open("Pickler.py", "wb")
pickle.dump("", writer, protocol=2)
writer.close()






