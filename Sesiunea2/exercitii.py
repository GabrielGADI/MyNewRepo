# Exercitii
'''
1. Sa se scrie un program care citeste 2 nr de la tastatura si afiseaza urmatoarele informatii:
    a. Daca primul numar este par
    b. Daca al doilea numar este impar
    c. Suma numerelor
    d. Catul numerelor daca al doilea este diferit de 0, altfel se afiseaza un mesaj in care se specifica “Catul nu se poate realiza”
    e. Primul numar ridicat la puterea al doilea numar
    f. Care este numar mai mare
    g. Daca ambele numere sunt pozitive
    h. Daca ambele numere sunt negative
'''

a = int(input("introdu un nr: "))
b = int(input("introdu un nr2: "))

# a. - daca primul nr e par
if a % 2 == 0:
    print("a. primul nr e par")
else:
    print("a. ----")

# b. - Daca al doilea numar este impar  fara sa folosim op de comparatie
if b % 2:  # se poate si b % 2 !=0, dar se subaintelege ca este difeit de 0
    print("b. al doilea nr este impar")
else:
    print("b. ------")

# c. Suma numerelor
print(f"c. Suma nr este {a + b} ")

# d. Catul numerelor daca al doilea este diferit de 0,
# altfel se afiseaza un mesaj in care se specifica “Catul nu se poate realiza”

if b:
    print(f"d. Catul a/b este {a / b}")
else:
    print("Catul nu se poate realiza")

# e. Primul numar ridicat la puterea al doilea numar
print(f"e. a la puterea b este {a ** b}")

# f.  Care este numar mai mare

print("f. a este mai mare") if a > b else print("f. b este mai mare")

# g. Daca ambele numere sunt pozitive
# h. Daca ambele numere sunt negative
