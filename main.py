
def table_verite():
    table = []
    nb_entry = int(input("nb_entry : "))
    nb_sortie = int(input("nb_sortie : "))
    temp = []
    for k in range(nb_entry):
        temp.append(input(f"nom de la {k+1} entrées : "))
    table.append(temp)
    temp = []
    for i in range(nb_sortie):
        temp.append(input(f"nom de la {i+1} sorties : "))
    table.append(temp)
    for x in range(pow(2,nb_entry)):
        table.append([input("entrées : "), input("sorties : ")])
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
    printable += "|"+"".join(table[0][:mid])+"|"+"".join(table[0][mid:]) + " " + " ".join([bin(gray(bin(i)[2:]))[2:].zfill(len(table[0][:mid])) for i in range(pow(2,len(table[0][mid:])))]) + "|\n"
    kValues1 = [bin(gray(bin(i)[2:]))[2:].zfill(len(table[0][:mid])) for i in range(pow(2,len(table[0][:mid])))]
    kValues2 = [bin(gray(bin(i)[2:]))[2:].zfill(len(table[0][:mid])) for i in range(pow(2,len(table[0][mid:])))]
    for s in range(len(table[1])):
        printable += f"Sortie {table[1][s]} :\n"
        for kv in kValues1:
            printable += "|" + "".join([v.ljust(maxL) for v in list(kv)]) + "|" + " "*(maxL*len(table[0][mid:])+1) + (" "*maxL).join([table[int(kv+x,2)+2][1][s] for x in kValues2]) + " |\n"
    print(printable)


table = [
    ["a1","a0","b1","b0"],
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
affK(table)