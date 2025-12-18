s = input() 
# |   |
# |   -- Uzima unos korisnika i vraća string
# -- Spremamo dobiveni string u varijablu s

# Ako je unos jednak stringu "Borna"
#  -- Varijabla koja sadrži unos korisnika
#  | -- Operator usporedbe (provjerava jesu li dvije vrijednosti jednake)
#  | |     -- String s kojim uspoređujemo
#  | |     |
if s == "Borna":
    print("Los")  # Ispisuje "Los" ako je unos bio "Borna"

# elif = else if, tj. "ako nije prethodno, ali je ovo istina"
# Provjerava je li unos jednak stringu "Luka"
elif s == "Luka":
    print("Još gori")  # Ispisuje "Još gori" ako je unos bio "Luka"

# else = ako nije zadovoljen nijedan prethodni uvjet
else:
    print("idk")  # Ispisuje "idk" ako unos nije ni "Borna" ni "Luka"
