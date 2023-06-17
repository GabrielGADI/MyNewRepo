print(20 * " - ", "Numara ordonat", 20 * " - ")
count = 0
while count < 3:
    count += 1  # daca nu se pune aceasta regula va fi infinit
    print(f"Count : {count}")

print(20 * " - ", "iterare pe lista", 20 * " - ")
l = [1, 2, 3, 4, 5]
index = 0
while index < len(l):
    print(f"Element: {l[index]}")
    index += 1

print(20 * " - ", "break", 20 * " - ")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # forteaza ierirea din bucla
    i += 1  # i = i + 1crestem

print(20 * " - ", "break + bucla infinita", 20 * " - ")
import random

while True:
    nr = random.randint(0, 9)
    print(nr)
    if nr % 2 == 0:
        break

print(20 * " - ", "continue", 20 * " - ")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # skip peste anumite elemente (3) sare peste codul de desesupt
    print(i)

print(20 * " - ", "else", 20 * " - ")
count = 0
while count < 3:
    count += 1
    print(f"Count: {count}")
else:  # se executa cand se termina bucla, cand conditia devine falsa
    print(f" In blocul Else")
# se executa la finalul buclei while cand conditia devine falsa

print(20 * " - ", "else  + break", 20 * " - ")
count = 0
while count < 3:
    count += 1
    print(f"Count: {count}")
    if count == 2:
        break  # intrerupe toata bucla, nu se mai executa
else:  # se executa cand se termina bucla
    print(f" In blocul Else")
# nu se mai executa pentru ca a aparut break
