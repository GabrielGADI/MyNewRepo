import random # trebuie importata functia random pentru  Joc ghicit zarul


# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
a = 6783
a = str(a)
print(len(a))
if len(a) < 4:
    print("Nu are minim 4 cifre")
else:
    print("are cele 4 cifre sau mai multe.")

# 2.Verifică dacă x are exact 6 cifre.
if len(a) == 6:
    print("Are 6 cifre.")
else:
    print("nu are")

# 3.Verifică dacă x este număr par sau impar (x e int).
a = 6783
if a % 2 == 0:
    print("este par")
else:
    print("este impar")

# 4. x, y, z (int) Afișează care este cel mai mare dintre ele?
x = 3
y = 3
z = 3
if x > y and x > z:
    print(f"{x} mai mare")
elif y > x and y > z:
    print(f"{y} este mai mare ")
elif z > x and z > y:
    print(f"{z} este mai mare ")

print(max(x,y,z)) # o metoda simplificata pentru a afisa care este mai mare

'''
5. X, y, z - reprezintă unghiurile unui triunghi. 
Verifică și afișează dacă triunghiul este valid sau nu.
'''
x = 120
y = 40
y = 60
if x + y + z == 180 and x != 0 and y != 0 and z != 0: # sau x + y + z == 180 and x and y and z
    print(" Este un triunghi valid ")
else:
    print(" Nu este un triunghi valid ")

'''
6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citește de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
a = 'Coral is either the stupidest animal or the smartest rock'
a = int(input())
print(a[:-7])

'''
7. Același string. Declară un string nou care să fie 
format din primele 5 caractere + ultimele 5.
'''
a = 'Coral is either the stupidest animal or the smartest rock'
# sliceing
first = a[:5]
last = a[-5:]
print(first,last)

'''8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvânt
● output: 'Coral is either the stupidest animal or the smartest'
'''
a = 'Coral is either the stupidest animal or the smartest rock'
ab = a.find("rock")
print(a[:ab])


'''
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''

ghicit= int(input("alege un numar la zar :"))
dice_roll = random.randint(1,6)
if ghicit == dice_roll:
    print("Ai ghicit")
elif ghicit > dice_roll:
    print("Ai pierdut pentru ca ai ales un numar mai mare.")
else:
    print("Ai pierdut pentru ca ai ales un numar mai mic.")


