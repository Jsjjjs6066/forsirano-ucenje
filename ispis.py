print("Hello world!") # Ispisuje "Hello world!" (bez navodnika)
print("Hello", "netko!") # U `print` funkciji kada odvojimo nešto zarezom, dodat će razmak između
print("\nHello!") # "\n" ide u sljedeći red.
# `print` funkcija će automatski staviti taj znak nakon svakog ispisa.
# Možemo staviti na kraju funkcije tako da ode dva reda ispod umjesto jednog.
# Što će se dogoditi ako "\n" stavimo dva puta.

# Ako ne želimo da završi s time možemo promjeniti `end` argument u funkciji
print("Hello", end=" ") # Završava s " " umjesto "\n"
print("world!\n") # Provjeri radi li

# `end` argument može i biti prazan string ("")
print("H", end="")
print("I")