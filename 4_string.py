string = "jhskhusifhuihfuhdz"
# Varijabla koja sadrži string

#     string
#     |
#     ------
#     |    |
print(string)
# Ispisuje cijeli string ("jhskhusifhuihfuhdz")

#     int
#     |
#     -----------
#     |         |
#     |  string |
#     |   |     |
#     |   ------|
#     |   |    ||
print(len(string))
# Funkcija len() vraća broj znakova u stringu (duljinu)

#     string   
#     |        
#     ---------
#     |       |
#     |    int|
#     |      ||
print(string[0])
# Dohvaća znak na indeksu 0 (prvi znak u stringu)

#     string
#     |
#     -----------------------
#     |                     |
#     |      int            |
#     |      |              |
#     |      ---------------|
#     |      |             ||
#     |      |   string    ||
#     |      |   |         ||
#     |      |   ------    ||
#     |      |   |    |    ||
print(string[len(string) - 1])
# Dohvaća zadnji znak stringa
# len(string) vraća duljinu (npr. 18), a -1 jer indeksi počinju od 0

#        string
#        |
#        -------------------
#        |                 |
#        |      int        |
#        |      |          |
#        |      -----------|
#        |      |         ||
#        |      |   string||
#        |      |   |     ||
#        |      |   ------||
#        |      |   |    |||
"""print(string[len(string)])"""
# Daje error
# Jer len(string) vraća duljinu 18, ali zadnji indeks je 17
