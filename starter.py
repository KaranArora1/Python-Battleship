from zellegraphics import *
from definitions import *
import pickle

#Starter
def Instructions(stage, *args):
    #Globals
    global win
    global choice_yes
    global choice_no
    global choice_ok
    global choice_next
    global choice_start

    #Rectangles
    win=GraphWin("%s" %args[0],600, 325, autoflush=False)
    
    case= Rectangle(Point(25, 25), Point(575, 300))
    case.setFill("AntiqueWhite1")
    
    if stage=="1":
        choice_yes= Rectangle(Point(130, 225), Point(215, 260))
        choice_no= Rectangle(Point(385, 225), Point(470, 260))
        choice_ok= Rectangle(Point(355, 180), Point(430, 220))
        instruction_line= Rectangle(Point(225, 70), Point(375, 70))
        choice_start= Rectangle(Point(262.5, 225),Point(337.5, 260))
        choice_next= Rectangle(Point(262.5, 225), Point(337.5, 260))
        
        #Text
        instruction6= Text(Point(300, 150), "Lets start!")

        instruction5_4= Text(Point(300, 190),"- The Patrol Boat has 2 points.")
        instruction5_3= Text(Point(300, 160), "- The Frigate and the Submarine both have 3 points")
        instruction5_2= Text(Point(300, 130), "- A Battleship has 4 points")
        instruction5= Text(Point(300, 100), "- An Aircraft Carrier has 5 points")  

        instruction4_2= Text(Point(300, 180), "click in your desired box.")
        instruction4=Text(Point(300, 130), "To place a ship or fire a shot, just")

        instruction3_3=Text(Point(300, 190), "still standing, you win!")
        instruction3_2=Text(Point(300, 150), "least one of your own ships are")
        instruction3=Text(Point(300, 110), "If you accomplish this, and at")

        instruction2_2= Text(Point(300, 170), "all of your opponents ships.")
        instruction2=Text(Point(300, 120), "The goal of Battleship is to sink")

        instruction1=Text(Point(300, 150),"Here are the instructions for Battleship.")

        title4= Text(Point(300, 150), "Would you like to read the instructions?")
        title3=Text(Point(300, 150), "What is Player 2's name?")
        title2= Text(Point(300, 150), "What is Player 1's name?")
        title= Text(Point(300, 150), "Do you want to play Battleship?")

        text_yes= Text(Point(172.5, 242.5), "Yes")
        text_no= Text(Point(427.5, 242.5), "No")
        text_ok= Text(Point(392.5, 200), "OK")
        text_next= Text(Point(300, 242.5), "Next")

        text_instruction= Text(Point(300, 55), "Instructions")

        text_start= Text(Point(300, 242.5), "Start!")

        #Entry
        nameentry_1=Entry(Point(250,200),30)
        nameentry_2=Entry(Point(250, 200),30)

        #Sizes
        title.setSize(26)
        title2.setSize(26)
        title3.setSize(26)
        title4.setSize(24)

        instruction1.setSize(26)

        instruction2.setSize(26)
        instruction2_2.setSize(26)

        instruction3.setSize(26)
        instruction3_2.setSize(26)
        instruction3_3.setSize(26)

        instruction4_2.setSize(26)
        instruction4.setSize(26)

        instruction5.setSize(20)
        instruction5_2.setSize(20)
        instruction5_3.setSize(20)
        instruction5_4.setSize(20)

        instruction6.setSize(26)

        text_instruction.setSize(28)

        #Drawing
        case.draw(win)
        choice_no.draw(win)
        choice_yes.draw(win)
        title.draw(win)
        text_yes.draw(win)
        text_no.draw(win)

        choice_yes.setFill("AntiqueWhite2")
        choice_no.setFill("AntiqueWhite2")
        choice_ok.setFill("AntiqueWhite2")
        choice_start.setFill("AntiqueWhite2")
        choice_next.setFill("AntiqueWhite2")

        #Yes/No
        if yes_no_detector(130, 215, 260, 225, 385, 470, 260, 225,
                           win, choice_yes, choice_no) is False:
            time.sleep(0.5)
            win.close()
            sys.exit()

        title.undraw()
        choice_yes.undraw()
        choice_no.undraw()
        text_yes.undraw()
        text_no.undraw()

        #Naming
        nameentry_1.draw(win)
        choice_ok.draw(win)

        title2.draw(win)
        text_ok.draw(win)

        next_detector(355, 430, 220, 180, choice_ok, win)
        player1_name=nameentry_1.getText()
        if player1_name==(""):
            player1_name=("Player1")
        
        title2.undraw()
        nameentry_1.undraw()

        nameentry_2.draw(win)
        title3.draw(win)    

        next_detector(355, 430, 220, 180, choice_ok, win)
        player2_name=nameentry_2.getText()
        if player2_name==(""):
            player2_name=("Player2")

        nameentry_2.undraw()
        text_ok.undraw()
        choice_ok.undraw()
        title3.undraw()
        
        choice_yes.draw(win)
        choice_no.draw(win)
        title4.draw(win)
        text_yes.draw(win)
        text_no.draw(win)

        doer="yes"

        #Instructions
        if yes_no_detector(130, 215, 260, 225, 385, 470, 260, 225,
                           win, choice_yes, choice_no) is True:

            doer!="yes"

            title4.undraw()
            choice_yes.undraw()
            choice_no.undraw()
            text_yes.undraw()
            text_no.undraw()
            
            text_instruction.draw(win)
            instruction_line.draw(win)
            choice_next.draw(win)
            text_next.draw(win)

            instruction1.draw(win)

            next_detector(262.5, 337.5, 260, 225, choice_next, win)

            instruction1.undraw()

            instruction2.draw(win)
            instruction2_2.draw(win)

            next_detector(262.5, 337.5, 260, 225, choice_next, win)

            instruction2.undraw()
            instruction2_2.undraw()

            instruction3.draw(win)
            instruction3_2.draw(win)
            instruction3_3.draw(win)

            next_detector(262.5, 337.5, 260, 225, choice_next, win)

            instruction3.undraw()
            instruction3_2.undraw()
            instruction3_3.undraw()

            instruction4.draw(win)
            instruction4_2.draw(win)

            next_detector(262.5, 337.5, 260, 225, choice_next, win)

            instruction4.undraw()
            instruction4_2.undraw()

            instruction5.draw(win)
            instruction5_2.draw(win)
            instruction5_3.draw(win)
            instruction5_4.draw(win)

            next_detector(262.5, 337.5, 260, 225, choice_next, win) 

            instruction5.undraw()
            instruction5_2.undraw()
            instruction5_3.undraw()
            instruction5_4.undraw()

        if doer=="yes":
            title4.undraw()
            choice_yes.undraw()
            choice_no.undraw()
            text_yes.undraw()
            text_no.undraw()
            
        instruction_line.undraw()
        text_instruction.undraw()
        text_next.undraw()

        choice_next.undraw()
        
        instruction6.draw(win)
        choice_start.draw(win)
        text_start.draw(win)

        next_detector(262.5, 337.5, 260, 225, choice_start, win)
        time.sleep(1)
        win.close()
        return player1_name, player2_name

    elif stage=="2":

        choice_next_turn=Rectangle(Point(247.5, 217.5), Point(352.5, 267.5))
        
        message=Text(Point(300, 150),
                     "Waiting for the device to be passed to %s..." %args[1])
        
        text_next_2= Text(Point(300, 242.5), "Next Turn")
        
        message.setSize(18)

        choice_next_turn.setFill("AntiqueWhite2")        

        case.draw(win)
        message.draw(win)
        choice_next_turn.draw(win)
        text_next_2.draw(win)

        next_detector(247.5, 352.5, 267.5, 217.5, choice_next_turn, win)
        time.sleep(0.1)

        win.close()

        

if __name__== "__main__":
    Instructions("1", "Start")





