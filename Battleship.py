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

    airbox.draw(winP1)
    bshipbox.draw(winP1)
    frigbox.draw(winP1)
    subbox.draw(winP1)
    patbox.draw(winP1)
    
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

        instruct_text1.draw(winP1)
        instruct_text2.draw(winP1)
        
        Looper(5, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Aircraft")
        for i in P1BoxConf:
            Aircraft1.append(i)

        instruct_text1.undraw()
        instruct_text2.undraw()

        instruct_text3.draw(winP1)
        instruct_text4.draw(winP1)

        Looper(9, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Battleship")
        for i in range(5, 9):
            Bship1.append(P1BoxConf[i])

        instruct_text3.undraw()
        instruct_text4.undraw()

        instruct_text5.draw(winP1)
        instruct_text7.draw(winP1)

        Looper(12, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Frigate")
        for i in range(9, 12):
            Frig1.append(P1BoxConf[i])

        instruct_text5.undraw()

        instruct_text6.draw(winP1)

        Looper(15, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Submarine")
        for i in range(12, 15):
            Sub1.append(P1BoxConf[i])

        instruct_text6.undraw()
        instruct_text7.undraw()

        instruct_text8.draw(winP1)
        instruct_text9.draw(winP1)
        instruct_text10.draw(winP1)

        Looper(17, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Patrol")
        for i in range(15, 17):
            Pat1.append(P1BoxConf[i])

        instruct_text8.undraw()
        instruct_text9.undraw()
        instruct_text10.undraw()

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
        confirmP1.undraw()
        
        num=0
        checker(Aircraft2, P1att, num, 5, airbox, winP1)
        checker(Bship2, P1att, num, 4, bshipbox, winP1)
        checker(Pat2, P1att, num, 2, patbox, winP1)
        checker(Sub2, P1att, num, 3, subbox, winP1)
        checker(Frig2, P1att, num, 3, frigbox, winP1)
        
        while True:
            length= len(P1att)
            click_getter(winP1)
            attack1()
            length2= len(P1att)
            if length2==length+1:
                break

        confirmP1.draw(winP1)
        confirm_title.draw(winP1)
        
        num=0
        checker(Aircraft2, P1att, num, 5, airbox, winP1)
        checker(Bship2, P1att, num, 4, bshipbox, winP1)
        checker(Pat2, P1att, num, 2, patbox, winP1)
        checker(Sub2, P1att, num, 3, subbox, winP1)
        checker(Frig2, P1att, num, 3, frigbox, winP1)

        for i in P1att:
            if i in P2BoxConf:
                num=num+1
                
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

    airbox.draw(winP2)
    bshipbox.draw(winP2)
    frigbox.draw(winP2)
    subbox.draw(winP2)
    patbox.draw(winP2)

    drawer2(winP2)
    confirmP2.draw(winP2)

    if "1"== stage:
        airbox.setFill("SpringGreen2")
        bshipbox.setFill("SpringGreen2")
        subbox.setFill("SpringGreen2")
        frigbox.setFill("SpringGreen2")
        patbox.setFill("SpringGreen2")
        
        confirm_title.draw(winP2)

        instruct_text1.draw(winP2)
        instruct_text2.draw(winP2)

        Looper(5, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Aircraft")
        for i in P2BoxConf:
            Aircraft2.append(i)

        instruct_text1.undraw()
        instruct_text2.undraw()

        instruct_text3.draw(winP2)
        instruct_text4.draw(winP2)
        
        Looper(9, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Battleship")
        for i in range(5, 9):
            Bship2.append(P2BoxConf[i])

        instruct_text3.undraw()
        instruct_text4.undraw()

        instruct_text5.draw(winP2)
        instruct_text7.draw(winP2)

        Looper(12, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Frigate")
        for i in range(9, 12):
            Frig2.append(P2BoxConf[i])

        instruct_text5.undraw()

        instruct_text6.draw(winP2)

        Looper(15, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Submarine")
        for i in range(12, 15):
            Sub2.append(P2BoxConf[i])

        instruct_text6.undraw()
        instruct_text7.undraw()

        instruct_text8.draw(winP2)
        instruct_text9.draw(winP2)
        instruct_text10.draw(winP2)

        Looper(17, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Patrol")
        for i in range(15, 17):
            Pat2.append(P2BoxConf[i])

        instruct_text8.undraw()
        instruct_text9.undraw()
        instruct_text10.undraw()

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
        confirmP2.undraw()
        
        num=0
        checker(Aircraft1, P2att, num, 5, airbox, winP2)
        checker(Bship1, P2att, num, 4, bshipbox, winP2)
        checker(Pat1, P2att, num, 2, patbox, winP2)
        checker(Sub1, P2att, num, 3, subbox, winP2)
        checker(Frig1, P2att, num, 3, frigbox, winP2)
        
        while True:
            length= len(P2att)
            click_getter(winP2)
            attack2()
            length2= len(P2att)
            if length2==length+1:
                break

        confirmP2.draw(winP2)
        confirm_title.draw(winP2)

        checker(Aircraft1, P2att, num, 5, airbox, winP2)
        checker(Bship1, P2att, num, 4, bshipbox, winP2)
        checker(Pat1, P2att, num, 2, patbox, winP2)
        checker(Sub1, P2att, num, 3, subbox, winP2)
        checker(Frig1, P2att, num, 3, frigbox, winP2)

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






