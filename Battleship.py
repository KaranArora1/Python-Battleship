#!/usr/local/bin/python3

import pickle
import time
import sys
import pygame
from definitions import *
from starter import *
from var import *
from zellegraphics import *

#Instructions
'''player1_name, player2_name, music, soundvar=Instructions("1", "Start")'''

player1_name= "Karan"
player2_name= "Rajan"
soundvar=False
music=False

pygame.init()

if music:
    pygame.mixer.music.load("seamusic.mp3")
    pygame.mixer.music.play(-1)

#########################################################################
#Confirmer
def Confirmer(conflist, stringli, boxloc, boxconf,confirmbox, win, ship,
              soundvar):
    if single_detector_conf(1100, 1260, 520, 450, confirmbox, win, ship,
                            conflist, soundvar) is True:
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
           ship, soundvar, music, *args):
    
    global x_click, y_click, confirmP1
    while True:
        x_click, y_click=click_getter(win)
        if 590<x_click<1085 and 60<y_click<590:
            if soundvar:
                sound=pygame.mixer.Sound("error.ogg")
                sound.play()
                continue
        try:
            error_text.undraw()
            error_text2.undraw()
            for text in args:
                text.draw(win)
        except:
            GraphicsError

        original= music
        music=musicplay(music, 1100, 1175, 65, 15, music_box, win)
        if music==None:
            music=original
        if music != original:
            continue

        original=soundvar
        soundvar=soundplay(soundvar, 1185, 1260, 65, 15, sound_box, win)
        if soundvar==None:
            soundvar=original
        if soundvar != original:
            continue
            
        if len(location) is length:
            
            if Confirmer(confirmlist, location, boxloc, boxconf, confirmbox,
                         win, ship, soundvar):
                return music, soundvar
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
                ListofListAppenders1(soundvar)
        except:
            NameError
        try:
            if win is winP2:
                ListofListAppenders2(soundvar)
        except:
            NameError

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

    winP1=GraphWin("%s's Battleship Board" %player1_name, 1275, 650,
                   autoflush= False)
    
    confirmP1= Rectangle(Point(1100, 450), Point(1260, 520))

    winP1.setBackground("cyan3")

    text_box.setFill("AntiqueWhite")
    confirmP1.setFill("AntiqueWhite")
    
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
    
    drawer1(winP1, music, soundvar)

    winP1.update()

    if "1"== stage:
        confirmP1.draw(winP1)
        airbox.setFill("SpringGreen2")
        bshipbox.setFill("SpringGreen2")
        subbox.setFill("SpringGreen2")
        frigbox.setFill("SpringGreen2")
        patbox.setFill("SpringGreen2")
        
        confirm_title.draw(winP1)

        instruct_text1.draw(winP1)
        instruct_text2.draw(winP1)
        
        music, soundvar=Looper(5, winP1, Player1_Locations, P1confirmlist,
                               P1BoxLoc, P1BoxConf, confirmP1, "Aircraft",
                               soundvar, music, instruct_text1, instruct_text2)
        for point in P1BoxConf:
            Aircraft1.append(point)

        instruct_text1.undraw()
        instruct_text2.undraw()
        
        instruct_text3.draw(winP1)
        instruct_text4.draw(winP1)

        music, soundvar= Looper(9, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1,
                                "Battleship", soundvar, music, instruct_text3,
                                instruct_text4)
        for point in range(5, 9):
            Bship1.append(P1BoxConf[point])

        instruct_text3.undraw()
        instruct_text4.undraw()

        '''instruct_text5.draw(winP1)
        instruct_text7.draw(winP1)

        music, soundvar= Looper(12, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1,
                                "Frigate", soundvar, music,instruct_text5,
                                 instruct_text7)
        for point in range(9, 12):
            Frig1.append(P1BoxConf[point])

        instruct_text5.undraw()

        instruct_text6.draw(winP1)

        music, soundvar= Looper(15, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1, "Submarine",
                                soundvar, music, instruct_text6, instruct_text7)
        for point in range(12, 15):
            Sub1.append(P1BoxConf[point])

        instruct_text6.undraw()
        instruct_text7.undraw()

        instruct_text8.draw(winP1)
        instruct_text9.draw(winP1)
        instruct_text10.draw(winP1)

        music, soundvar= Looper(17, winP1, Player1_Locations, P1confirmlist,
                                P1BoxLoc, P1BoxConf, confirmP1, "Patrol",
                                soundvar, music, instruct_text8, instruct_text9,
                                instruct_text10)
        for point in range(15, 17):
            Pat1.append(P1BoxConf[point])

        instruct_text8.undraw()
        instruct_text9.undraw()
        instruct_text10.undraw()

        time.sleep(0.25)'''
        
        confirm_title.undraw()
        confirm_title= Text(Point(1180, 485), "Done!")
        confirm_title.draw(winP1)

        done_text.draw(winP1)
        done_text2.draw(winP1)

        done_text3= Text(Point(1175, 165), "the device to %s" %player2_name)
        done_text3.draw(winP1)

        while True:
            click_getter(winP1)
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                winP1.close()
                break
            
    elif "2"== stage:
        confirm_title= Text(Point(1180, 485), "Next Turn")
        confirmP1.undraw()

        captain_text.draw(winP1)

        hitlen=len(P1hit)
        misslen=len(P1miss)
        
        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1,
                player2_name)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1,
                player2_name)
        checker(Pat2,"Patrol Boat", P1att, 0, 2, patbox, winP1, player2_name)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1, player2_name)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1, player2_name)
        
        while True:
            length= len(P1att)
            x_click, y_click=click_getter(winP1)

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
            if music==None:
                music=original

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65, 15, sound_box, winP1)
            if soundvar==None:
                soundvar=original

            if 35<x_click<530 and 60<y_click<590:
                if soundvar:
                    sound=pygame.mixer.Sound("error.ogg")
                    sound.play()
                continue
            
            attack1(soundvar)
            
            length2= len(P1att)
            if length2==length+1:
                break

        captain_text.undraw()

        if len(P1hit)==hitlen+1:
            hit_message.draw(winP1)
            
        elif len(P1miss)==misslen+1:
            miss_message.draw(winP1)
        
        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1,
                player2_name)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1,
                player2_name)
        checker(Pat2, "Patrol Boat", P1att, 0, 2, patbox, winP1, player2_name)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1, player2_name)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1, player2_name)

        if winner()=="Player1":
            if soundvar:
                sound=pygame.mixer.Sound("victory.ogg")
                sound.play()
            winner_text.draw(winP1)
            see_oth_player_box.draw(winP1)
            close_game.draw(winP1)

            see_oth_text= Text(Point(1180, 455), "See %s's Ships" %player2_name)
            see_oth_text.draw(winP1)
            close_game_text.draw(winP1)

            while True:
                click_getter(winP1)

                original= music
                music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
                if music==None:
                    music=original
                if music != original:
                    continue

                original=soundvar
                soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP1)
                if soundvar==None:
                    soundvar=original
                if soundvar != original:
                    continue
    
                if single_detector(1100, 1260, 490, 420, see_oth_player_box,
                                   winP1) is True:
                    winP1.close()
                    Player2("3")

                elif single_detector(1100, 1260, 580, 510, close_game,
                                     winP1) is True:
                    time.sleep(0.3)
                    winP1.close()
                    sys.exit()

        confirmP1.draw(winP1)
        confirm_title.draw(winP1)
                
        while True:
            click_getter(winP1)

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
            if music==None:
                music=original
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP1)
            if soundvar==None:
                soundvar=original
            if soundvar != original:
                continue
                
            if single_detector(1100, 1260, 520, 450, confirmP1, winP1) is True:
                time.sleep(0.1)
                winP1.close()
                break
            
    elif "3"== stage:
        if winner()=="Player2":
            oth_winner_text=Text(Point(1175, 115), "%s won!" %player2_name)
            
        elif winner()=="Player1":
            oth_winner_text=Text(Point(1175, 115), "%s won!" %player1_name)
        
        oth_winner_text.draw(winP1)

        checker(Aircraft2, "Aircraft Carrier", P1att, 0, 5, airbox, winP1,
                player2_name)
        checker(Bship2, "Battleship", P1att, 0, 4, bshipbox, winP1,
                player2_name)
        checker(Pat2, "Patrol Boat", P1att, 0, 2, patbox, winP1, player2_name)
        checker(Sub2, "Submarine", P1att, 0, 3, subbox, winP1, player2_name)
        checker(Frig2, "Frigate", P1att, 0, 3, frigbox, winP1, player2_name)
            
        see_oth_player_box.draw(winP1)
        close_game.draw(winP1)
        close_game_text.draw(winP1)

        see_oth_text= Text(Point(1180, 455), "See %s's Ships" %player2_name)
        see_oth_text.draw(winP1)
            
        while True:
            click_getter(winP1)

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP1)
            if music==None:
                music=original
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP1)
            if soundvar==None:
                soundvar=original
            if soundvar != original:
                continue

            if single_detector(1100, 1260, 490, 420, see_oth_player_box,
                               winP1) is True:
                winP1.close()
                Player2("3")

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

        '''instruct_text3.draw(winP2)
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

        time.sleep(0.25)'''
        
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
            
    elif "2"== stage:
        confirm_title= Text(Point(1180, 485), "Next Turn")
        captain_text.draw(winP2)

        hitlen=len(P2hit)
        misslen=len(P2miss)
        
        checker(Aircraft1,"Aircraft Carrier", P2att, 0, 5, airbox, winP2,
                player1_name)
        checker(Bship1,"Battleship", P2att, 0, 4, bshipbox, winP2, player1_name)
        checker(Pat1, "Patrol Boat", P2att, 0, 2, patbox, winP2, player1_name)
        checker(Sub1, "Submarine" ,P2att, 0, 3, subbox, winP2, player1_name)
        checker(Frig1,"Frigate", P2att, 0, 3, frigbox, winP2, player1_name)
        
        while True:
            length= len(P2att)
            x_click, y_click=click_getter(winP2)

            original= music
            music=musicplay(music, 1100, 1175, 65, 15, music_box, winP2)
            if music==None:
                music=original

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65, 15, sound_box, winP2)
            if soundvar==None:
                soundvar=original

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
                player1_name)       
        checker(Bship1,"Battleship", P2att, 0, 4, bshipbox, winP2, player1_name)
        checker(Pat1, "Patrol Boat", P2att, 0, 2, patbox, winP2, player1_name)
        checker(Sub1, "Submarine", P2att, 0, 3, subbox, winP2, player1_name)
        checker(Frig1, "Frigate", P2att, 0, 3, frigbox, winP2, player1_name)

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
                if music==None:
                    music=original
                if music != original:
                    continue

                original=soundvar
                soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP2)
                if soundvar==None:
                    soundvar=original
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
            if music==None:
                music=original
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP2)
            if soundvar==None:
                soundvar=original
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
            if music==None:
                music=original
            if music != original:
                continue

            original=soundvar
            soundvar=soundplay(soundvar, 1185, 1260, 65,15,sound_box, winP2)
            if soundvar==None:
                soundvar=original
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

'''os.startfile('/Users/karanarora/Desktop')'''

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






