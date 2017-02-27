import pickle
import time
import sys
from zellegraphics import *
from definitions import *
from var import *
from starter import *

#Instructions
player1_name, player2_name=Instructions()

print(player2_name)

#########################################################################
#Confirmer
def Confirmer(location1, location2):
    if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
        for x in location2:
            if x not in location1:
                location1.append(x)
        return True

#Looper
def Looper(length, win, location):
    global click
    while True:
        click_getter(winP1)
        if len(location) is length:
            if Confirmer(P1confirmlist, Player1_Locations) is True:
                break
        try:
            if win is winP1:
                ListofListAppenders1()
                FinalFiller1()
        except:
            NameError
        try:
            if win is winP2:
                ListofListAppenders2()
                FinalFiller2()
        except:
            NameError

####################### PLAYER1 BOARD ######################################
#Player 1's Board
def Player1():
    global winP1
    global click
    global confirmP1

    winP1=GraphWin("Battleship Board", 1275, 650)
    
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
    confirmP1.setFill("AntiqueWhite")
    
    attack.draw(winP1)
    fleet.draw(winP1)

    text_box.draw(winP1)
    confirmP1.draw(winP1)

    fleet_title= Text(Point(277.5, 25), "FLEET")
    radar_title= Text(Point(882.5, 25), "RADAR")
    confirm_title= Text(Point(1180, 485), "Confirm")

    fleet_title.setSize(20)

    text_box_title=Text(Point(1170, 95), "Dialogue")
    button1_text=Text(Point(1170, 425), "BUTTON1")
    button2_text=Text(Point(1170, 495), "BUTTON2")

    fleet_title.draw(winP1)
    radar_title.draw(winP1)
    confirm_title.draw(winP1)
    text_box_title.draw(winP1)

    drawer1(winP1)

    FinalFiller1()
    Looper(3, winP1, Player1_Locations)

    FinalFiller1()

    Looper(5, winP1, Player1_Locations)

    FinalFiller1()

    Looper(6, winP1, Player1_Locations)

    print("im here")

#####################
def Player2():
    global winP2
    global click

    global A1_2, B1_2, C1_2, D1_2, E1_2, F1_2, G1_2, H1_2, I1_2, J1_2
    global A2_2, B2_2, C2_2, D2_2, E2_2, F2_2, G2_2, H2_2, I2_2, J2_2
    global A3_2, B3_2, C3_2, D3_2, E3_3, F3_2, G3_2, H3_2, I3_2, J3_2
    global A4_2, B4_2, C4_2, D4_2, E4_4, F4_2, G4_2, H4_2, I4_2, J4_2
    global A5_2, B5_2, C5_2, D5_2, E5_5, F5_2, G5_2, H5_2, I5_2, J5_2
    global A6_2, B6_2, C6_2, D6_2, E6_6, F6_2, G6_2, H6_2, I6_2, J6_2
    global A7_2, B7_2, C7_2, D7_2, E7_7, F7_2, G7_2, H7_2, I7_2, J7_2
    global A8_2, B8_2, C8_2, D8_2, E8_8, F8_2, G8_2, H8_2, I8_2, J8_2
    global A9_2, B9_2, C9_2, D9_2, E9_9, F9_2, G9_2, H9_2, I9_2, J9_2
    global A10_2, B10_2, C10_2, D10_2, E10_20, F10_2, G10_2, H10_2, I10_2, J10_2

    winP2=GraphWin("Battleship Board", 1275, 650)
    
    fleet= Rectangle(Point(35, 60), Point(530, 590))
    attack= Rectangle(Point(590, 60), Point(1085, 590))

    text_box= Rectangle(Point(1100, 80), Point(1260, 380))
    button1= Rectangle(Point(1100, 400), Point(1260, 450))
    button2= Rectangle(Point(1100, 470), Point(1260, 520))

    winP2.setBackground("cyan3")
    fleet.setFill("cyan4")
    attack.setFill("cyan4")

    text_box.setFill("AntiqueWhite")
    button1.setFill("AntiqueWhite")
    button2.setFill("AntiqueWhite")
    

    attack.draw(winP2)
    fleet.draw(winP2)

    text_box.draw(winP2)
    button1.draw(winP2)
    button2.draw(winP2)

    fleet_title= Text(Point(277.5, 25), "FLEET")
    radar_title= Text(Point(882.5, 25), "RADAR")

    fleet_title.setSize(20)

    text_box_title=Text(Point(1170, 95), "Dialogue")
    button1_text=Text(Point(1170, 425), "BUTTON1")
    button2_text=Text(Point(1170, 495), "BUTTON2")

    fleet_title.draw(winP2)
    radar_title.draw(winP2)

    text_box_title.draw(winP2)
    button1_text.draw(winP2)
    button2_text.draw(winP2)

    A1_2=Rectangle(Point(35, 60), Point(84.5, 113))
    A2_2=Rectangle(Point(84.5, 60 ), Point(134, 113))
    A3_2=Rectangle(Point(134, 60), Point(183.5, 113))
    A4_2=Rectangle(Point(183.5, 60), Point(233, 113))
    A5_2=Rectangle(Point(233, 60), Point(282.5, 113))
    A6_2=Rectangle(Point(282.5, 60), Point(332, 113))
    A7_2=Rectangle(Point(332, 60), Point(381.5, 113))
    A8_2=Rectangle(Point(381.5, 60), Point(431, 113))
    A9_2=Rectangle(Point(431, 60), Point(480.5, 113))
    A10_2=Rectangle(Point(480.5, 60), Point(530, 113))

    A1_2.draw(winP2)
    A2_2.draw(winP2)
    A3_2.draw(winP2)
    A4_2.draw(winP2)
    A5_2.draw(winP2)
    A6_2.draw(winP2)
    A7_2.draw(winP2)
    A8_2.draw(winP2)
    A9_2.draw(winP2)
    A10_2.draw(winP2)

    Looper(3, winP2)
 
Player1()
winP1.close()

writer= open("Pickler.py", "wb")
pickle.dump("", writer, protocol=2)
writer.close()






