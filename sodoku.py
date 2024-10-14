#!/bin/python3

]
map = [
    [["Hello",False],["world",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],["2nd row 2nd column",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]]
]
zahlen = ["1","2","3","4","5","6","7","8","9"]

pos1 = input("pos1: ")
pos2 = input("pos2: ")

if pos1 in zahlen:
    pos1 = int(pos1)
    pos1 -= 1
    if pos2 in zahlen:
        pos2 = int(pos2)
        pos2 -= 1
        print(map[pos1][pos2][0])
    else:
        print("error")
else:
    print("error")



#print(map1)
#print(map2)

#print(map1[0][0])
#print("pos1: ", pos1, "pos2: ", pos2, "map2[0][0]:\n", map2[0][0])