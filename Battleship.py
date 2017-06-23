import pickle
import time
import sys
from definitions import *
from starter import *
from var import *
from zellegraphics import *

#Instructions
'''player1_name, player2_name=Instructions()'''

#########################################################################
#Confirmer
def Confirmer(conflist, stringli, boxloc, boxconf,confirmbox, win, ship):
    if single_detector_conf(1100, 1260, 520, 450, confirmbox, win, ship,
                            conflist) is True:
        for string in stringli:
            if string not in conflist:
                conflist.append(string)
        for box in boxloc:
            if box not in boxconf:
                boxconf.append(box)
        for box in boxconf:
            box.setFill("snow4")
        return True

#Looper
def Looper(length, win, location, confirmlist, boxloc, boxconf, confirmbox,
           ship, *args):
    
    global x_click, y_click, confirmP1
    while True:
        x_click, y_click=click_getter(win)
        try:
            error_text.undraw()
            error_text2.undraw()
            for text in args:
                text.draw(win)
        except:
            GraphicsError
            
        if len(location) is length:
            
            if Confirmer(confirmlist, location, boxloc, boxconf, confirmbox,
                         win, ship):
                break
            
            else:
                if 1100<x_click< 1260 and 450<y_click<520:
                    try:
                       for text in args:
                           text.undraw()
                       error_text.draw(win)
                       error_text2.draw(win)
                    except:
                        GraphicsError
                        
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
            try:
                error_text.draw(win)
                error_text2.draw(win)
                
                for text in args:
                    text.undraw()
            except:
                GraphicsError
            
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
               confirmP1, "Aircraft", instruct_text1, instruct_text2)
        for point in P1BoxConf:
            Aircraft1.append(point)

        instruct_text1.undraw()
        instruct_text2.undraw()

        instruct_text3.draw(winP1)
        instruct_text4.draw(winP1)

        Looper(9, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Battleship", instruct_text3, instruct_text4)
        for point in range(5, 9):
            Bship1.append(P1BoxConf[point])

        instruct_text3.undraw()
        instruct_text4.undraw()

        instruct_text5.draw(winP1)
        instruct_text7.draw(winP1)

        Looper(12, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Frigate", instruct_text5, instruct_text7)
        for point in range(9, 12):
            Frig1.append(P1BoxConf[point])

        instruct_text5.undraw()

        instruct_text6.draw(winP1)

        Looper(15, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Submarine", instruct_text6, instruct_text7)
        for point in range(12, 15):
            Sub1.append(P1BoxConf[point])

        instruct_text6.undraw()
        instruct_text7.undraw()

        instruct_text8.draw(winP1)
        instruct_text9.draw(winP1)
        instruct_text10.draw(winP1)

        Looper(17, winP1, Player1_Locations, P1confirmlist, P1BoxLoc, P1BoxConf,
               confirmP1, "Patrol", instruct_text8, instruct_text9,
               instruct_text10)
        for point in range(15, 17):
            Pat1.append(P1BoxConf[point])

        instruct_text8.undraw()
        instruct_text9.undraw()
        instruct_text10.undraw()

        time.sleep(0.25)
        
        confirm_title.undraw()
        confirm_title= Text(Point(1180, 485), "Done!")
        confirm_title.draw(winP1)

        done_text.draw(winP1)
        done_text2.draw(winP1)
        done_text3.draw(winP1)

        while True:
            click_getter(winP1)
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                winP1.close()
                break
            
    elif "2"== stage:
        confirm_title= Text(Point(1180, 485), "Next Turn")
        confirmP1.undraw()
        
        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1)
        checker(Pat2,"Patrol Boat", P1att, 0, 2, patbox, winP1)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1)
        
        while True:
            length= len(P1att)
            click_getter(winP1)
            attack1()
            length2= len(P1att)
            if length2==length+1:
                break

        confirmP1.draw(winP1)
        confirm_title.draw(winP1)
        
        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1)
        checker(Pat2, "Patrol Boat", P1att, 0, 2, patbox, winP1)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1)
                
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
               confirmP2, "Aircraft", instruct_text1, instruct_text2)
        for point in P2BoxConf:
            Aircraft2.append(point)

        instruct_text1.undraw()
        instruct_text2.undraw()

        instruct_text3.draw(winP2)
        instruct_text4.draw(winP2)
        
        Looper(9, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Battleship", instruct_text3, instruct_text4)
        for point in range(5, 9):
            Bship2.append(P2BoxConf[point])

        instruct_text3.undraw()
        instruct_text4.undraw()

        instruct_text5.draw(winP2)
        instruct_text7.draw(winP2)

        Looper(12, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Frigate", instruct_text5, instruct_text7)
        for point in range(9, 12):
            Frig2.append(P2BoxConf[point])

        instruct_text5.undraw()

        instruct_text6.draw(winP2)

        Looper(15, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Submarine", instruct_text6, instruct_text7)
        for point in range(12, 15):
            Sub2.append(P2BoxConf[point])

        instruct_text6.undraw()
        instruct_text7.undraw()

        instruct_text8.draw(winP2)
        instruct_text9.draw(winP2)
        instruct_text10.draw(winP2)

        Looper(17, winP2, Player2_Locations, P2confirmlist, P2BoxLoc, P2BoxConf,
               confirmP2, "Patrol", instruct_text8, instruct_text9,
               instruct_text10)
        for point in range(15, 17):
            Pat2.append(P2BoxConf[point])

        instruct_text8.undraw()
        instruct_text9.undraw()
        instruct_text10.undraw()

        time.sleep(0.25)
        
        confirm_title.undraw()
        confirm_title= Text(Point(1180, 485), "Done!")
        confirm_title.draw(winP2)

        done_text.draw(winP2)
        done_text2.draw(winP2)
        done_text4.draw(winP2)
        
        while True:
            click_getter(winP2)
            if single_detector(1100, 1260, 520, 450, confirmP2, winP2) is True:
                winP2.close()
                break
            
    elif "2"== stage:
        confirm_title= Text(Point(1180, 485), "Next Turn")
        confirmP2.undraw()
        
        checker(Aircraft1,"Aircraft Carrier", P2att, 0, 5, airbox, winP2)
        checker(Bship1,"Battleship", P2att, 0, 4, bshipbox, winP2)
        checker(Pat1, "Patrol Boat", P2att, 0, 2, patbox, winP2)
        checker(Sub1, "Submarine" ,P2att, 0, 3, subbox, winP2)
        checker(Frig1,"Frigate", P2att, 0, 3, frigbox, winP2)
        
        while True:
            length= len(P2att)
            click_getter(winP2)
            attack2()
            length2= len(P2att)
            if length2==length+1:
                break

        confirmP2.draw(winP2)
        confirm_title.draw(winP2)

        checker(Aircraft1, "Aircraft", P2att, 0, 5, airbox, winP2)       
        checker(Bship1,"Battleship", P2att, 0, 4, bshipbox, winP2)
        checker(Pat1, "Patrol", P2att, 0, 2, patbox, winP2)
        checker(Sub1, "Sub", P2att, 0, 3, subbox, winP2)
        checker(Frig1, "Frigate", P2att, 0, 3, frigbox, winP2)

        while True:
            click_getter(winP2)
            if single_detector(1100, 1260, 520, 450, confirmP2, winP2) is True:
                break

    winP2.close()

#################################################################################

'''os.startfile('/Users/karanarora/Desktop')'''

Player1('1')
Player2('1')
while True:
    Player1('2')
    Player2('2')

writer= open("Pickler.py", "wb")
pickle.dump("", writer, protocol=2)
writer.close()






