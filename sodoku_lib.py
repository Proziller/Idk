import random

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

        self.difficulty = int(difficulty)
        
    #=============================================================================================================================

    def print_map(self):

        Vcounter = 0

        for pos1 in range(9):

            print("")

            if Vcounter == 3:
                Vcounter = 0
                print("------+-------+------")

            Vcounter += 1

            Hcounter = 0
            for pos2 in range(9):

                if Hcounter == 3:
                    Hcounter = 0
                    print("|","", end = "")

                print(self.xymap[pos1][pos2][0],"", end = "")

                Hcounter += 1
            

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

    #=============================================================================================================================