#!/bin/python3

import random

map = [
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
    [["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False],["□",False]],
]


def print_map():
    print(map[6][6][0],map[6][7][0],map[6][8][0],"|",map[7][6][0],map[7][7][0],map[7][8][0],"|",map[8][6][0],map[8][7][0],map[8][8][0])
    print(map[6][3][0],map[6][4][0],map[6][5][0],"|",map[7][3][0],map[7][4][0],map[7][5][0],"|",map[8][3][0],map[8][4][0],map[8][5][0])
    print(map[6][0][0],map[6][1][0],map[6][2][0],"|",map[7][0][0],map[7][1][0],map[7][2][0],"|",map[8][0][0],map[8][1][0],map[8][2][0])
    print("---------------------")
    print(map[3][6][0],map[3][7][0],map[3][8][0],"|",map[4][6][0],map[4][7][0],map[4][8][0],"|",map[5][6][0],map[5][7][0],map[5][8][0])
    print(map[3][3][0],map[3][4][0],map[3][5][0],"|",map[4][3][0],map[4][4][0],map[4][5][0],"|",map[5][3][0],map[5][4][0],map[5][5][0])
    print(map[3][0][0],map[3][1][0],map[3][2][0],"|",map[4][0][0],map[4][1][0],map[4][2][0],"|",map[5][0][0],map[5][1][0],map[5][2][0])
    print("---------------------")
    print(map[0][6][0],map[0][7][0],map[0][8][0],"|",map[1][6][0],map[1][7][0],map[1][8][0],"|",map[2][6][0],map[2][7][0],map[2][8][0])
    print(map[0][3][0],map[0][4][0],map[0][5][0],"|",map[1][3][0],map[1][4][0],map[1][5][0],"|",map[2][3][0],map[2][4][0],map[2][5][0])
    print(map[0][0][0],map[0][1][0],map[0][2][0],"|",map[1][0][0],map[1][1][0],map[1][2][0],"|",map[2][0][0],map[2][1][0],map[2][2][0])

#TODO: revisit after doing check
def generate(amount):

    for i in range(amount):

        randpos1 = random.randint(0,8)
        randpos2 = random.randint(0,8)
        randnum = random.randint(1,9)

        if map[randpos1][randpos2][1] != True:
            map[randpos1][randpos2][1] = True
            map[randpos1][randpos2][0] = str(randnum)

        else:
            while map[randpos1][randpos2][1] == True:
                randpos1 = random.randint(0,8)
                randpos2 = random.randint(0,8)

            map[randpos1][randpos2][1] = True
            map[randpos1][randpos2][0] = str(randnum)

        print("pos1: ",randpos1)
        print("pos2: ",randpos2)
        print(map[randpos1][randpos2])


def mark():
    zahlen = ["1","2","3","4","5","6","7","8","9"]

    pos1 = input("pos1: ")

    if pos1 in zahlen:
        pos1 = int(pos1)
        pos1 -= 1

        pos2 = input("pos2: ")

        if pos2 in zahlen:
            pos2 = int(pos2)
            pos2 -= 1
            if map[pos1][pos2][1] == False:
                new_num = input("new entry")

                if new_num in zahlen:
                    map[pos1][pos2][0] = new_num
                else:
                    print("error")
            else:
                print("already occupied")
        else:
            print("error")
    else:
        print("error")

generate(10)
print_map()

#mark()

#print(map1)
#print(map2)

#print(map1[0][0])
#print("pos1: ", pos1, "pos2: ", pos2, "map2[0][0]:\n", map2[0][0])