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

        self.playmap = []

        self.difficulty = int(difficulty)
        
    #=============================================================================================================================

    def print_map(self):
        print(self.playmap[6][6][0],self.playmap[6][7][0],self.playmap[6][8][0],"|",self.playmap[7][6][0],self.playmap[7][7][0],self.playmap[7][8][0],"|",self.playmap[8][6][0],self.playmap[8][7][0],self.playmap[8][8][0])
        print(self.playmap[6][3][0],self.playmap[6][4][0],self.playmap[6][5][0],"|",self.playmap[7][3][0],self.playmap[7][4][0],self.playmap[7][5][0],"|",self.playmap[8][3][0],self.playmap[8][4][0],self.playmap[8][5][0])
        print(self.playmap[6][0][0],self.playmap[6][1][0],self.playmap[6][2][0],"|",self.playmap[7][0][0],self.playmap[7][1][0],self.playmap[7][2][0],"|",self.playmap[8][0][0],self.playmap[8][1][0],self.playmap[8][2][0])
        print("------+-------+-------")
        print(self.playmap[3][6][0],self.playmap[3][7][0],self.playmap[3][8][0],"|",self.playmap[4][6][0],self.playmap[4][7][0],self.playmap[4][8][0],"|",self.playmap[5][6][0],self.playmap[5][7][0],self.playmap[5][8][0])
        print(self.playmap[3][3][0],self.playmap[3][4][0],self.playmap[3][5][0],"|",self.playmap[4][3][0],self.playmap[4][4][0],self.playmap[4][5][0],"|",self.playmap[5][3][0],self.playmap[5][4][0],self.playmap[5][5][0])
        print(self.playmap[3][0][0],self.playmap[3][1][0],self.playmap[3][2][0],"|",self.playmap[4][0][0],self.playmap[4][1][0],self.playmap[4][2][0],"|",self.playmap[5][0][0],self.playmap[5][1][0],self.playmap[5][2][0])
        print("------+-------+-------")
        print(self.playmap[0][6][0],self.playmap[0][7][0],self.playmap[0][8][0],"|",self.playmap[1][6][0],self.playmap[1][7][0],self.playmap[1][8][0],"|",self.playmap[2][6][0],self.playmap[2][7][0],self.playmap[2][8][0])
        print(self.playmap[0][3][0],self.playmap[0][4][0],self.playmap[0][5][0],"|",self.playmap[1][3][0],self.playmap[1][4][0],self.playmap[1][5][0],"|",self.playmap[2][3][0],self.playmap[2][4][0],self.playmap[2][5][0])
        print(self.playmap[0][0][0],self.playmap[0][1][0],self.playmap[0][2][0],"|",self.playmap[1][0][0],self.playmap[1][1][0],self.playmap[1][2][0],"|",self.playmap[2][0][0],self.playmap[2][1][0],self.playmap[2][2][0])

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
        
        self.playmap = [
            [self.xymap[8][0],self.xymap[8][1],self.xymap[8][2],self.xymap[7][0],self.xymap[7][1],self.xymap[7][2],self.xymap[6][0],self.xymap[6][1],self.xymap[6][2]],
            [self.xymap[8][3],self.xymap[8][4],self.xymap[8][5],self.xymap[7][3],self.xymap[7][4],self.xymap[7][5],self.xymap[6][3],self.xymap[6][4],self.xymap[6][5]],
            [self.xymap[8][6],self.xymap[8][7],self.xymap[8][8],self.xymap[7][6],self.xymap[7][7],self.xymap[7][8],self.xymap[6][6],self.xymap[6][7],self.xymap[6][8]],
            [self.xymap[5][0],self.xymap[5][1],self.xymap[5][2],self.xymap[4][0],self.xymap[4][1],self.xymap[4][2],self.xymap[3][0],self.xymap[3][1],self.xymap[3][2]],
            [self.xymap[5][3],self.xymap[5][4],self.xymap[5][5],self.xymap[4][3],self.xymap[4][4],self.xymap[4][5],self.xymap[3][3],self.xymap[3][4],self.xymap[3][5]],
            [self.xymap[5][6],self.xymap[5][7],self.xymap[5][8],self.xymap[4][6],self.xymap[4][7],self.xymap[4][8],self.xymap[3][6],self.xymap[3][7],self.xymap[3][8]],
            [self.xymap[2][0],self.xymap[2][1],self.xymap[2][2],self.xymap[1][0],self.xymap[1][1],self.xymap[1][2],self.xymap[0][0],self.xymap[0][1],self.xymap[0][2]],
            [self.xymap[2][3],self.xymap[2][4],self.xymap[2][5],self.xymap[1][3],self.xymap[1][4],self.xymap[1][5],self.xymap[0][3],self.xymap[0][4],self.xymap[0][5]],
            [self.xymap[2][6],self.xymap[2][7],self.xymap[2][8],self.xymap[1][6],self.xymap[1][7],self.xymap[1][8],self.xymap[0][6],self.xymap[0][7],self.xymap[0][8]],
        ]
        self.xymap = self.playmap
        for i in range(81-self.difficulty):

            pos1 = random.randint(0,8)
            pos2 = random.randint(0,8)

            while self.playmap[pos1][pos2][0] == "□":
                pos1 = random.randint(0,8)
                pos2 = random.randint(0,8)

            self.playmap[pos1][pos2] = ["□",True]

    #=============================================================================================================================

    def mark(self):
        valnum = ["1","2","3","4","5","6","7","8","9"]

        pos1 = input("pos1:")
        if pos1 in valnum:
            pos2 = input("pos2:")
            if pos2 in valnum:
                num = input("num:")
                if num in valnum:
                    if self.playmap[int(pos1)-1][int(pos2)-1][1] == True:
                        self.playmap[int(pos1)-1][int(pos2)-1][0] = num
                        print(self.playmap[int(pos1)-1][int(pos2)-1][0])
                    else:
                        print("invalide position")
                else:
                    print("invalid num")
            else:
                print("invalid pos2")
        else:
            print("invalid pos1")