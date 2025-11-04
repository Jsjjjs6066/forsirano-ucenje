n = int(input())

# Provjeravamo je li broj paran. 
# Možemo odrediti je li broj paran ako je dijeljiv s 2. 
# Ako je dijeljiv s dva pri dijeljenju s dva će ostatak biti 0.
if n % 2 == 0:
    print("PARAN") # Ispisuje "PARAN" ako je broj paran

# else = ako nije zadovoljen prethodni uvjet
else:
    print("NEPARAN")  # Ispisuje "NEPARAN" ako broj nije paran
