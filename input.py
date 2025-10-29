""" s = input() """ # vraća string

""" print(s + 1) """ # Daje error (zbrajanje stringa i inta)

#   int
#   |
#   ------------
#   |          |
#   |   string |
#   |   |      |
#   |   -------|
#   |   |     ||
n = int(input())
#    |   |
#    |   -- Uzima unos, vraća string
#    -- Pretvara neki tip koji se nalazi u zagradama (u ovom slučaju string) u int

#     int
#     |
#     -----
#     |   |
print(n + 1) # Dobro (zbrajanje inta i inta)
#     |   |
#     ------ Intovi

#     string   string    string
#     |        |              |
#     ------   ---   ----------
#     |    |   | |   |        |
print(str(n) + " " + str(n + 1)) # Ispisuje n pa razmak pa n+1
#      |  |  |     |  |  |   |
#      |  |  |     |  |  ------ Zbrojimo int iz varijable "n" i int "1"
#      |  |  |     |  -- Pretvaramo neki tip koji se nalazi u zagradama (u ovom slučaju int) u string
#      |  |  |     -- Prijašnje dobivenom stringu dodajemo string s desna
#      |  |  --Prijašnje dobivenom stringu dadajemo string s desna (u ovom slučaju " ")
#      |  -- Int iz varijable "n"
#      -- Pretvaramo neki tip koji se nalazi u zagradama (u ovom slučaju int) u string
