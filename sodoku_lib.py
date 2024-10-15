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

            for pos1 in range(9):

                Vnums = [1,2,3,4,5,6,7,8,9,"□"]

                for pos2 in range(9):

                    if retry != True:

                        Hcounter = 0
                        Hnums = [1,2,3,4,5,6,7,8,9,"□"]

                        while pos1-Hcounter > 0:
                            checkpos1 = pos1-Hcounter
                            Hnums.remove(self.xymap[checkpos1][pos2][0])
                            Hcounter += 1

                        randnum = random.randint(1,9)

                        q = 0
                        for i in range(len(Hnums)):
                            if Hnums[i] in Vnums:
                                q += 1

                        if q > 0:

                            while randnum not in Vnums or randnum not in Hnums:
                                randnum = random.randint(1,9)

                            Hnums.remove(randnum)
                            Vnums.remove(randnum)

                            self.xymap[pos1][pos2][0] = randnum
                        else:
                            retry = True
            
            print("")
            print("=========================")
            
            Vcounter = 0

            for qpos1 in range(9):

                print("")

                if Vcounter == 3:
                    Vcounter = 0
                    print("------+-------+------")

                Vcounter += 1

                qHcounter = 0
                for qpos2 in range(9):

                    if qHcounter == 3:
                        qHcounter = 0
                        print("|","", end = "")

                    print(self.xymap[qpos1][qpos2][0],"", end = "")

                    qHcounter += 1

    #=============================================================================================================================