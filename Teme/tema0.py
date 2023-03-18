''' Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă:- string- int- float- bool
'''
casa_frumoasa = True
numar_etaje = 10
diagonala_tv = 81.5
tip_apa = "sarata"

# Utilizează funcția type pentru a verifica dacă au tipul de date așteptat

print(type(casa_frumoasa))
print(type(numar_etaje))
print(type(diagonala_tv))
print(type(tip_apa))
'''Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):    Verifică tipul acesteia.
'''
round(diagonala_tv)
print(type(round(diagonala_tv)))

'''Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești'''
print(f"Este aceasta casa frumosa?" + str(casa_frumoasa))
print(f"Blocul are " + str(numar_etaje) + " etaje.")
print(f"Un televizor de " + str(diagonala_tv) + " cm este scump!")
print(f"In mare gasesti apa" + str(tip_apa) + ".")

'''Citește de la tastatură:  - numele;- prenumele.
Afișează: 'Numele complet are x caractere'.
'''
numele = input('Numele meu este: ')
prenumele = input('Prenumele meu este')
print(f"Numele complet are {len(prenumele + numele)} caractere")

'''Citește de la tastatură:   - lungimea;- lățimea.
Afișează: 'Aria dreptunghiului este x'.'''
lungimea = 6
latimea = 4
x = lungimea * latimea
print(f"Aria dreptunghiului este: {x}")

'''Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';'''

string = 'Coral is either the stupidest animal or the smartest rock.'
print(string.count('the'))
caracter = input("introduceti un string: ")
first_caracter = caracter[0]
caracter = first_caracter + caracter[1:-1].replace(first_caracter, first_caracter.upper()) + caracter[-1]
print(caracter)
