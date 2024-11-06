
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