#!/bin/python3

map1 = [
    [{"zahl": "", "writable": False},{"zahl": "", "writable": False}],
    [{"zahl": "", "writable": False},{"zahl": "", "writable": False}],
]
map2 = [
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
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
else:
    print("error")

if pos2 in zahlen:
    pos2 = int(pos1)
    pos2 -= 1
else:
    print("error")

print(map2[pos1][pos2][0])