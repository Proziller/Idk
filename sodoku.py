#!/bin/python3

map1 = [
    [{"zahl": "", "writable": False},{"zahl": "", "writable": False}],
    [{"zahl": "", "writable": False},{"zahl": "", "writable": False}],
]
map2 = [
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]],
    [[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false],[" ",false]]
]
zahlen = ["1","2","3","4","5","6","7","8","9"]

pos1 = input("pos1: ")
pos2 = input("pos2: ")

if pos1 in zahlen:
    pos1 = int(pos1)
else:
    print("error")

if pos2 in zahlen:
    pos2 = int(pos1)
else:
    print("error")

print(map2[pos1][pos2][0])