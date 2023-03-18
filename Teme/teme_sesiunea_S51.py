# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu

# Ex 1.Funcție care să calculeze și să returneze suma a două numere

def suma(a, b):
    return a + b


s = suma(2, 9)
s1 = suma(5, 14)


# Ex 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def paritate(x):
    x = int(x)
    if x % 2 == 0:
        return True
    else:
        return False


p = paritate(9)
p1 = paritate(10)


# Ex 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def character():
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    nume_mijlociu = input("Nume_mijlociu: ")

    return len(nume + prenume + nume_mijlociu)


# Ex 4. Funcție care returnează aria dreptunghiului

def arie(x, y):
    return x * y


a = arie(7, 13)
a1 = arie(5, 9)

# Ex 5. Funcție care returnează aria cercului

import math


def cerc(x):
    return math.pi * x * x


c = cerc(3)
c1 = cerc(7)


# Ex 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.

def find(ch, string):
    if ch in string:
        return True
    else:
        return False


# Ex 7. Funcție fără return, primește un string și printează pe ecran:
# ● Numărul de caractere lower case este x
# ● Numărul de caractere upper case este y

def check_chr(x):
    low = 0
    high = 0

    for i in x:
        if i.isupper():
            high += 1
        else:
            low += 1

    print(f"Numărul de caractere lower case este {low}")
    print(f"Numărul de caractere upper case este {high}")


check_chr(input("String: "))


# Ex 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu
# numerele pozitive.

def lista(x):
    poz = []

    for i in x:
        if int(i) > 0:
            poz.append(int(i))
    return poz


l = lista([1, 5, -5, 0, 9, 20, -70, 90])
l1 = lista([1, 2, -5, 0, -70, 90])


# Ex 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# ● Primul număr x este mai mare decat al doilea număr y
# ● Al doilea număr y este mai mare decat primul număr x
# ● Numerele sunt egale.

def comparare(x, y):
    if x > y:
        print(f"Primul număr {x} este mai mare decat al doilea număr {y}")
    elif y > x:
        print(f"Al doilea număr {y} este mai mare decat primul număr {x}")
    else:
        print("Numerele sunt egale")


comparare(8, 14)
comparare(9, 16)

print(40 * "*")


# Ex 10. Funcție care primește un număr și un set de numere.
# ● Printează ‘am adaugat numărul nou în set’ + returnează True
# ● Printează ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

def store(nr, set1):
    if nr in set1:
        set1.add(nr)
        print("nu am adaugat numărul în set. Acesta există deja")
        return False
    else:
        set1.add(nr)
        print("am adaugat numărul nou în set")
        return True


st = store(4, {4, 6, 9, 12, 16})
st1 = store(7, {5, 8, 12, 17, 28})
