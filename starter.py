from zellegraphics import *
from definitions import *
from var import *
import pygame

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
    
    if stage=="1":

        #Drawing
        case.draw(win)
        choice_no.draw(win)
        choice_yes.draw(win)
        title.draw(win)
        text_yes.draw(win)
        text_no.draw(win)

        #Yes/No
        if yes_no_detector(130, 215, 260, 225, 385, 470, 260, 225,
                           win, choice_yes, choice_no) is False:
            time.sleep(0.5)
            win.close()
            sys.exit()

        title.undraw()

        #Sound
        title5.draw(win)
        title6.draw(win)
        
        if yes_no_detector(130, 215, 260, 225, 385, 470, 260, 225,
                           win, choice_yes, choice_no):
            music=True
            sound=True

            pygame.init()
            pygame.mixer.music.load("waves.mp3")
            pygame.mixer.music.play(-1)
        
        else:
            sound=False
            music=False
            
        title5.undraw()
        title6.undraw()
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
        return player1_name, player2_name, music, sound

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





