from zellegraphics import *

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

#LooperVars
Astr=("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10")
Bstr=("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10")
Cstr=("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10")
Dstr=("D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10")
Estr=("E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10")
Fstr= ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10")

#BoxesP1
BoxesP1A=(A1_1, A2_1, A3_1, A4_1, A5_1, A6_1, A7_1, A8_1, A9_1, A10_1)
BoxesP1B=(B1_1, B2_1, B3_1, B4_1, B5_1, B6_1, B7_1, B8_1, B9_1, B10_1)
BoxesP1C=(C1_1, C2_1, C3_1, C4_1, C5_1, C6_1, C7_1, C8_1, C9_1, C10_1)
BoxesP1D=(D1_1, D2_1, D3_1, D4_1, D5_1, D6_1, D7_1, D8_1, D9_1, D10_1)
BoxesP1E=(E1_1, E2_1, E3_1, E4_1, E5_1, E6_1, E7_1, E8_1, E9_1, E10_1)
BoxesP1F=(F1_1, F2_1, F3_1, F4_1, F5_1, F6_1, F7_1, F8_1, F9_1, F10_1)

#BoxesP2
BoxesP2=[]

#Player1Loc
Player1_Locations=[]

#Player2Loc
Player2_Locations=[]

#P1conf
P1confirmlist=[]

#P2conf
P2confirmlist=[]
