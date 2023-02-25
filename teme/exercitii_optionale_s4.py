# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
# Google.

# Ex 1
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final

for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    elif i < 0:
        numere_negative.append(i)

print(f"Nr pare - {numere_pare}")
print(f"Nr impare - {numere_impare}")
print(f"Nr > 0 - {numere_pozitive}")
print(f"Nr < 0 -{numere_negative}")

print(40 * "*")

# Ex 2
# Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4
# Am tras cu ochiul putin pe net si am inteles pana la urma metoda de sortrare. Var1 este de pe net si Var2 este varianta modificata si facuta de mine. Flag-ul switch ajuta la eficienta algoritmului in caz ca nu mai sunt elemente de sortat si se asigura ca se iese din primul `for` care si-ar continua treaba indiferent daca ar mai fi sau nu numere de sortat, pt eficienta la runtime.

# var 1

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
a = len(alte_numere)

for i in range(a):
    switch = False
    for j in range(a-i-1):
        if alte_numere[j] > alte_numere[j+1]:
            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
            switch = True
    if not switch:
        break

print(alte_numere)

# var 2

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
a = len(alte_numere)

for i in range(a):
    switch = False
    for j in range(1, a-i):
        if alte_numere[j] < alte_numere[j-1]:
            alte_numere[j], alte_numere[j-1] = alte_numere[j-1], alte_numere[j]
            switch = True
    if not switch:
        break

print(alte_numere)

print(40 * "*")

# Ex 3
# Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
#
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
import random
numar_secret = random.randint(1,30)
numar_ghicit = None

while True:
    numar_ghicit = int(input("Alege un nr 1-30: "))
    if numar_ghicit < numar_secret:
        print("Nr secret e mai mare\n")
    elif numar_ghicit > numar_secret:
        print("Nr secret e mai mic\n")
    else:
        print("Felicitări! Ai ghicit!\n")
        break

print(40 * "*")
