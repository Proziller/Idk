import random
import tkinter as tk

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

        self.playfield = tk.Tk()

        self.difficulty = int(difficulty)

        self.mistakes = 0

        self.right = self.difficulty

        self.map =[]
        self.entries = []
        self.correct = []

        self.chooser = tk.Label(self.playfield, text=0)
        self.chooser.grid(row= 13, column=10)

        self.num = 0

    #=============================================================================================================================

    def set_num(self,number):
        self.chooser.config(text=number)
        self.num = number
        print(number)
        
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
                self.map.append(self.playmap[i][o][0])
                self.correct.append(self.xymap[i][o][0])

                if self.playmap[i][o][1] == True:
                    self.entries[i*9+o] = tk.Button(self.playfield, text=self.playmap[i][o][0])
                    
                else:
                    self.entries[i*9+o] = tk.Label(self.playfield, text=self.playmap[i][o][0])


    #=============================================================================================================================
    
    def aktion(self,number):
        self.map[number] = self.num
        if self.map[number] == self.correct[number]:
           self.entries[number].config(text = self.correct[number])
    
    #=============================================================================================================================

    def play(self):

        filler = tk.Label(self.playfield, text="")
        filler1 = tk.Label(self.playfield, text="")
        filler2 = tk.Label(self.playfield, text="")

        for i in range(3):
            for o in range(3):
                self.entries[i*3+o].grid(row=o, column=i)
                self.entries[i*3+o].config(command=self.aktion(i*9+o))
        filler.grid(row=0, column=3)

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+9].grid(row=o, column=i+4)
                self.entries[(i*3+o)+9].config(command=self.aktion(i*9+o))
        filler.grid(row=0, column=7)

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+18].grid(row=o, column=i+8)
                self.entries[(i*3+o)+18].config(command=self.aktion(i*9+o))
        filler1.grid(row=3, column=0)

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+27].grid(row=o+4, column=i)
                self.entries[(i*3+o)+27].config(command=self.aktion(i*9+o))

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+36].grid(row=o+4, column=i+4)
                self.entries[(i*3+o)+36].config(command=self.aktion(i*9+o))

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+45].grid(row=o+4, column=i+8)
                self.entries[(i*3+o)+45].config(command=self.aktion(i*9+o))
        filler2.grid(row=7, column=0)

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+54].grid(row=o+8, column=i)
                self.entries[(i*3+o)+54].config(command=self.aktion(i*9+o))

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+63].grid(row=o+8, column=i+4)
                self.entries[(i*3+o)+63].config(command=self.aktion(i*9+o))

        for i in range(3):
            for o in range(3):
                self.entries[(i*3+o)+72].grid(row=o+8, column=i+8)
                self.entries[(i*3+o)+72].config(command=self.aktion(i*9+o))

        self.playfield.bind("1",self.set_num(1))
        self.playfield.bind("2",self.set_num(2))
        self.playfield.bind("3",self.set_num(3))
        self.playfield.bind("4",self.set_num(4))
        self.playfield.bind("5",self.set_num(5))
        self.playfield.bind("6",self.set_num(6))
        self.playfield.bind("7",self.set_num(7))
        self.playfield.bind("8",self.set_num(8))
        self.playfield.bind("9",self.set_num(9))

        self.playfield.mainloop()