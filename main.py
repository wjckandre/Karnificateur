
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

print(table_verite())

def gray(b):
    b=int(b,2)
    b^=(b>>1)
    return bin(b)[2:]

def affTV(table):
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

def affK():
    pass