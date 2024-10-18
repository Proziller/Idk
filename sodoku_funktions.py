import random
import tkinter as tk

def paint(target):
    flr1 = tk.Label(text="     ")
    flr2 = tk.Label(text="     ")
    flr3 = tk.Label(text=" ")
    flr4 = tk.Label(text=" ")
    l = 0
    for u in range(3):
        for i in range(3):
            for o in range(3):
                for p in range(3):
                    target[l].grid(row=i+u+(u*3), column=(o*3)+p+o)
                    l += 1
                
                if o == 0:
                    flr1.grid(row=i+u+(u*3), column=3)
                elif o == 1:
                    flr2.grid(row=i+u+(u*3), column=7)
        if u == 0:
            flr3.grid(row=3, column=0)
        elif u == 1:
            flr4.grid(row=7, column=0)

def generate(xymap,):
    retry = True
    while retry == True:
        retry = False

        xymap.clear()
        for i in range(9):
            xymap.append([["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]])

        columns = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
        boxes = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
        box = 0

        for pos1 in range(9):

            Vnums = [1,2,3,4,5,6,7,8,9]

            for pos2 in range(9):
                if pos1 <=2 and pos2 <=2:
                    box = 0
                elif pos1 <=2 and pos2 <=5:
                    box = 1
                elif pos1 <=2 and pos2 <=8:
                    box = 2
                elif pos1 <=5 and pos2 <=2:
                    box = 3
                elif pos1 <=5 and pos2 <=5:
                    box = 4
                elif pos1 <=5 and pos2 <=8:
                    box = 5
                elif pos1 <=8 and pos2 <=2:
                    box = 6
                elif pos1 <=8 and pos2 <=5:
                    box = 7
                elif pos1 <=8 and pos2 <=8:
                    box = 8

                if retry != True:

                    q = 0
                    possibilities =[]
                    for i in range(len(columns[pos2])):
                        if columns[pos2][i] in Vnums and columns[pos2][i] in boxes[box]:
                            q += 1
                            possibilities.append(columns[pos2][i])
                    if q > 0:
                        
                        randnum = random.choice(possibilities)

                        while randnum not in Vnums or randnum not in columns[pos2]:
                            randnum = random.choice(possibilities)

                        boxes[box].remove(randnum)
                        columns[pos2].remove(randnum)
                        Vnums.remove(randnum)

                        xymap[pos1][pos2][0] = randnum
                    else:
                        retry = True