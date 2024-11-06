def affK(table):
    maxL = max([len(x) for x in table[0]+table[1]])
    printable = ""
    for i in range(len(table[0])):
        table[0][i] = table[0][i].ljust(maxL)
    for i in range(len(table[1])):
        table[1][i] = table[1][i].ljust(maxL)
    printable += "|"+"|".join(table[0]+table[1])+"|\n"
    for ligne in table[2:]:
        printable+= "|"+"|".join([v.ljust(maxL) for v in ligne[0]+ligne[1]])+"|\n"
    print(printable)