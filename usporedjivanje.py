a = 30  # Int
b = 30  # Int
c = 20  # Int

#     boolean
#     |
#     ------
#     |    |
print(a == b)  # Je li a (30) jedanko b (30)

#     boolean
#     |
#     ------
#     |    |
print(a == c)  # Je li a (30) jedanko c (20)


#     boolean
#     |
#     ------
#     |    |
print(a != b)  # Je li a (30) nejedanko b (30)

#     boolean
#     |
#     ------
#     |    |
print(a != c)  # Je li a (30) nejedanko c (20)


#     boolean
#     |
#     ------
#     |    |
print(a < b)  # Je li a (30) manje od b (30)

#     boolean
#     |
#     ------
#     |    |
print(a < c)  # Je li a (30) manje od c (20)


#     boolean
#     |
#     ------
#     |    |
print(a > b)  # Je li a (30) veće od b (30)

#     boolean
#     |
#     ------
#     |    |
print(a > c)  # Je li a (30) veće od c (20)


#     boolean
#     |
#     ------
#     |    |
print(a <= b)  # Je li a (30) manje ili jedanko od b (30)

#     boolean
#     |
#     ------
#     |    |
print(a <= c)  # Je li a (30) manje ili jednako od c (20)


#     boolean
#     |
#     ------
#     |    |
print(a >= b)  # Je li a (30) veće ili jednako od b (30)

#     boolean
#     |
#     ------
#     |    |
print(a >= c)  # Je li a (30) veće ili jednako od c (20)


s1 = "nesto"  # String
s2 = "nesto"  # String
s3 = "nesto2"  # String

#     boolean
#     |
#     --------
#     |      |
print(s1 == s2)  # Je li s1 ("nesto") jedanko s2 ("nesto")

#     boolean
#     |
#     --------
#     |      |
print(s1 == s3)  # Je li s1 ("nesto") jedanko s3 ("nesto2")


#     boolean
#     |
#     --------
#     |      |
print(s1 != s2)  # Je li s1 ("nesto") nejedanko s2 ("nesto")

#     boolean
#     |
#     --------
#     |      |
print(s1 != s3)  # Je li s1 ("nesto") nejedanko s3 ("nesto2")


# PRIMJER

godina = int(input())

# Ako je godina manja od 0
#   boolean
#   |
#   ----------
#   |        |
if (godina < 0):
    print("Nisi još rođen.")
# Inače ovo
else:
    print("Rođen si.")
