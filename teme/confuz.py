'''
 10. Aceeași listă:
  ● Iterează prin ea.
  ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
  Ex: dacă e 3, să devină -3
  ● Afișază noua listă.
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)
# Ex 3.
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
print(numar_secret)
while True:
    numar_ghicit = int(input("Alege un nr 1-30: "))
    if numar_ghicit < numar_secret:
        print("Nr secret e mai mare\n")
    elif numar_ghicit > numar_secret:
        print("Nr secret e mai mic\n")
    else:
        print("Felicitări! Ai ghicit!\n")
        break

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
#masini[1] = [masina.upper() for masina in masini[1:-1]]
print(masini)
masini[1] = [masina.upper() for masina in masini[1]]
print(masini)
#masini[1:-1] = [masina.upper() for masina in masini[1]]
print(masini)

masini[:] = [masina.upper() for masina in masini[:]]
print(masini)
