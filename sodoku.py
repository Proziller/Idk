import sodoku_lib as sodoku
print("-~==~==~==~==~==~==~-")
difficulty = input("difficulty: ")

sodoku1 = sodoku.SoMap(difficulty)

sodoku1.generate()
while True:
    sodoku1.print_map()
    sodoku1.mark()