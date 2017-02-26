import time
import pickle
import zellegraphics
from var import *
import threading

xvar=-1
liststart=-1
yvar=-1
boxvar=-1

#next_detector
def next_detector(ok_left, ok_right, ok_top, ok_bottom, box, win):
    while True:
        click= win.getMouse()
        x_click=click.getX()
        y_click=click.getY()
        if ok_left< x_click < ok_right and ok_bottom < y_click < ok_top:
            (box).setFill("white")
            time.sleep(0.10)
            (box).setFill("AntiqueWhite2")
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
            time.sleep(0.10)
            yes.setFill("AntiqueWhite2")
            return True
            time.sleep(0.25)
            break
        elif no_left < x_click < no_right and no_bottom < y_click < no_top:
            no.setFill("white")
            time.sleep(0.12)
            no.setFill("AntiqueWhite2")
            return False
            break

###########################################################################

#singledetector
def single_detector(ok_left, ok_right, ok_top, ok_bottom, box, win):
        try:
                reciever= open("Pickler.py", "rb")
                clicks=pickle.load(reciever)
                reciever.close()
                x_click, y_click= clicks
        except:
                NameError

        if ok_left< x_click < ok_right and ok_bottom < y_click < ok_top:
            (box).setFill("white")
            time.sleep(0.10)
            (box).setFill("AntiqueWhite2")
            return True

#AfterFiller
def AfterFiller(square1 ,square2,location, confirmed_spot_list):
    if square2 in confirmed_spot_list:
        (square1).setFill("slategray")

    elif square2 in location and square2 not in confirmed_spot_list:
        (square1).setFill("gray")

    elif square2 not in location:
        (square1).setFill("cyan4")

#FinalFiller1
def FinalFiller1():
    for i in range(10):
        AfterFiller(boxrunner(BoxesP1A), stringrun(Astr) , Player1_Locations,
                    P1confirmlist)
    for i in range(10):
        AfterFiller(boxrunner(BoxesP1B), stringrun(Bstr), Player1_Locations,
                    P1confirmlist)
    for i in range(10):
        AfterFiller(boxrunner(BoxesP1C), stringrun(Cstr), Player1_Locations,
                    P1confirmlist)
    for i in range(10):
        AfterFiller(boxrunner(BoxesP1D), stringrun(Dstr), Player1_Locations,
                    P1confirmlist)
    for i in range(10):
        AfterFiller(boxrunner(BoxesP1E), stringrun(Estr), Player1_Locations,
                    P1confirmlist)
    for i in range(10):
        AfterFiller(boxrunner(BoxesP1F), stringrun(Fstr), Player1_Locations,
                    P1confirmlist)

#FinalFiller2
def FinalFiller2():
    pass

#ListAppender
def ListAppender(left, right, top, bottom, location, appender,
                 confirmlist):
    reader= open("Pickler.py", "rb")
    x_click, y_click=pickle.load(reader)
    reader.close()

    if left<x_click<right and bottom>y_click>top:

        if (appender) not in location:
            (location).append(appender)

        elif (appender) in location and (appender) not in confirmlist:
            (location).remove(appender)

#Listoflistappenders1
def ListofListAppenders1():
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 60, 113, Player1_Locations,
                     stringrun(Astr), P1confirmlist)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 113, 166, Player1_Locations,
                     stringrun(Bstr), P1confirmlist)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 166, 219, Player1_Locations,
                     stringrun(Cstr), P1confirmlist)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 219, 272, Player1_Locations,
                     stringrun(Dstr), P1confirmlist)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 272, 325, Player1_Locations,
                     stringrun(Estr), P1confirmlist)
    for i in range(10):
        ListAppender(leftbound(), rightbound(), 325, 378, Player1_Locations,
                     stringrun(Fstr), P1confirmlist)

#Listoflistappenders2
def ListofListAppenders2():
    pass

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

#clickgetter
def click_getter(win):
        click=win.getMouse()
        x_click=click.getX()
        y_click=click.getY()
        clicknames=[x_click, y_click]

        writer= open("Pickler.py", "wb")
        pickle.dump(clicknames, writer, protocol=2)
        writer.close()
