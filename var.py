from zellegraphics import *

#Global text and Setfills
fleet= Rectangle(Point(35, 60), Point(530, 590))
attack= Rectangle(Point(590, 60), Point(1085, 590))
text_box= Rectangle(Point(1100, 80), Point(1260, 385))

see_oth_player_box=Rectangle(Point(1100, 420), Point(1260, 490))
close_game= Rectangle(Point(1100, 510), Point(1260, 580))

fleet_title= Text(Point(282.5, 20), "FLEET")
radar_title= Text(Point(837.5, 20), "RADAR")
confirm_title= Text(Point(1180, 485), "Confirm")

dialogue_line=Line(Point(1150, 100), Point(1200, 100))
OPship_line= Line(Point(1140, 210), Point(1210, 210))
fleet_line=Line(Point(257.5, 28), Point(307.5, 28))
radar_line=Line(Point(807.5, 28), Point(867.5, 28))

text_box_title=Text(Point(1175, 95), "Dialogue")
other_player_ships_title= Text(Point(1175, 205), "Enemy Ships")

airtext=Text(Point(1154, 230), "Aircraft Carrier  =")
bshiptext=Text(Point(1142, 262.5), "Battleship  =")
frigtext=Text(Point(1136, 295), "Frigate  =")
subtext=Text(Point(1146, 327.5), "Submarine  =")
pattext=Text(Point(1146, 360), "Patrol Boat  =")

error_text=Text(Point(1170, 115), "Your ship cannot be")
error_text2=Text(Point(1170, 135), "arranged like that!")

instruct_text1= Text(Point(1175, 115), "Place your Aircraft Carrier!")
instruct_text2= Text(Point(1175, 135), "(5 points)")

instruct_text3= Text(Point(1175, 115), "Place your Battleship!")
instruct_text4= Text(Point(1175, 135), "(4 points)")

instruct_text5= Text(Point(1175, 115), "Place your Frigate!")
instruct_text6= Text(Point(1175, 115), "Place your Submarine!")
instruct_text7= Text(Point(1175, 135), "(3 points)")

instruct_text8= Text(Point(1175, 115), "Finally, place your")
instruct_text9= Text(Point(1175, 132.5), "Patrol Boat!")
instruct_text10= Text(Point(1175, 160), "(2 points)")

done_text= Text(Point(1175, 115), "You're finished!")
done_text2= Text(Point(1175, 145), "Click 'Done' and pass")

hit_message= Text(Point(1175, 115), "It's a hit!")
miss_message= Text(Point(1175, 115), "It's a miss.")

winner_text= Text(Point(1175, 180), "You have won the game!")

close_game_text= Text(Point(1180, 545), "Close Game")

fleet.setFill("cyan4")
attack.setFill("cyan4")
see_oth_player_box.setFill("AntiqueWhite")
close_game.setFill("AntiqueWhite")

fleet_title.setSize(16)
radar_title.setSize(16)
winner_text.setSize(11)

winner_text.setStyle("italic")

#Text
A_text=Text(Point(20, 86.5), "A")
B_text=Text(Point(20, 139.5), "B")
C_text=Text(Point(20, 192.5), "C")
D_text=Text(Point(20, 245.5), "D")
E_text=Text(Point(20, 298.5), "E")
F_text=Text(Point(20, 351.5), "F")
G_text=Text(Point(20, 404.5), "G")
H_text=Text(Point(20, 457.5), "H")
I_text=Text(Point(20, 510.5), "I")
J_text=Text(Point(20, 563.5), "J")

one=Text(Point(59.75, 45), "1")
two=Text(Point(109.25, 45), "2")
three=Text(Point(158.75, 45),"3")
four=Text(Point(208.25, 45),"4")
five=Text(Point(257.25, 45),"5")
six=Text(Point(307.25, 45),"6")
seven=Text(Point(356.75, 45),"7")
eight=Text(Point(406.25, 45),"8")
nine=Text(Point(455.75, 45),"9")
ten=Text(Point(505.25, 45),"10")

oth_A=Text(Point(575, 86.5), "A")
oth_B=Text(Point(575, 139.5),"B")
oth_C=Text(Point(575,192.5),"C")
oth_D=Text(Point(575,245.5),"D")
oth_E=Text(Point(575,298.5),"E")
oth_F=Text(Point(575,351.5),"F")
oth_G=Text(Point(575,404.5),"G")
oth_H=Text(Point(575,457.5),"H")
oth_I=Text(Point(575,510.5),"I")
oth_J=Text(Point(575,563.5),"J")

oth_one=Text(Point(614.75, 45),"1")
oth_two=Text(Point(664.25, 45),"2")
oth_three=Text(Point(713.75, 45),"3")
oth_four=Text(Point(763.25, 45),"4")
oth_five=Text(Point(812.75, 45),"5")
oth_six=Text(Point(862.25, 45),"6")
oth_seven=Text(Point(911.75, 45),"7")
oth_eight=Text(Point(961.75, 45),"8")
oth_nine=Text(Point(1010.75, 45),"9")
oth_ten=Text(Point(1060.25, 45),"10")

#Player1Board
#A
A1_1=Rectangle(Point(35, 60), Point(84.5, 113))
A2_1=Rectangle(Point(84.5, 60 ), Point(134, 113))
A3_1=Rectangle(Point(134, 60), Point(183.5, 113))
A4_1=Rectangle(Point(183.5, 60), Point(233, 113))
A5_1=Rectangle(Point(233, 60), Point(282.5, 113))
A6_1=Rectangle(Point(282.5, 60), Point(332, 113))
A7_1=Rectangle(Point(332, 60), Point(381.5, 113))
A8_1=Rectangle(Point(381.5, 60), Point(431, 113))
A9_1=Rectangle(Point(431, 60), Point(480.5, 113))
A10_1=Rectangle(Point(480.5, 60), Point(530, 113))

#B
B1_1= Rectangle(Point(35, 113), Point(84.5, 166))
B2_1= Rectangle(Point(84.5, 113), Point(134, 166))
B3_1= Rectangle(Point(134, 113), Point(183.5, 166))
B4_1= Rectangle(Point(183.5, 113), Point(233, 166))
B5_1= Rectangle(Point(233, 113), Point(282.5, 166))
B6_1= Rectangle(Point(282.5, 113), Point(332, 166))
B7_1= Rectangle(Point(332, 113), Point(381.5, 166))
B8_1= Rectangle(Point(381.5, 113), Point(431, 166))
B9_1= Rectangle(Point(431, 113), Point(480.5, 166))
B10_1= Rectangle(Point(480.5, 113), Point(530, 166))

#C
C1_1= Rectangle(Point(35, 166), Point(84.5, 219))
C2_1=Rectangle(Point(84.5, 166), Point(134, 219))
C3_1=Rectangle(Point(134, 166), Point(183.5, 219))
C4_1=Rectangle(Point(183.5, 166), Point(233, 219))
C5_1=Rectangle(Point(233, 166), Point(282.5, 219))
C6_1=Rectangle(Point(282.5, 166), Point(332, 219))
C7_1=Rectangle(Point(332, 166), Point(381.5, 219))
C8_1=Rectangle(Point(381.5, 166), Point(431, 219))
C9_1=Rectangle(Point(431, 166), Point(480.5, 219))
C10_1=Rectangle(Point(480.5, 166), Point(530, 219))

#D
D1_1=Rectangle(Point(35, 219), Point(84.5, 272))
D2_1=Rectangle(Point(84.5, 219), Point(134, 272))
D3_1=Rectangle(Point(134, 219), Point(183.5, 272))
D4_1=Rectangle(Point(183.5, 219), Point(233, 272))
D5_1=Rectangle(Point(233, 219), Point(282.5, 272))
D6_1=Rectangle(Point(282.5, 219), Point(332, 272))
D7_1=Rectangle(Point(332, 219), Point(381.5, 272))
D8_1=Rectangle(Point(381.5, 219), Point(431, 272))
D9_1=Rectangle(Point(431, 219), Point(480.5, 272))
D10_1=Rectangle(Point(480.5, 219), Point(530, 272))

#E
E1_1=Rectangle(Point(35, 272), Point(84.5, 325))
E2_1=Rectangle(Point(84.5, 272), Point(134, 325))
E3_1=Rectangle(Point(134, 272), Point(183.5, 325))
E4_1=Rectangle(Point(183.5, 272), Point(233, 325))
E5_1=Rectangle(Point(233, 272), Point(282.5, 325))
E6_1=Rectangle(Point(282.5, 272), Point(332, 325))
E7_1=Rectangle(Point(332, 272), Point(381.5, 325))
E8_1=Rectangle(Point(381.5, 272), Point(431, 325))
E9_1=Rectangle(Point(431, 272), Point(480.5, 325))
E10_1=Rectangle(Point(480.5, 272), Point(530, 325))

#F
F1_1=Rectangle(Point(35, 325), Point(84.5, 378))
F2_1=Rectangle(Point(84.5, 325), Point(134, 378))
F3_1=Rectangle(Point(134, 325), Point(183.5, 378))
F4_1=Rectangle(Point(183.5, 325), Point(233, 378))
F5_1=Rectangle(Point(233, 325), Point(282.5, 378))
F6_1=Rectangle(Point(282.5, 325), Point(332, 378))
F7_1=Rectangle(Point(332, 325), Point(381.5, 378))
F8_1=Rectangle(Point(381.5, 325), Point(431, 378))
F9_1=Rectangle(Point(431, 325), Point(480.5, 378))
F10_1=Rectangle(Point(480.5, 325), Point(530, 378))

#G
G1_1=Rectangle(Point(35, 378), Point(84.5, 431))
G2_1=Rectangle(Point(84.5, 378), Point(134, 431))
G3_1=Rectangle(Point(134, 378), Point(183.5, 431))
G4_1=Rectangle(Point(183.5, 378), Point(233, 431))
G5_1=Rectangle(Point(233, 378), Point(282.5, 431))
G6_1=Rectangle(Point(282.5, 378), Point(332, 431))
G7_1=Rectangle(Point(332, 378), Point(381.5, 431))
G8_1=Rectangle(Point(381.5, 378), Point(431, 431))
G9_1=Rectangle(Point(431, 378), Point(480.5, 431))
G10_1=Rectangle(Point(480.5, 378), Point(530, 431))

#H
H1_1=Rectangle(Point(35, 431), Point(84.5, 484))
H2_1=Rectangle(Point(84.5, 431), Point(134, 484))
H3_1=Rectangle(Point(134, 431), Point(183.5, 484))
H4_1=Rectangle(Point(183.5, 431), Point(233, 484))
H5_1=Rectangle(Point(233, 431), Point(282.5, 484))
H6_1=Rectangle(Point(282.5, 431), Point(332, 484))
H7_1=Rectangle(Point(332, 431), Point(381.5, 484))
H8_1=Rectangle(Point(381.5, 431), Point(431, 484))
H9_1=Rectangle(Point(431, 431), Point(480.5, 484))
H10_1=Rectangle(Point(480.5, 431), Point(530, 484))

#I
I1_1=Rectangle(Point(35, 484), Point(84.5, 537))
I2_1=Rectangle(Point(84.5, 484), Point(134, 537))
I3_1=Rectangle(Point(134, 484), Point(183.5, 537))
I4_1=Rectangle(Point(183.5, 484), Point(233, 537))
I5_1=Rectangle(Point(233, 484), Point(282.5, 537))
I6_1=Rectangle(Point(282.5, 484), Point(332, 537))
I7_1=Rectangle(Point(332, 484), Point(381.5, 537))
I8_1=Rectangle(Point(381.5, 484), Point(431, 537))
I9_1=Rectangle(Point(431, 484), Point(480.5, 537))
I10_1=Rectangle(Point(480.5, 484), Point(530, 537))

#J
J1_1=Rectangle(Point(35, 537), Point(84.5, 590))
J2_1=Rectangle(Point(84.5, 537), Point(134, 590))
J3_1=Rectangle(Point(134, 537), Point(183.5, 590))
J4_1=Rectangle(Point(183.5, 537), Point(233, 590))
J5_1=Rectangle(Point(233, 537), Point(282.5, 590))
J6_1=Rectangle(Point(282.5, 537), Point(332, 590))
J7_1=Rectangle(Point(332, 537), Point(381.5, 590))
J8_1=Rectangle(Point(381.5, 537), Point(431, 590))
J9_1=Rectangle(Point(431, 537), Point(480.5, 590))
J10_1=Rectangle(Point(480.5, 537), Point(530, 590))

###############################################################################

#Player1ATT
#Player1Board
#A
A1_1ATT=Rectangle(Point(590, 60), Point(639.5, 113))
A2_1ATT=Rectangle(Point(639.5, 60), Point(689, 113))
A3_1ATT=Rectangle(Point(689, 60), Point(738.5, 113))
A4_1ATT=Rectangle(Point(738.5, 60), Point(788, 113))
A5_1ATT=Rectangle(Point(788, 60), Point(837.5, 113))
A6_1ATT=Rectangle(Point(837.5, 60), Point(887, 113))
A7_1ATT=Rectangle(Point(887, 60), Point(936.5, 113))
A8_1ATT=Rectangle(Point(936.5, 60), Point(986, 113))
A9_1ATT=Rectangle(Point(986, 60), Point(1035.5, 113))
A10_1ATT=Rectangle(Point(1035.5, 60), Point(1085, 113))

#B
B1_1ATT= Rectangle(Point(590, 113), Point(639.5, 166))
B2_1ATT= Rectangle(Point(639.5, 113), Point(689, 166))
B3_1ATT= Rectangle(Point(689, 113), Point(738.5, 166))
B4_1ATT= Rectangle(Point(738.5, 113), Point(788, 166))
B5_1ATT= Rectangle(Point(788, 113), Point(837.5, 166))
B6_1ATT= Rectangle(Point(837.5, 113), Point(887, 166))
B7_1ATT= Rectangle(Point(887, 113), Point(936.5, 166))
B8_1ATT= Rectangle(Point(936.5, 113), Point(986, 166))
B9_1ATT= Rectangle(Point(986, 113), Point(1035.5, 166))
B10_1ATT= Rectangle(Point(1035.5, 113), Point(1085, 166))

#C
C1_1ATT= Rectangle(Point(590, 166), Point(639.5, 219))
C2_1ATT=Rectangle(Point(639.5, 166), Point(689, 219))
C3_1ATT=Rectangle(Point(689, 166), Point(738.5, 219))
C4_1ATT=Rectangle(Point(738.5, 166), Point(788, 219))
C5_1ATT=Rectangle(Point(788, 166), Point(837.5, 219))
C6_1ATT=Rectangle(Point(837.5, 166), Point(887, 219))
C7_1ATT=Rectangle(Point(887, 166), Point(936.5, 219))
C8_1ATT=Rectangle(Point(936.5, 166), Point(986, 219))
C9_1ATT=Rectangle(Point(986, 166), Point(1035.5, 219))
C10_1ATT=Rectangle(Point(1035.5, 166), Point(1085, 219))

#D
D1_1ATT=Rectangle(Point(590, 219), Point(639.5, 272))
D2_1ATT=Rectangle(Point(639.5, 219), Point(689, 272))
D3_1ATT=Rectangle(Point(689, 219), Point(738.5, 272))
D4_1ATT=Rectangle(Point(738.5, 219), Point(788, 272))
D5_1ATT=Rectangle(Point(788, 219), Point(837.5, 272))
D6_1ATT=Rectangle(Point(837.5, 219), Point(887, 272))
D7_1ATT=Rectangle(Point(887, 219), Point(936.5, 272))
D8_1ATT=Rectangle(Point(936.5, 219), Point(986, 272))
D9_1ATT=Rectangle(Point(986, 219), Point(1035.5, 272))
D10_1ATT=Rectangle(Point(1035.5, 219), Point(1085, 272))

#E
E1_1ATT=Rectangle(Point(590, 272), Point(639.5, 325))
E2_1ATT=Rectangle(Point(639.5, 272), Point(689, 325))
E3_1ATT=Rectangle(Point(689, 272), Point(738.5, 325))
E4_1ATT=Rectangle(Point(738.5, 272), Point(788, 325))
E5_1ATT=Rectangle(Point(788, 272), Point(837.5, 325))
E6_1ATT=Rectangle(Point(837.5, 272), Point(887, 325))
E7_1ATT=Rectangle(Point(887, 272), Point(936.5, 325))
E8_1ATT=Rectangle(Point(936.5, 272), Point(986, 325))
E9_1ATT=Rectangle(Point(986, 272), Point(1035.5, 325))
E10_1ATT=Rectangle(Point(1035.5, 272), Point(1085, 325))

#F
F1_1ATT=Rectangle(Point(590, 325), Point(639.5, 378))
F2_1ATT=Rectangle(Point(639.5, 325), Point(689, 378))
F3_1ATT=Rectangle(Point(689, 325), Point(738.5, 378))
F4_1ATT=Rectangle(Point(738.5, 325), Point(788, 378))
F5_1ATT=Rectangle(Point(788, 325), Point(837.5, 378))
F6_1ATT=Rectangle(Point(837.5, 325), Point(887, 378))
F7_1ATT=Rectangle(Point(887, 325), Point(936.5, 378))
F8_1ATT=Rectangle(Point(936.5, 325), Point(986, 378))
F9_1ATT=Rectangle(Point(986, 325), Point(1035.5, 378))
F10_1ATT=Rectangle(Point(1035.5, 325), Point(1085, 378))

#G
G1_1ATT=Rectangle(Point(590, 378), Point(639.5, 431))
G2_1ATT=Rectangle(Point(639.5, 378), Point(689, 431))
G3_1ATT=Rectangle(Point(689, 378), Point(738.5, 431))
G4_1ATT=Rectangle(Point(738.5, 378), Point(788, 431))
G5_1ATT=Rectangle(Point(788, 378), Point(837.5, 431))
G6_1ATT=Rectangle(Point(837.5, 378), Point(887, 431))
G7_1ATT=Rectangle(Point(887, 378), Point(936.5, 431))
G8_1ATT=Rectangle(Point(936.5, 378), Point(986, 431))
G9_1ATT=Rectangle(Point(986, 378), Point(1035.5, 431))
G10_1ATT=Rectangle(Point(1035.5, 378), Point(1085, 431))

#H
H1_1ATT=Rectangle(Point(590, 431), Point(639.5, 484))
H2_1ATT=Rectangle(Point(639.5, 431), Point(689, 484))
H3_1ATT=Rectangle(Point(689, 431), Point(738.5, 484))
H4_1ATT=Rectangle(Point(738.5, 431), Point(788, 484))
H5_1ATT=Rectangle(Point(788, 431), Point(837.5, 484))
H6_1ATT=Rectangle(Point(837.5, 431), Point(887, 484))
H7_1ATT=Rectangle(Point(887, 431), Point(936.5, 484))
H8_1ATT=Rectangle(Point(936.5, 431), Point(986, 484))
H9_1ATT=Rectangle(Point(986, 431), Point(1035.5, 484))
H10_1ATT=Rectangle(Point(1035.5, 431), Point(1085, 484))

#I
I1_1ATT=Rectangle(Point(590, 484), Point(639.5, 537))
I2_1ATT=Rectangle(Point(639.5, 484), Point(689, 537))
I3_1ATT=Rectangle(Point(689, 484), Point(738.5, 537))
I4_1ATT=Rectangle(Point(738.5, 484), Point(788, 537))
I5_1ATT=Rectangle(Point(788, 484), Point(837.5, 537))
I6_1ATT=Rectangle(Point(837.5, 484), Point(887, 537))
I7_1ATT=Rectangle(Point(887, 484), Point(936.5, 537))
I8_1ATT=Rectangle(Point(936.5, 484), Point(986, 537))
I9_1ATT=Rectangle(Point(986, 484), Point(1035.5, 537))
I10_1ATT=Rectangle(Point(1035.5, 484), Point(1085, 537))

#J
J1_1ATT=Rectangle(Point(590, 537), Point(639.5, 590))
J2_1ATT=Rectangle(Point(639.5, 537), Point(689, 590))
J3_1ATT=Rectangle(Point(689, 537), Point(738.5, 590))
J4_1ATT=Rectangle(Point(738.5, 537), Point(788, 590))
J5_1ATT=Rectangle(Point(788, 537), Point(837.5, 590))
J6_1ATT=Rectangle(Point(837.5, 537), Point(887, 590))
J7_1ATT=Rectangle(Point(887, 537), Point(936.5, 590))
J8_1ATT=Rectangle(Point(936.5, 537), Point(986, 590))
J9_1ATT=Rectangle(Point(986, 537), Point(1035.5, 590))
J10_1ATT=Rectangle(Point(1035.5, 537), Point(1085, 590))

###############################################################################

#Player2Board
#A
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

#B
B1_2= Rectangle(Point(35, 113), Point(84.5, 166))
B2_2= Rectangle(Point(84.5, 113), Point(134, 166))
B3_2= Rectangle(Point(134, 113), Point(183.5, 166))
B4_2= Rectangle(Point(183.5, 113), Point(233, 166))
B5_2= Rectangle(Point(233, 113), Point(282.5, 166))
B6_2= Rectangle(Point(282.5, 113), Point(332, 166))
B7_2= Rectangle(Point(332, 113), Point(381.5, 166))
B8_2= Rectangle(Point(381.5, 113), Point(431, 166))
B9_2= Rectangle(Point(431, 113), Point(480.5, 166))
B10_2= Rectangle(Point(480.5, 113), Point(530, 166))

#C
C1_2= Rectangle(Point(35, 166), Point(84.5, 219))
C2_2=Rectangle(Point(84.5, 166), Point(134, 219))
C3_2=Rectangle(Point(134, 166), Point(183.5, 219))
C4_2=Rectangle(Point(183.5, 166), Point(233, 219))
C5_2=Rectangle(Point(233, 166), Point(282.5, 219))
C6_2=Rectangle(Point(282.5, 166), Point(332, 219))
C7_2=Rectangle(Point(332, 166), Point(381.5, 219))
C8_2=Rectangle(Point(381.5, 166), Point(431, 219))
C9_2=Rectangle(Point(431, 166), Point(480.5, 219))
C10_2=Rectangle(Point(480.5, 166), Point(530, 219))

#D
D1_2=Rectangle(Point(35, 219), Point(84.5, 272))
D2_2=Rectangle(Point(84.5, 219), Point(134, 272))
D3_2=Rectangle(Point(134, 219), Point(183.5, 272))
D4_2=Rectangle(Point(183.5, 219), Point(233, 272))
D5_2=Rectangle(Point(233, 219), Point(282.5, 272))
D6_2=Rectangle(Point(282.5, 219), Point(332, 272))
D7_2=Rectangle(Point(332, 219), Point(381.5, 272))
D8_2=Rectangle(Point(381.5, 219), Point(431, 272))
D9_2=Rectangle(Point(431, 219), Point(480.5, 272))
D10_2=Rectangle(Point(480.5, 219), Point(530, 272))

#E
E1_2=Rectangle(Point(35, 272), Point(84.5, 325))
E2_2=Rectangle(Point(84.5, 272), Point(134, 325))
E3_2=Rectangle(Point(134, 272), Point(183.5, 325))
E4_2=Rectangle(Point(183.5, 272), Point(233, 325))
E5_2=Rectangle(Point(233, 272), Point(282.5, 325))
E6_2=Rectangle(Point(282.5, 272), Point(332, 325))
E7_2=Rectangle(Point(332, 272), Point(381.5, 325))
E8_2=Rectangle(Point(381.5, 272), Point(431, 325))
E9_2=Rectangle(Point(431, 272), Point(480.5, 325))
E10_2=Rectangle(Point(480.5, 272), Point(530, 325))

#F
F1_2=Rectangle(Point(35, 325), Point(84.5, 378))
F2_2=Rectangle(Point(84.5, 325), Point(134, 378))
F3_2=Rectangle(Point(134, 325), Point(183.5, 378))
F4_2=Rectangle(Point(183.5, 325), Point(233, 378))
F5_2=Rectangle(Point(233, 325), Point(282.5, 378))
F6_2=Rectangle(Point(282.5, 325), Point(332, 378))
F7_2=Rectangle(Point(332, 325), Point(381.5, 378))
F8_2=Rectangle(Point(381.5, 325), Point(431, 378))
F9_2=Rectangle(Point(431, 325), Point(480.5, 378))
F10_2=Rectangle(Point(480.5, 325), Point(530, 378))

#G
G1_2=Rectangle(Point(35, 378), Point(84.5, 431))
G2_2=Rectangle(Point(84.5, 378), Point(134, 431))
G3_2=Rectangle(Point(134, 378), Point(183.5, 431))
G4_2=Rectangle(Point(183.5, 378), Point(233, 431))
G5_2=Rectangle(Point(233, 378), Point(282.5, 431))
G6_2=Rectangle(Point(282.5, 378), Point(332, 431))
G7_2=Rectangle(Point(332, 378), Point(381.5, 431))
G8_2=Rectangle(Point(381.5, 378), Point(431, 431))
G9_2=Rectangle(Point(431, 378), Point(480.5, 431))
G10_2=Rectangle(Point(480.5, 378), Point(530, 431))

#H
H1_2=Rectangle(Point(35, 431), Point(84.5, 484))
H2_2=Rectangle(Point(84.5, 431), Point(134, 484))
H3_2=Rectangle(Point(134, 431), Point(183.5, 484))
H4_2=Rectangle(Point(183.5, 431), Point(233, 484))
H5_2=Rectangle(Point(233, 431), Point(282.5, 484))
H6_2=Rectangle(Point(282.5, 431), Point(332, 484))
H7_2=Rectangle(Point(332, 431), Point(381.5, 484))
H8_2=Rectangle(Point(381.5, 431), Point(431, 484))
H9_2=Rectangle(Point(431, 431), Point(480.5, 484))
H10_2=Rectangle(Point(480.5, 431), Point(530, 484))

#I
I1_2=Rectangle(Point(35, 484), Point(84.5, 537))
I2_2=Rectangle(Point(84.5, 484), Point(134, 537))
I3_2=Rectangle(Point(134, 484), Point(183.5, 537))
I4_2=Rectangle(Point(183.5, 484), Point(233, 537))
I5_2=Rectangle(Point(233, 484), Point(282.5, 537))
I6_2=Rectangle(Point(282.5, 484), Point(332, 537))
I7_2=Rectangle(Point(332, 484), Point(381.5, 537))
I8_2=Rectangle(Point(381.5, 484), Point(431, 537))
I9_2=Rectangle(Point(431, 484), Point(480.5, 537))
I10_2=Rectangle(Point(480.5, 484), Point(530, 537))

#J
J1_2=Rectangle(Point(35, 537), Point(84.5, 590))
J2_2=Rectangle(Point(84.5, 537), Point(134, 590))
J3_2=Rectangle(Point(134, 537), Point(183.5, 590))
J4_2=Rectangle(Point(183.5, 537), Point(233, 590))
J5_2=Rectangle(Point(233, 537), Point(282.5, 590))
J6_2=Rectangle(Point(282.5, 537), Point(332, 590))
J7_2=Rectangle(Point(332, 537), Point(381.5, 590))
J8_2=Rectangle(Point(381.5, 537), Point(431, 590))
J9_2=Rectangle(Point(431, 537), Point(480.5, 590))
J10_2=Rectangle(Point(480.5, 537), Point(530, 590))

##############################################################################

#Player2ATTBoard
#A
A1_2ATT=Rectangle(Point(590, 60), Point(639.5, 113))
A2_2ATT=Rectangle(Point(639.5, 60 ), Point(689, 113))
A3_2ATT=Rectangle(Point(689, 60), Point(738.5, 113))
A4_2ATT=Rectangle(Point(738.5, 60), Point(788, 113))
A5_2ATT=Rectangle(Point(788, 60), Point(837.5, 113))
A6_2ATT=Rectangle(Point(837.5, 60), Point(887, 113))
A7_2ATT=Rectangle(Point(887, 60), Point(936.5, 113))
A8_2ATT=Rectangle(Point(936.5, 60), Point(986, 113))
A9_2ATT=Rectangle(Point(986, 60), Point(1035.5, 113))
A10_2ATT=Rectangle(Point(1035.5, 60), Point(1085, 113))

#B
B1_2ATT= Rectangle(Point(590, 113), Point(639.5, 166))
B2_2ATT= Rectangle(Point(639.5, 113), Point(689, 166))
B3_2ATT= Rectangle(Point(689, 113), Point(738.5, 166))
B4_2ATT= Rectangle(Point(738.5, 113), Point(788, 166))
B5_2ATT= Rectangle(Point(788, 113), Point(837.5, 166))
B6_2ATT= Rectangle(Point(837.5, 113), Point(887, 166))
B7_2ATT= Rectangle(Point(887, 113), Point(936.5, 166))
B8_2ATT= Rectangle(Point(936.5, 113), Point(986, 166))
B9_2ATT= Rectangle(Point(986, 113), Point(1035.5, 166))
B10_2ATT= Rectangle(Point(1035.5, 113), Point(1085, 166))

#C
C1_2ATT= Rectangle(Point(590, 166), Point(639.5, 219))
C2_2ATT=Rectangle(Point(639.5, 166), Point(689, 219))
C3_2ATT=Rectangle(Point(689, 166), Point(738.5, 219))
C4_2ATT=Rectangle(Point(738.5, 166), Point(788, 219))
C5_2ATT=Rectangle(Point(788, 166), Point(837.5, 219))
C6_2ATT=Rectangle(Point(837.5, 166), Point(887, 219))
C7_2ATT=Rectangle(Point(887, 166), Point(936.5, 219))
C8_2ATT=Rectangle(Point(936.5, 166), Point(986, 219))
C9_2ATT=Rectangle(Point(986, 166), Point(1035.5, 219))
C10_2ATT=Rectangle(Point(1035.5, 166), Point(1085, 219))

#D
D1_2ATT=Rectangle(Point(590, 219), Point(639.5, 272))
D2_2ATT=Rectangle(Point(639.5, 219), Point(689, 272))
D3_2ATT=Rectangle(Point(689, 219), Point(738.5, 272))
D4_2ATT=Rectangle(Point(738.5, 219), Point(788, 272))
D5_2ATT=Rectangle(Point(788, 219), Point(837.5, 272))
D6_2ATT=Rectangle(Point(837.5, 219), Point(887, 272))
D7_2ATT=Rectangle(Point(887, 219), Point(936.5, 272))
D8_2ATT=Rectangle(Point(936.5, 219), Point(986, 272))
D9_2ATT=Rectangle(Point(986, 219), Point(1035.5, 272))
D10_2ATT=Rectangle(Point(1035.5, 219), Point(1085, 272))

#E
E1_2ATT=Rectangle(Point(590, 272), Point(639.5, 325))
E2_2ATT=Rectangle(Point(639.5, 272), Point(689, 325))
E3_2ATT=Rectangle(Point(689, 272), Point(738.5, 325))
E4_2ATT=Rectangle(Point(738.5, 272), Point(788, 325))
E5_2ATT=Rectangle(Point(788, 272), Point(837.5, 325))
E6_2ATT=Rectangle(Point(837.5, 272), Point(887, 325))
E7_2ATT=Rectangle(Point(887, 272), Point(936.5, 325))
E8_2ATT=Rectangle(Point(936.5, 272), Point(986, 325))
E9_2ATT=Rectangle(Point(986, 272), Point(1035.5, 325))
E10_2ATT=Rectangle(Point(1035.5, 272), Point(1085, 325))

#F
F1_2ATT=Rectangle(Point(590, 325), Point(639.5, 378))
F2_2ATT=Rectangle(Point(639.5, 325), Point(689, 378))
F3_2ATT=Rectangle(Point(689, 325), Point(738.5, 378))
F4_2ATT=Rectangle(Point(738.5, 325), Point(788, 378))
F5_2ATT=Rectangle(Point(788, 325), Point(837.5, 378))
F6_2ATT=Rectangle(Point(837.5, 325), Point(887, 378))
F7_2ATT=Rectangle(Point(887, 325), Point(936.5, 378))
F8_2ATT=Rectangle(Point(936.5, 325), Point(986, 378))
F9_2ATT=Rectangle(Point(986, 325), Point(1035.5, 378))
F10_2ATT=Rectangle(Point(1035.5, 325), Point(1085, 378))

#G
G1_2ATT=Rectangle(Point(590, 378), Point(639.5, 431))
G2_2ATT=Rectangle(Point(639.5, 378), Point(689, 431))
G3_2ATT=Rectangle(Point(689, 378), Point(738.5, 431))
G4_2ATT=Rectangle(Point(738.5, 378), Point(788, 431))
G5_2ATT=Rectangle(Point(788, 378), Point(837.5, 431))
G6_2ATT=Rectangle(Point(837.5, 378), Point(887, 431))
G7_2ATT=Rectangle(Point(887, 378), Point(936.5, 431))
G8_2ATT=Rectangle(Point(936.5, 378), Point(986, 431))
G9_2ATT=Rectangle(Point(986, 378), Point(1035.5, 431))
G10_2ATT=Rectangle(Point(1035.5, 378), Point(1085, 431))

#H
H1_2ATT=Rectangle(Point(590, 431), Point(639.5, 484))
H2_2ATT=Rectangle(Point(639.5, 431), Point(689, 484))
H3_2ATT=Rectangle(Point(689, 431), Point(738.5, 484))
H4_2ATT=Rectangle(Point(738.5, 431), Point(788, 484))
H5_2ATT=Rectangle(Point(788, 431), Point(837.5, 484))
H6_2ATT=Rectangle(Point(837.5, 431), Point(887, 484))
H7_2ATT=Rectangle(Point(887, 431), Point(936.5, 484))
H8_2ATT=Rectangle(Point(936.5, 431), Point(986, 484))
H9_2ATT=Rectangle(Point(986, 431), Point(1035.5, 484))
H10_2ATT=Rectangle(Point(1035.5, 431), Point(1085, 484))

#I
I1_2ATT=Rectangle(Point(590, 484), Point(639.5, 537))
I2_2ATT=Rectangle(Point(639.5, 484), Point(689, 537))
I3_2ATT=Rectangle(Point(689, 484), Point(738.5, 537))
I4_2ATT=Rectangle(Point(738.5, 484), Point(788, 537))
I5_2ATT=Rectangle(Point(788, 484), Point(837.5, 537))
I6_2ATT=Rectangle(Point(837.5, 484), Point(887, 537))
I7_2ATT=Rectangle(Point(887, 484), Point(936.5, 537))
I8_2ATT=Rectangle(Point(936.5, 484), Point(986, 537))
I9_2ATT=Rectangle(Point(986, 484), Point(1035.5, 537))
I10_2ATT=Rectangle(Point(1035.5, 484), Point(1085, 537))

#J
J1_2ATT=Rectangle(Point(590, 537), Point(639.5, 590))
J2_2ATT=Rectangle(Point(639.5, 537), Point(689, 590))
J3_2ATT=Rectangle(Point(689, 537), Point(738.5, 590))
J4_2ATT=Rectangle(Point(738.5, 537), Point(788, 590))
J5_2ATT=Rectangle(Point(788, 537), Point(837.5, 590))
J6_2ATT=Rectangle(Point(837.5, 537), Point(887, 590))
J7_2ATT=Rectangle(Point(887, 537), Point(936.5, 590))
J8_2ATT=Rectangle(Point(936.5, 537), Point(986, 590))
J9_2ATT=Rectangle(Point(986, 537), Point(1035.5, 590))
J10_2ATT=Rectangle(Point(1035.5, 537), Point(1085, 590))

################################################################################################

#LooperVars
Astr=("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10")
Bstr=("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10")
Cstr=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10")
Dstr=("D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10")
Estr=("E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10")
Fstr= ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10")
Gstr= ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10")
Hstr= ("H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10")
Istr= ("I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10")
Jstr= ("J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10")

#BoxesP1
BoxesP1A=(A1_1, A2_1, A3_1, A4_1, A5_1, A6_1, A7_1, A8_1, A9_1, A10_1)
BoxesP1B=(B1_1, B2_1, B3_1, B4_1, B5_1, B6_1, B7_1, B8_1, B9_1, B10_1)
BoxesP1C=(C1_1, C2_1, C3_1, C4_1, C5_1, C6_1, C7_1, C8_1, C9_1, C10_1)
BoxesP1D=(D1_1, D2_1, D3_1, D4_1, D5_1, D6_1, D7_1, D8_1, D9_1, D10_1)
BoxesP1E=(E1_1, E2_1, E3_1, E4_1, E5_1, E6_1, E7_1, E8_1, E9_1, E10_1)
BoxesP1F=(F1_1, F2_1, F3_1, F4_1, F5_1, F6_1, F7_1, F8_1, F9_1, F10_1)
BoxesP1G=(G1_1, G2_1, G3_1, G4_1, G5_1, G6_1, G7_1, G8_1, G9_1, G10_1)
BoxesP1H=(H1_1, H2_1, H3_1, H4_1, H5_1, H6_1, H7_1, H8_1, H9_1, H10_1)
BoxesP1I=(I1_1, I2_1, I3_1, I4_1, I5_1, I6_1, I7_1, I8_1, I9_1, I10_1)
BoxesP1J=(J1_1, J2_1, J3_1, J4_1, J5_1, J6_1, J7_1, J8_1, J9_1, J10_1)

BoxesP1ATT_A= (A1_1ATT, A2_1ATT, A3_1ATT, A4_1ATT, A5_1ATT, A6_1ATT, A7_1ATT,
               A8_1ATT, A9_1ATT, A10_1ATT)
BoxesP1ATT_B= (B1_1ATT, B2_1ATT, B3_1ATT, B4_1ATT, B5_1ATT, B6_1ATT, B7_1ATT,
               B8_1ATT, B9_1ATT, B10_1ATT)
BoxesP1ATT_C= (C1_1ATT, C2_1ATT, C3_1ATT, C4_1ATT, C5_1ATT, C6_1ATT, C7_1ATT,
               C8_1ATT, C9_1ATT, C10_1ATT)
BoxesP1ATT_D= (D1_1ATT, D2_1ATT, D3_1ATT, D4_1ATT, D5_1ATT, D6_1ATT, D7_1ATT,
               D8_1ATT, D9_1ATT, D10_1ATT)
BoxesP1ATT_E= (E1_1ATT, E2_1ATT, E3_1ATT, E4_1ATT, E5_1ATT, E6_1ATT, E7_1ATT,
               E8_1ATT, E9_1ATT, E10_1ATT)
BoxesP1ATT_F= (F1_1ATT, F2_1ATT, F3_1ATT, F4_1ATT, F5_1ATT, F6_1ATT, F7_1ATT,
               F8_1ATT, F9_1ATT, F10_1ATT)
BoxesP1ATT_G= (G1_1ATT, G2_1ATT, G3_1ATT, G4_1ATT, G5_1ATT, G6_1ATT, G7_1ATT,
               G8_1ATT, G9_1ATT, G10_1ATT)
BoxesP1ATT_H= (H1_1ATT, H2_1ATT, H3_1ATT, H4_1ATT, H5_1ATT, H6_1ATT, H7_1ATT,
               H8_1ATT, H9_1ATT, H10_1ATT)
BoxesP1ATT_I= (I1_1ATT, I2_1ATT, I3_1ATT, I4_1ATT, I5_1ATT, I6_1ATT, I7_1ATT,
               I8_1ATT, I9_1ATT, I10_1ATT)
BoxesP1ATT_J= (J1_1ATT, J2_1ATT, J3_1ATT, J4_1ATT, J5_1ATT, J6_1ATT, J7_1ATT,
               J8_1ATT, J9_1ATT, J10_1ATT)

#BoxesP2
BoxesP2A=(A1_2, A2_2, A3_2, A4_2, A5_2, A6_2, A7_2, A8_2, A9_2, A10_2)
BoxesP2B=(B1_2, B2_2, B3_2, B4_2, B5_2, B6_2, B7_2, B8_2, B9_2, B10_2)
BoxesP2C=(C1_2, C2_2, C3_2, C4_2, C5_2, C6_2, C7_2, C8_2, C9_2, C10_2)
BoxesP2D=(D1_2, D2_2, D3_2, D4_2, D5_2, D6_2, D7_2, D8_2, D9_2, D10_2)
BoxesP2E=(E1_2, E2_2, E3_2, E4_2, E5_2, E6_2, E7_2, E8_2, E9_2, E10_2)
BoxesP2F=(F1_2, F2_2, F3_2, F4_2, F5_2, F6_2, F7_2, F8_2, F9_2, F10_2)
BoxesP2G=(G1_2, G2_2, G3_2, G4_2, G5_2, G6_2, G7_2, G8_2, G9_2, G10_2)
BoxesP2H=(H1_2, H2_2, H3_2, H4_2, H5_2, H6_2, H7_2, H8_2, H9_2, H10_2)
BoxesP2I=(I1_2, I2_2, I3_2, I4_2, I5_2, I6_2, I7_2, I8_2, I9_2, I10_2)
BoxesP2J=(J1_2, J2_2, J3_2, J4_2, J5_2, J6_2, J7_2, J8_2, J9_2, J10_2)

BoxesP2ATT_A= (A1_2ATT, A2_2ATT, A3_2ATT, A4_2ATT, A5_2ATT, A6_2ATT, A7_2ATT,
               A8_2ATT, A9_2ATT, A10_2ATT)
BoxesP2ATT_B= (B1_2ATT, B2_2ATT, B3_2ATT, B4_2ATT, B5_2ATT, B6_2ATT, B7_2ATT,
               B8_2ATT, B9_2ATT, B10_2ATT)
BoxesP2ATT_C= (C1_2ATT, C2_2ATT, C3_2ATT, C4_2ATT, C5_2ATT, C6_2ATT, C7_2ATT,
               C8_2ATT, C9_2ATT, C10_2ATT)
BoxesP2ATT_D= (D1_2ATT, D2_2ATT, D3_2ATT, D4_2ATT, D5_2ATT, D6_2ATT, D7_2ATT,
               D8_2ATT, D9_2ATT, D10_2ATT)
BoxesP2ATT_E= (E1_2ATT, E2_2ATT, E3_2ATT, E4_2ATT, E5_2ATT, E6_2ATT, E7_2ATT,
               E8_2ATT, E9_2ATT, E10_2ATT)
BoxesP2ATT_F= (F1_2ATT, F2_2ATT, F3_2ATT, F4_2ATT, F5_2ATT, F6_2ATT, F7_2ATT,
               F8_2ATT, F9_2ATT, F10_2ATT)
BoxesP2ATT_G= (G1_2ATT, G2_2ATT, G3_2ATT, G4_2ATT, G5_2ATT, G6_2ATT, G7_2ATT,
               G8_2ATT, G9_2ATT, G10_2ATT)
BoxesP2ATT_H= (H1_2ATT, H2_2ATT, H3_2ATT, H4_2ATT, H5_2ATT, H6_2ATT, H7_2ATT,
               H8_2ATT, H9_2ATT, H10_2ATT)
BoxesP2ATT_I= (I1_2ATT, I2_2ATT, I3_2ATT, I4_2ATT, I5_2ATT, I6_2ATT, I7_2ATT,
               I8_2ATT, I9_2ATT, I10_2ATT)
BoxesP2ATT_J= (J1_2ATT, J2_2ATT, J3_2ATT, J4_2ATT, J5_2ATT, J6_2ATT, J7_2ATT,
               J8_2ATT, J9_2ATT, J10_2ATT)

#Numbers and Letters
nums=(one, two, three, four, five, six, seven, eight, nine, ten, oth_one,
      oth_two, oth_three, oth_four, oth_five, oth_six, oth_seven, oth_eight,
      oth_nine, oth_ten)
text=(A_text, B_text, C_text, D_text, E_text, F_text, G_text, H_text, I_text,
      J_text, oth_A, oth_B, oth_C, oth_D, oth_E, oth_F, oth_G, oth_H, oth_I,
      oth_J)

#Player1Loc
Player1_Locations=[]
P1confirmlist=[]
P1BoxLoc=[]
P1BoxConf=[]
P1att=[]
P1hit=[]
P1miss=[]
P1x=[]
P1y=[]

#Player2Loc
Player2_Locations=[]
P2confirmlist=[]
P2BoxLoc=[]
P2BoxConf=[]
P2att=[]
P2hit=[]
P2miss=[]
P2x=[]
P2y=[]

#Ships
Bship1=[]
Aircraft1=[]
Pat1=[]
Sub1=[]
Frig1=[]

Bship2=[]
Aircraft2=[]
Pat2=[]
Sub2=[]
Frig2=[]

#ShipLists
shipsP1=["Aircraft Carrier"]
''',"Battleship ,"Submarine", "Frigate", "Patrol Boat"]'''
shipsP2=["Aircraft Carrier"]
''', "Battleship","Submarine", "Frigate", "Patrol Boat"]'''


#Listvars
xvar=-1
yvar=-1
liststart=-1
boxvar=-1
brun=-1
rightvar=-1
leftvar=-1
xval=0

#badlist
badlist=[]
