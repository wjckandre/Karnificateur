def table_verite():
    table = []
    nb_entrees = int(input("nombre d'entrées : "))
    nb_sorties = int(input("nombre de sorties : "))
    temp = []
    for k in range(nb_entrees):
        temp.append(input(f"nom de l'entrée {k+1} : "))
    table.append(temp)
    temp = []
    for i in range(nb_sorties):
        temp.append(input(f"nom de la sortie {i+1} : "))
    table.append(temp)
    for x in range(2**nb_entrees):
        vEntree = bin(x)[2:].zfill(len(table[0]))
        table.append([vEntree,"".join([input(f"{table[1][z]} pour {vEntree} : ") for z in range(nb_sorties)])])
    return table

def gray(b):
    b=int(b,2)
    b^=(b>>1)
    return b

def format(table):
    maxL = max([len(x) for x in table[0]+table[1]])
    for i in range(len(table[0])):
        table[0][i] = table[0][i].ljust(maxL)
    for i in range(len(table[1])):
        table[1][i] = table[1][i].ljust(maxL)
    return table,maxL

def affTV(table):
    table,maxL = format(table)
    printable = ""
    printable += "|"+"|".join(table[0]+table[1])+"|\n"
    for ligne in table[2:]:
        printable+= "|"+"|".join([v.ljust(maxL) for v in ligne[0]+ligne[1]])+"|\n"
    print(printable)

def affK(table):
    table,maxL = format(table)
    printable = ""
    mid = len(table[0])//2+len(table[0])%2
    kValues1 = [bin(gray(bin(i)[2:]))[2:].zfill(len(table[0][:mid])) for i in range(pow(2,len(table[0][:mid])))]
    kValues2 = [bin(gray(bin(i)[2:]))[2:].zfill(len(table[0][mid:])) for i in range(pow(2,len(table[0][mid:])))]
    for s in range(len(table[1])):
        printable += f"Sortie {table[1][s]} :\n"
        printable += "|"+"".join(table[0][:mid])+"|"+"".join(table[0][mid:]) + " " + " ".join([bin(gray(bin(i)[2:]))[2:].zfill(len(table[0][mid:])) for i in range(pow(2,len(table[0][mid:])))]) + "|\n"
        for kv in kValues1:
            printable += "|" + "".join([v.ljust(maxL) for v in list(kv)]) + "|" + " "*(maxL*len(table[0][mid:])+1) + (" "*len(kValues2[0])).join([table[int(kv+x,2)+2][1][s] for x in kValues2]) + " "*(len(table[0][mid:])-1) + "|\n"
    print(printable)


table = [
    ["a1","a0","a3","a2"],
    ["s","x"],
    ["0000","10"],
    ["0001","01"],
    ["0010","11"],
    ["0011","00"],
    ["0100","00"],
    ["0101","00"],
    ["0110","00"],
    ["0111","00"],
    ["1000","00"],
    ["1001","00"],
    ["1010","00"],
    ["1011","00"],
    ["1100","00"],
    ["1101","00"],
    ["1110","00"],
    ["1111","11"]
]
t = table_verite()
affTV(t)
affK(t)