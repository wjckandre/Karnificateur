from tkinter import *

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

def affTVtk(table):
    root = Tk()
    table[0] = table[0]+table.pop(1)
    print(table)
    table = [table[0]] + [list(x[0])+list(x[1]) for x in table[1:]]
    print(table)
    for i in range(len(table)):
        for j in range(len(table[0])):
            c = Label(root, text=table[i][j])
            c.grid(row=i, column=j)
    mainloop()

def affKtk(table):
    root = Tk()
    offset=0
    mid = len(table[0])//2+len(table[0])%2
    entries1 = table[0][:mid]
    entries2 = table[0][mid:]
    sorties = table[1]
    table = [table[:2]] + [list(x[1]) for x in table[2:]]
    for s in range(len(sorties)):
        c = Label(root, text=f"Sortie '{sorties[s]}'")
        c.grid(row=0, column=0+offset, columnspan=10)
        c = Label(root, text="".join(entries1))
        c.grid(row=1, column=0+offset)
        c = Label(root, text="|")
        c.grid(row=1, column=1+offset)
        c = Label(root, text="".join(entries2))
        c.grid(row=1, column=2+offset)
        kValues1 = [bin(gray(bin(i)[2:]))[2:].zfill(len(entries1)) for i in range(pow(2,len(entries1)))]
        kValues2 = [bin(gray(bin(i)[2:]))[2:].zfill(len(entries2)) for i in range(pow(2,len(entries2)))]
        for kv in kValues2:
            c = Label(root, text=kv)
            c.grid(row=1, column=3+kValues2.index(kv)+offset)
        for kv in kValues1:
            c = Label(root, text=kv)
            c.grid(row=kValues1.index(kv)+2, column=0+offset)
            c = Label(root, text="|")
            c.grid(row=kValues1.index(kv)+2, column=1+offset)
            for x in range(len(kValues2)):
                c = Label(root, text=table[int(kv+kValues2[x],2)+1][s])
                c.grid(row=kValues1.index(kv)+2, column=3+x+offset)
        c = Label(root, text="    ")
        c.grid(row=1, column=4+x+offset)
        offset+=3+len(kValues2)+1
    mainloop()

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
t = [['a1', 'a0'], ['s'], ['00', '1'], ['01', '1'], ['10', '1'], ['11', '0']]
t2= [['a3', 'a2', 'a1', 'a0'], ['s1', 's0'], ['0000', '11'], ['0001', '11'], ['0010', '11'], ['0011', '10'], ['0100', '01'], ['0101', '11'], ['0110', '01'], ['0111', '11'], ['1000', '11'], ['1001', '00'], ['1010', '10'], ['1011', '11'], ['1100', '11'], ['1101', '11'], ['1110', '11'], ['1111', '10']]
t3= [['a2', 'a1', 'a0'], ['s'], ['000', '1'], ['001', '0'], ['010', '1'], ['011', '0'], ['100', '1'], ['101', '0'], ['110', '1'], ['111', '1']]

#affTV(t)
#affK(t)
#affTVtk(t2)
#affKtk(t3)