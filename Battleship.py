#!/usr/local/bin/python3

#imports
import pickle
import time
import sys
import pygame
from definitions import *
from starter import *
from var import *
from zellegraphics import *

#Calls starter code
player1_name, player2_name, music, soundvar=Instructions("1", "Start")

'''#Sets variables that are normally set by starter code
player1_name= "Karan"
player2_name= "Rajan"
soundvar=False
music=False'''

#initialization of pygame
pygame.init()

#Plays music if value is true
if music:
    pygame.mixer.music.load("seamusic.mp3")
    pygame.mixer.music.play(-1)

#########################################################################
#Confirmer
def Confirmer(conflist, stringli, boxloc, boxconf,confirmbox, win, ship,
              soundvar):

    #If the ship is placed properly
    if single_detector_conf(1100, 1260, 520, 450, confirmbox, win, ship,
                            conflist, soundvar) is True:

        #Add ship's strings to a confirmlist
        for string in stringli:
            if string not in conflist:
                conflist.append(string)
                
        #Add the ship's actual box objects to a list
        for box in boxloc:
            if box not in boxconf:
                boxconf.append(box)

        #SetFill the confirmed boxes gray
        for box in boxconf:
            box.setFill("snow4")
        return True

#Looper
def Looper(length, win, location, confirmlist, boxloc, boxconf, confirmbox,
           ship, soundvar, music, *args):
    
    global x_click, y_click, confirmP1
    
    while True:
        #Gets click
        x_click, y_click=click_getter(win)
        
        #If click is in attack box and sound is on play error.ogg
        if 590<x_click<1085 and 60<y_click<590:
            if soundvar:
                sound=pygame.mixer.Sound("error.ogg")
                sound.play()
                continue

        #Try to undraw errors if there are any
        #and display the instructions again
        try:
            error_text.undraw()
            error_text2.undraw()
            for text in args:
                text.draw(win)
        except:
            GraphicsError

        #Allows users to change sound and music options
        original= music
        music=musicplay(music, 1100, 1175, 65, 15, music_box, win)
        if music != original:
            continue

        original=soundvar
        soundvar=soundplay(soundvar, 1185, 1260, 65, 15, sound_box, win)
        if soundvar != original:
            continue

        #If ship is appropriate length
        if len(location) is length:

            #If ship is placed correctly return the music and soundvar values
            #and break
            if Confirmer(confirmlist, location, boxloc, boxconf, confirmbox,
                         win, ship, soundvar):
                return music, soundvar
                break

            #undraw the instructions and draw the error text 
            else:
                if 1100<x_click< 1260 and 450<y_click<520:
                    try:
                       for text in args:
                           text.undraw()
                       error_text.draw(win)
                       error_text2.draw(win)
                    except:
                        GraphicsError

        #If nothing above is satisfied it moves to listappenders                       
        try:
            if win is winP1:
                ListofListAppenders1(soundvar)
        except:
            NameError
        try:
            if win is winP2:
                ListofListAppenders2(soundvar)
        except:
            NameError

        #If the confirmbox is clicked but the length isn't appropriate
        #play an error sound (if sound is true) and draw error text
        if 1100<x_click< 1260 and 450<y_click<520 and len(location) != length:

            if soundvar:
                sound=pygame.mixer.Sound("error.ogg")
                sound.play()
            
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
    global soundvar, music
    
    #winP1
    winP1=GraphWin("%s's Battleship Board" %player1_name, 1275, 650,
                   autoflush= False)

    #Confirmbox
    confirmP1= Rectangle(Point(1100, 450), Point(1260, 520))

    #Colors
    winP1.setBackground("cyan3")

    text_box.setFill("AntiqueWhite")
    confirmP1.setFill("AntiqueWhite")

    #Drawing
    attack.draw(winP1)
    fleet.draw(winP1)
    text_box.draw(winP1)

    #Checker boxes
    airbox=Rectangle(Point(1225, 220), Point(1245, 240))
    bshipbox=Rectangle(Point(1225, 252.5), Point(1245, 272.5))
    frigbox=Rectangle(Point(1225, 285), Point(1245, 305))
    subbox=Rectangle(Point(1225, 317.5), Point(1245, 337.5))
    patbox=Rectangle(Point(1225, 350), Point(1245, 370))

    #Drawing checker boxes
    airbox.draw(winP1)
    bshipbox.draw(winP1)
    frigbox.draw(winP1)
    subbox.draw(winP1)
    patbox.draw(winP1)

    #Drawer function and update
    drawer1(winP1, music, soundvar)

    winP1.update()

    #If player is in ship placing stage
    if "1"== stage:
        #Draw confirmbox and set all of the checker boxes green
        #(no ship is sunk yet). 
        confirmP1.draw(winP1)
        airbox.setFill("SpringGreen2")
        bshipbox.setFill("SpringGreen2")
        subbox.setFill("SpringGreen2")
        frigbox.setFill("SpringGreen2")
        patbox.setFill("SpringGreen2")

        #Text
        confirm_title.draw(winP1)

        instruct_text1.draw(winP1)
        instruct_text2.draw(winP1)

        #Aircraft carrier looper + sound and music variable setting
        music, soundvar=Looper(5, winP1, Player1_Locations, P1confirmlist,
                               P1BoxLoc, P1BoxConf, confirmP1, "Aircraft",
                               soundvar, music, instruct_text1, instruct_text2)
        for point in P1BoxConf:
            Aircraft1.append(point)

        #Text
        instruct_text1.undraw()
        instruct_text2.undraw()
        
        instruct_text3.draw(winP1)
        instruct_text4.draw(winP1)

        #Battleship looper + sound and music variable setting
        music, soundvar= Looper(9, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1,
                                "Battleship", soundvar, music, instruct_text3,
                                instruct_text4)
        for point in range(5, 9):
            Bship1.append(P1BoxConf[point])

        #Text
        instruct_text3.undraw()
        instruct_text4.undraw()

        instruct_text5.draw(winP1)
        instruct_text7.draw(winP1)

        #Frigate looper + sound and music variable setting
        music, soundvar= Looper(12, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1,
                                "Frigate", soundvar, music,instruct_text5,
                                 instruct_text7)
        for point in range(9, 12):
            Frig1.append(P1BoxConf[point])

        #Text
        instruct_text5.undraw()

        instruct_text6.draw(winP1)

        #Submarine looper + sound and music variable setting
        music, soundvar= Looper(15, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1, "Submarine",
                                soundvar, music, instruct_text6, instruct_text7)
        for point in range(12, 15):
            Sub1.append(P1BoxConf[point])

        #Text
        instruct_text6.undraw()
        instruct_text7.undraw()

        instruct_text8.draw(winP1)
        instruct_text9.draw(winP1)
        instruct_text10.draw(winP1)

        #Patrol Boat looper + sound and music variable setting
        music, soundvar= Looper(17, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1, "Patrol",
                                soundvar, music, instruct_text8, instruct_text9,
                                instruct_text10)
        for point in range(15, 17):
            Pat1.append(P1BoxConf[point])

        #Text
        instruct_text8.undraw()
        instruct_text9.undraw()
        instruct_text10.undraw()

        time.sleep(0.25)

        #Change confirm title to Done! and draw done_text
        confirm_title.undraw()
        confirm_title= Text(Point(1180, 485), "Done!")
        confirm_title.draw(winP1)

        done_text.draw(winP1)
        done_text2.draw(winP1)

        done_text3= Text(Point(1175, 165), "the device to %s" %player2_name)
        done_text3.draw(winP1)

        #Wait for player to click done so Player2 can go
        while True:
            click_getter(winP1)
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                winP1.close()
                break

            #Also check if player wants to change sound or music options
            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65, 15, sound_box, winP1)
            if soundvar != original:
                continue

    #If player is in attacking stage
    elif "2"== stage:
        #Change confirm title, undraw confirm box, and draw captain text
        confirm_title= Text(Point(1180, 485), "Next Turn")
        confirmP1.undraw()

        captain_text.draw(winP1)

        #Get theamount of hits and misses Player1 has
        hitlen=len(P1hit)
        misslen=len(P1miss)

        #Check the status of all ships and fill in the boxes red or green
        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1,
                player2_name, soundvar)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1,
                player2_name, soundvar)
        checker(Pat2,"Patrol Boat", P1att, 0, 2, patbox, winP1, player2_name,
                soundvar)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1, player2_name,
                soundvar)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1, player2_name,
                soundvar)

        #Attacking
        while True:
            #Get amount of attacks Player1 has done
            length= len(P1att)

            #Get click
            x_click, y_click=click_getter(winP1)

            #Sound or music options based on click
            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65, 15, sound_box, winP1)
            if soundvar != original:
                continue

            #If click is in the Player's own fleet box and if sound is on
            #play the error sound
            if 35<x_click<530 and 60<y_click<590:
                if soundvar:
                    sound=pygame.mixer.Sound("error.ogg")
                    sound.play()
                continue

            #Use the coordinates of the click and see if the player attacked.
            #Fill in his radar accordingly
            attack1(soundvar)

            #If the length of the amount of attacks Player1 has done has
            #increased, that must mean he has taken his turn, and so it is over
            length2= len(P1att)
            if length2==length+1:
                break

        #Undraw
        captain_text.undraw()

        #If P1hit length has increased, draw that it's a hit
        if len(P1hit)==hitlen+1:
            hit_message.draw(winP1)

        #If P1miss length has increased, draw that it's a miss
        elif len(P1miss)==misslen+1:
            miss_message.draw(winP1)

        #Check the status of all of the ships again and fill in their
        #status box with the appropriate color
        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1,
                player2_name, soundvar)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1,
                player2_name, soundvar)
        checker(Pat2, "Patrol Boat", P1att, 0, 2, patbox, winP1, player2_name,
                soundvar)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1, player2_name,
                soundvar)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1, player2_name,
                soundvar)

        #If there is a winner, and it is Player1
        if winner()=="Player1":
            #Play the victory sound if it is on
            if soundvar:
                sound=pygame.mixer.Sound("victory.ogg")
                sound.play()

            #Draw winner text and buttons at bottom
            winner_text.draw(winP1)
            see_oth_player_box.draw(winP1)
            close_game.draw(winP1)

            see_oth_text= Text(Point(1180, 455), "See %s's Ships" %player2_name)
            see_oth_text.draw(winP1)
            close_game_text.draw(winP1)

            while True:
                #Get click
                click_getter(winP1)

                #Options for player to change music and sound
                original= music
                music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
                if music != original:
                    continue

                original=soundvar
                soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP1)
                if soundvar != original:
                    continue

                #If player wants to see his opponent's ships, go to stage3 of
                #the other player and show his win
                if single_detector(1100, 1260, 490, 420, see_oth_player_box,
                                   winP1) is True:
                    winP1.close()
                    Player2("3")

                #Or if the player just wants to close the game, exit
                elif single_detector(1100, 1260, 580, 510, close_game,
                                     winP1) is True:
                    time.sleep(0.3)
                    winP1.close()
                    sys.exit()

        #If there is no winner draw the confirm text and box
        confirmP1.draw(winP1)
        confirm_title.draw(winP1)

        
        while True:
            #Get click
            click_getter(winP1)

            #Player can toggle sound and music
            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP1)
            if soundvar != original:
                continue

            #If the next turn box is clicked, close the win and break the loop,
            #starting Player2's turn
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                time.sleep(0.1)
                winP1.close()
                break

    #If someone wins the game and wants to view Player1's ships
    elif "3"== stage:
        #Display text depending on the winner
        if winner()=="Player2":
            oth_winner_text=Text(Point(1175, 115), "%s won!" %player2_name)
            
        elif winner()=="Player1":
            oth_winner_text=Text(Point(1175, 115), "%s won!" %player1_name)
        
        oth_winner_text.draw(winP1)

        #Set all of the ship status boxes to red
        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1,
                player2_name)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1,
                player2_name)
        checker(Pat2, "Patrol Boat", P1att, 0, 2, patbox, winP1, player2_name)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1, player2_name)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1, player2_name)

        #Draw boxes and text
        see_oth_player_box.draw(winP1)
        close_game.draw(winP1)
        close_game_text.draw(winP1)

        see_oth_text= Text(Point(1180, 455), "See %s's Ships" %player2_name)
        see_oth_text.draw(winP1)

        while True:
            #Get click
            click_getter(winP1)

            #Toggle music and sound options
            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP1)
            if soundvar != original:
                continue

            #If the player selects the "see opponent ships" box, close the
            #window and go to Player2's third stage
            if single_detector(1100, 1260, 490, 420, see_oth_player_box,
                               winP1) is True:
                winP1.close()
                Player2("3")

            #If the player selects the "close game" box, exit the system
            elif single_detector(1100, 1260, 580, 510, close_game,
                                 winP1) is True:
                time.sleep(0.3)
                winP1.close()
                sys.exit()      

    winP1.close()
                        
#####################
def Player2(stage):
    global winP2, click, confirmP2, Player2_Locations, confirm_title
    global Aircraft2, Pat2, Sub2, Frig2, Bship2
    global soundvar, music

    winP2=GraphWin("%s's Battleship Board" %player2_name, 1275, 650,
                   autoflush=False)
    
    confirmP2= Rectangle(Point(1100, 450), Point(1260, 520))
    confirm_title= Text(Point(1180, 485), "Confirm")
    
    winP2.setBackground("cyan3")

    text_box.setFill("AntiqueWhite")
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

    drawer2(winP2, music, soundvar)

    winP2.update()

    if "1"== stage:
        confirmP2.draw(winP2)
        airbox.setFill("SpringGreen2")
        bshipbox.setFill("SpringGreen2")
        subbox.setFill("SpringGreen2")
        frigbox.setFill("SpringGreen2")
        patbox.setFill("SpringGreen2")
        
        confirm_title.draw(winP2)

        instruct_text1.draw(winP2)
        instruct_text2.draw(winP2)

        music, soundvar= Looper(5, winP2, Player2_Locations, P2confirmlist,
                                P2BoxLoc, P2BoxConf, confirmP2, "Aircraft",
                                soundvar, music, instruct_text1, instruct_text2)
        for point in P2BoxConf:
            Aircraft2.append(point)

        instruct_text1.undraw()
        instruct_text2.undraw()

        instruct_text3.draw(winP2)
        instruct_text4.draw(winP2)
        
        music, soundvar= Looper(9, winP2, Player2_Locations, P2confirmlist,
                                P2BoxLoc, P2BoxConf, confirmP2, "Battleship",
                                soundvar, music, instruct_text3, instruct_text4)
        for point in range(5, 9):
            Bship2.append(P2BoxConf[point])

        instruct_text3.undraw()
        instruct_text4.undraw()

        instruct_text5.draw(winP2)
        instruct_text7.draw(winP2)

        music, soundvar= Looper(12, winP2, Player2_Locations, P2confirmlist,
                                P2BoxLoc, P2BoxConf, confirmP2, "Frigate",
                                soundvar, music, instruct_text5, instruct_text7)
        for point in range(9, 12):
            Frig2.append(P2BoxConf[point])

        instruct_text5.undraw()

        instruct_text6.draw(winP2)

        music, soundvar=Looper(15, winP2, Player2_Locations, P2confirmlist,
                               P2BoxLoc, P2BoxConf, confirmP2, "Submarine",
                               soundvar, music, instruct_text6, instruct_text7)
        for point in range(12, 15):
            Sub2.append(P2BoxConf[point])

        instruct_text6.undraw()
        instruct_text7.undraw()

        instruct_text8.draw(winP2)
        instruct_text9.draw(winP2)
        instruct_text10.draw(winP2)

        music, soundvar= Looper(17, winP2, Player2_Locations, P2confirmlist,
                                P2BoxLoc, P2BoxConf,confirmP2, "Patrol",
                                soundvar, music, instruct_text8, instruct_text9,
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

        done_text4=Text(Point(1175, 165), "the device to %s" %player1_name)
        done_text4.draw(winP2)
        
        while True:
            click_getter(winP2)
            if single_detector(1100, 1260, 520, 450, confirmP2, winP2) is True:
                winP2.close()
                break

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP2)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP2)
            if soundvar != original:
                continue
            
    elif "2"== stage:
        confirm_title= Text(Point(1180, 485), "Next Turn")
        captain_text.draw(winP2)

        hitlen=len(P2hit)
        misslen=len(P2miss)
        
        checker(Aircraft1,"Aircraft Carrier", P2att, 0, 5, airbox, winP2,
                player1_name, soundvar)
        checker(Bship1,"Battleship", P2att, 0, 4, bshipbox, winP2, player1_name,
                soundvar)
        checker(Pat1, "Patrol Boat", P2att, 0, 2, patbox, winP2, player1_name,
                soundvar)
        checker(Sub1, "Submarine" ,P2att, 0, 3, subbox, winP2, player1_name,
                soundvar)
        checker(Frig1,"Frigate", P2att, 0, 3, frigbox, winP2, player1_name,
                soundvar)
        
        while True:
            length= len(P2att)
            x_click, y_click=click_getter(winP2)

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP2)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65, 15, sound_box, winP2)
            if soundvar != original:
                continue

            if 35<x_click<530 and 60<y_click<590:
                if soundvar:
                    sound=pygame.mixer.Sound("error.ogg")
                    sound.play()
                    continue
            
            attack2(soundvar)
            length2= len(P2att)
            if length2==length+1:
                break

        captain_text.undraw()

        if len(P2hit)==hitlen+1:
            hit_message.draw(winP2)

        elif len(P2miss)==misslen+1:
            miss_message.draw(winP2)

        checker(Aircraft1, "Aircraft Carrier", P2att, 0, 5, airbox, winP2,
                player1_name, soundvar)       
        checker(Bship1,"Battleship", P2att, 0, 4, bshipbox, winP2, player1_name,
                soundvar)
        checker(Pat1, "Patrol Boat", P2att, 0, 2, patbox, winP2, player1_name,
                soundvar)
        checker(Sub1, "Submarine", P2att, 0, 3, subbox, winP2, player1_name,
                soundvar)
        checker(Frig1, "Frigate", P2att, 0, 3, frigbox, winP2, player1_name,
                soundvar)

        if winner()=="Player2":
            if soundvar:
                sound=pygame.mixer.Sound("victory.ogg")
                sound.play()
            winner_text.draw(winP2)
            see_oth_player_box.draw(winP2)
            close_game.draw(winP2)

            see_oth_text= Text(Point(1180, 455), "See %s's Ships" %player1_name)
            see_oth_text.draw(winP2)
            close_game_text.draw(winP2)

            while True:
                click_getter(winP2)

                original= music
                music=musicplay(music, 1100, 1175, 65, 15, music_box, winP2)
                if music != original:
                    continue

                original=soundvar
                soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP2)
                if soundvar != original:
                    continue

                if single_detector(1100, 1260, 490, 420, see_oth_player_box,
                                   winP2) is True:
                    winP2.close()
                    Player1("3")

                elif single_detector(1100, 1260, 580, 510, close_game,
                                     winP2) is True:
                    time.sleep(0.3)
                    winP2.close()
                    sys.exit()

        confirmP2.draw(winP2)
        confirm_title.draw(winP2)
        
        while True:
            click_getter(winP2)

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP2)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP2)
            if soundvar != original:
                continue
            
            if single_detector(1100, 1260, 520, 450, confirmP2, winP2) is True:
                time.sleep(0.1)
                break

    elif "3"== stage:
        if winner()=="Player1":
            oth_winner_text=Text(Point(1175, 115), "%s won!" %player1_name)
            
        elif winner()=="Player2":
            oth_winner_text=Text(Point(1175, 115), "%s won!" %player2_name)
            
        oth_winner_text.draw(winP2)

        checker(Aircraft1, "Aircraft Carrier", P2att, 0, 5, airbox, winP2,
                player1_name)       
        checker(Bship1,"Battleship", P2att, 0, 4, bshipbox, winP2, player1_name)
        checker(Pat1, "Patrol Boat", P2att, 0, 2, patbox, winP2, player1_name)
        checker(Sub1, "Submarine", P2att, 0, 3, subbox, winP2, player1_name)
        checker(Frig1, "Frigate", P2att, 0, 3, frigbox, winP2, player1_name)
            
        see_oth_player_box.draw(winP2)
        close_game.draw(winP2)
        close_game_text.draw(winP2)

        see_oth_text= Text(Point(1180, 455), "See %s's Ships" %player1_name)
        see_oth_text.draw(winP2)

        while True:
            click_getter(winP2)

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP2)
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP2)
            if soundvar != original:
                continue

            if single_detector(1100, 1260, 490, 420, see_oth_player_box,
                               winP2) is True:
                winP2.close()
                Player1("3")

            elif single_detector(1100, 1260, 580, 510, close_game,
                                 winP2) is True:
                time.sleep(0.3)
                winP2.close()
                sys.exit() 

    winP2.close()



#################################################################################

Player1('1')
Player2('1')

while True:
    #Player1's run
    Player1('2')
    Instructions('2', '', player2_name)
 
    #Player2's run
    Player2('2')
    Instructions('2', '', player1_name)

writer= open("Pickler.py", "wb")
pickle.dump("", writer, protocol=2)
writer.close()






