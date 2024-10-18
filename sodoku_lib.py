import random
import tkinter as tk

playfield = tk.Tk()

class SoMap():

    def __init__(self, difficulty):
        self.xymap = [
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
        [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]]
        ]

        self.playmap = []

        self.difficulty = int(difficulty)

        self.mistakes = 0

        self.right = self.difficulty

        self.entries = []

        self.num = 0
        
    #=============================================================================================================================
    
    def set_num(self,num):
        self.num = num

    #=============================================================================================================================
    
    def aktion(self):
        pass
    
    #=============================================================================================================================

    def print_map(self):
        for i in range(9):
            for o in range(9):
                self.entries[i*9+o].grid(row=o, column=i)

        bt1 = tk.Button(playfield, text=1, command=self.set_num(1))
        bt2 = tk.Button(playfield, text=2, command=self.set_num(2))
        bt3 = tk.Button(playfield, text=3, command=self.set_num(3))
        bt4 = tk.Button(playfield, text=4, command=self.set_num(4))
        bt5 = tk.Button(playfield, text=5, command=self.set_num(5))
        bt6 = tk.Button(playfield, text=6, command=self.set_num(6))
        bt7 = tk.Button(playfield, text=7, command=self.set_num(7))
        bt8 = tk.Button(playfield, text=8, command=self.set_num(8))
        bt9 = tk.Button(playfield, text=9, command=self.set_num(9))
        bt1.grid(row=9, column=1)
        bt2.grid(row=9, column=2)
        bt3.grid(row=9, column=3)
        bt4.grid(row=9, column=4)
        bt5.grid(row=9, column=5)
        bt6.grid(row=9, column=6)
        bt7.grid(row=9, column=7)
        bt8.grid(row=9, column=8)
        bt9.grid(row=9, column=9)

        playfield.mainloop()

    #=============================================================================================================================

    def generate(self):
        retry = True
        while retry == True:

            retry = False

            self.xymap.clear()
            for i in range(9):
                self.xymap.append([["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]])

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

                            self.xymap[pos1][pos2][0] = randnum
                        else:
                            retry = True
        
        self.playmap = self.xymap

        self.xymap = self.playmap
        for i in range(81-self.difficulty):

            pos1 = random.randint(0,8)
            pos2 = random.randint(0,8)

            while self.playmap[pos1][pos2][0] == "□":
                pos1 = random.randint(0,8)
                pos2 = random.randint(0,8)

            self.playmap[pos1][pos2] = ["□",True]
    
        for i in range(9):
            for o in range(9):
                self.entries.append(self.playmap[i][o][0])
                self.correct.append(self.playmap[i][o][0])
                if self.playmap[i][o][1] == True:
                    self.entries[i*9+o] = tk.Button(playfield, text=self.playmap[i][o][0], command=self.aktion())
                else:
                    self.entries[i*9+o] = tk.Label(playfield, text=self.playmap[i][o][0])