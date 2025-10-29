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

# Provjeravamo je li broj paran. 
# Možemo odrediti je li broj paran ako je dijeljiv s 2. 
# Ako je dijeljiv s dva pri dijeljenju s dva će ostatak biti 0.
#  boolean
#  |
#  ----------
#  |        |
#  |   int  |
#  |   |    |
#  -----    int
#  |   |    |
if n % 2 == 0:
    print("PARAN") # Ispisuje "PARAN" ako je broj paran

# else = ako nije zadovoljen prethodni uvjet
else:
    print("NEPARAN")  # Ispisuje "NEPARAN" ako broj nije paran
