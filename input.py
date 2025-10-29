""" s = input() """ # vraća string

""" print(s + 1) """ # Daje error (zbrajanje stringa i inta)

n = int(input())
#    |   |
#    |   -- Uzima unos, vraća string
#    -- Pretvara neki tip (u ovom slučaju string) u int

print(n + 1) # Dobro (zbrajanje inta i inta)
#     |   |
#     ------ Intovi

#     string   string    string
#     |        |              |
#     ------   ---   ----------
#     |    |   | |   |        |
print(str(n) + " " + str(n + 1)) # Ispisuje n pa razmak pa n+1
#      |  |  |     |  |  |   |
#      |  |  |     |  |  |   |
#      |  |  |     |  |  |   |
#      |  |  |     |  |  |   |
#      |  |  |     |  |  |   |
#      |  |  |     |  |  |   |
#      |  |  |     |  |  |   |