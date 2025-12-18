l1 = [] # Prazna lista
l2 = [1, 2, 3] # Lista s tri inta
l3 = ["a", "b", "c"] # Lista s tri stringa

# Duljine lista
print("Duljina l1: ", len(l1))
print("Duljina l2: ", len(l2))
print("Duljina l3: ", len(l3))

# Ispis elemenata lista (ružni način koji se ne priznaje na natjecanjima)
print("Elementi l1: ", l1)
print("Elementi l2: ", l2)
print("Elementi l3: ", l3)

# Pristupanje elementima lista
print("Prvi element l2: ", l2[0])
print("Drugi element l3: ", l3[1])
print("Zadnji element l1: ", l2[len(l1)-1])
print("Zadnji element l1: ", l2[-1])
"""print("Pretjerani pristup l1: ", l1[0])""" # Ovo će izazvati grešku

# Modifikacija elemenata lista
l2[0] = 10
l3[1] = "z"
print("Modificirani l2: ", l2)
print("Modificirani l3: ", l3)

# Dodavanje elemenata na kraj liste
l1.append(5)
l2.append(4)
print("l1 nakon dodavanja: ", l1)
print("l2 nakon dodavanja: ", l2)

# Idi kroz listu
zbroj = 0 # Samo za primjer korištenja petlje
for broj in l2:
    zbroj += broj
print("Zbroj elemenata u l2: ", zbroj)

# Lijep ispis lista (svaki element u novom retku)
print("l1:")
for element in l1:
    print(element)
print("l2:")
for element in l2:
    print(element)
print("l3:")
for element in l3:
    print(element)
    
# Lijep ispis lista (svi elementi u jednom retku, razdvojeni razmakom)
print("l1:")
for element in l1:
    print(element, end=" ")
print() # Novi red
print("l2:")
for element in l2:
    print(element, end=" ")
print() # Novi red
print("l3:")
for element in l3:
    print(element, end=" ")