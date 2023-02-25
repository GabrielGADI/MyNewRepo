# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu

# Ex 1.Funcție care să calculeze și să returneze suma a două numere

def suma(a, b):
    return a + b


s = suma(2, 9)
s1 = suma(5, 14)

print(s)
print(s1)

print(40 * "*")

# Ex 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def paritate(x):
    return x % 2 == 0

    print(paritate(8))

'''
def numar_par(numar):
    return numar % 2 == 0 #Daca returnezi se va returna valoarea acelei egalitati (Adevarat sau Fals)
'''


p = paritate(9)
p1 = paritate(10)
print(p)
print(p1)

print(40 * "*")

# Ex 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def character():
    nume = input("Nume: ")
    prenume = input("Prenume: ")
    nume_mijlociu = input("Nume_mijlociu: ")

    return len(nume + prenume + nume_mijlociu)

'''
def name_length(last, middle, first):
    return len(last+middle+first)

print(name_length("Badea", "Gheorghe", "Ioan"))
'''

'''
def nr_char(name):
    return (len(name))
'''


print(character())

print(40 * "*")

# Ex 4. Funcție care returnează aria dreptunghiului

def arie(x, y):
    return x * y

a = arie(7, 13)
a1 = arie(5, 9)
print(a)
print(a1)

''''
def aria_dreptunghiului(lungime, latime):
    return lungime * latime
'''

print(40 * "*")

# Ex 5. Funcție care returnează aria cercului

import math


def cerc(x):
    return math.pi * x * x

c = cerc(3)
c1 = cerc(7)

'''
from math import pi

def circle_area(radius):
    return pi * radius**2
'''


'''
def aria_cercului(r, p=3.14): # fara a importa math
    return p * (r ** 2) 
print(aria_cercului(7)) # doar daca vrem sa se afiseze
'''

print(c)
print(c1)

print(40 * "*")

# Ex 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.

def find(ch, string):
    if ch in string:
        return True
    else:
        return False

'''
def is_char_in_str(x, string):
    return x in string

print(is_char_in_str('a', 'My test string'))
'''
'''
def find(ch, string):  # o rezolvare mai simplista- va returna False sau True
    return ch in string
print(find("a", "colocvial")) # daca dorim sa afisam
'''


print(find(input("Char: "), "Luigy"))

print(40 * "*")

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

'''
def lower_upper_count(string):
    upper_lower = {'upper': 0, 'lower': 0}
    for c in string:
        if c.isupper():
            upper_lower['upper'] += 1
        elif c.islower():
            upper_lower['lower'] += 1
            
    return upper_lower

print(lower_upper_count("Hello World!"))
'''

'''
def low_upp(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            pass
    print(f"numarul de cractere upper este {upper}")
    print(f"numarul de caractere lower este {lower}")
print(low_up("NE doare CaPul"))  # doar pentru a afisa rezultatul
'''

print(40 * "*")

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

# print(lista(input("Nr: ").split(" ")))
print(l)
print(l1)

'''
def list_of_positives(lst):
    res_list = []
    for n in lst:
        if n>0:
            res_list.append(n)

    return res_list
            
print(list_of_positives([1,-6,-4,22,5,3,-9]))
'''
'''
def pozitve(numere):
    nr_pozitive1 = []

    for i in numere:
        if i > 0:
            nr_pozitive1.append(i)
    return nr_pozitive1
'''

print(40 * "*")

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

print(st)
print(st1)
'''
def add_to_set(n, numbers_set):
    if n in numbers_set:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return False
    else:
        numbers_set.add(n)
        print('Am adaugat numarul in set')
        return True
    
print(add_to_set(3, {1,2,4,5}))
'''

'''
def num_set(number, set):
    if number not in set:
        number.__add__(set)
        print("am adaugat nr in nou in set")
        return True
    elif number in set:
        print('nu am adaugat nr in set, acesta exista deja')
        return False
    else:
        pass
'''



print(40 * "*")