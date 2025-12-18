x = 0
# Ime varijable je "x", a vrijednost 0

a = 1 # Cijeli broj (int)
b = 1.2 # Decimalni broj (float)
c = "abc" # Skupina znakova (svaki znak može biti broj, slovo, "."...) (string)
d = True # Točno ili netočno (boolean)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

a = 2 # Možemo i promjeniti vrijednost varijable
print("\na nakon promjene:", a)

# Lakši način za ispisivanje s varijablama:
print(f"\nVrijednost varijable a je {a}!")
print(f"Vrijednost varijable b je {b}!")
print(f"Vrijednost varijable c je {c}!")
print(f"Vrijednost varijable d je {d}!")
# Stavimo f prije navodnika kako bismo napravili f-string.
# Tamo gdje stavimo vitičaste zagrade ({ i }) stavit će vrijednost varijable
# čije smo ime stavili.
