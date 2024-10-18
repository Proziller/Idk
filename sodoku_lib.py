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

        self.scheissdraufaufdiesekackeichhabkeinbockmehrdrauf =[]
        self.entries = []
        self.correct = []

        self.chooser = tk.Label(playfield, text=0)
        self.chooser.grid(row= 13, column=10)

        self.num = 0

        self.bt1 = tk.Button(playfield, text=1)
        self.bt2 = tk.Button(playfield, text=2)
        self.bt3 = tk.Button(playfield, text=3)
        self.bt4 = tk.Button(playfield, text=4)
        self.bt5 = tk.Button(playfield, text=5)
        self.bt6 = tk.Button(playfield, text=6)
        self.bt7 = tk.Button(playfield, text=7)
        self.bt8 = tk.Button(playfield, text=8)
        self.bt9 = tk.Button(playfield, text=9)
        self.bt1.grid(row=13, column=0)
        self.bt2.grid(row=13, column=1)
        self.bt3.grid(row=13, column=2)
        self.bt4.grid(row=13, column=3)
        self.bt5.grid(row=13, column=4)
        self.bt6.grid(row=13, column=5)
        self.bt7.grid(row=13, column=6)
        self.bt8.grid(row=13, column=7)
        self.bt9.grid(row=13, column=8)
        
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
                self.scheissdraufaufdiesekackeichhabkeinbockmehrdrauf.append(self.playmap[i][o][0])
                self.correct.append(self.xymap[i][o][0])

                if self.playmap[i][o][1] == True:
                    self.entries[i*9+o] = tk.Button(playfield, text=self.playmap[i][o][0])
                    
                else:
                    self.entries[i*9+o] = tk.Label(playfield, text=self.playmap[i][o][0])

    #=============================================================================================================================


    def set_num(self,num):
        self.chooser.config(text=num)
        self.num = num
        print(num)

    #=============================================================================================================================
    
    def aktion(self,number):
        self.scheissdraufaufdiesekackeichhabkeinbockmehrdrauf[number] = self.num
        if self.scheissdraufaufdiesekackeichhabkeinbockmehrdrauf[number] == self.correct[number]:
           self.entries[number].config(text = self.correct[number])
    
    #=============================================================================================================================

    def play(self):


        filler = tk.Label(playfield, text="")
        filler1 = tk.Label(playfield, text="")
        filler2 = tk.Label(playfield, text="")

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
        filler.grid(row=12,column=0)

        self.bt1.config(command=self.set_num(1))
        self.bt2.config(command=self.set_num(2))
        self.bt3.config(command=self.set_num(3))
        self.bt4.config(command=self.set_num(4))
        self.bt5.config(command=self.set_num(5))
        self.bt6.config(command=self.set_num(6))
        self.bt7.config(command=self.set_num(7))
        self.bt8.config(command=self.set_num(8))
        self.bt9.config(command=self.set_num(9))
        
        playfield.mainloop()