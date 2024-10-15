import random

class SoMap():

    def __init__(self, difficulty):
        self.xymap = [
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
        [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]]
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
            print("BOOSH")
            retry = False

            self.xymap = [
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]],
            [["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False],["",False]]
            ]
        
            nums = [1,2,3,4,5,6,7,8,9]
            for pos1 in range(9):
                Vcheck = []
                for pos2 in range(9):

                    Hcounter = 0
                    Hcheck = []

                    while pos1-Hcounter >= 0:
                        checkpos1 = pos1-Hcounter
                        Hcheck.append(self.xymap[checkpos1][pos2][0])
                        Hcounter += 1

                    randnum = random.choice(nums)

                    if 1 not in Vcheck or 1 not in Hcheck:
                        if 2 not in Vcheck or 2 not in Hcheck:
                            if 3 not in Vcheck or 3 not in Hcheck:
                                if 4 not in Vcheck or 4 not in Hcheck:
                                    if 5 not in Vcheck or 5 not in Hcheck:
                                        if 6 not in Vcheck or 6 not in Hcheck:
                                            if 7 not in Vcheck or 7 not in Hcheck:
                                                if 8 not in Vcheck or 8 not in Hcheck:
                                                    if 9 not in Vcheck or 9 not in Hcheck:
                                                        while randnum in Vcheck or randnum in Hcheck:
                                                            randnum = random.choice(nums)
                                                        
                                                        Vcheck.append(randnum)
                                                        self.xymap[pos1][pos2][0] = randnum

                                                    else:
                                                        retry = True  
                 
                
                

    #=============================================================================================================================