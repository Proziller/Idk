import random
import tkinter as tk
import sodoku_funktions as sf

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
    
    def aktion(self,number):
        self.map[number] = self.num
        if self.map[number] == self.correct[number]:
           self.entries[number].config(text = self.correct[number])

    #=============================================================================================================================

    def set_num(self,number):
        self.chooser.config(text=number)
        self.num = number
        print("aa")
        
    #=============================================================================================================================

    def generate(self):
        
        sf.generate(self.xymap)
        
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
                    self.entries[i*9+o] = tk.Button(self.playfield, text=self.playmap[i][o][0], command=self.aktion(i*9+o))
                    
                else:
                    self.entries[i*9+o] = tk.Label(self.playfield, text=self.playmap[i][o][0])
    
    #=============================================================================================================================

    def play(self):

        sf.paint(self.entries)

        for i in range(9):
            self.playfield.bind(str(i+1),self.set_num(i+1))


    def rplay(self):
        self.playfield.mainloop()