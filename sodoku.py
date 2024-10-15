import sodoku_lib as sodoku

sodoku1 = sodoku.SoMap(30)

sodoku1.generate()
while True:
    sodoku1.print_map()
    sodoku1.mark()