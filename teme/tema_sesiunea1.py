# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# variabila - o zona de memorie care tine diferite tipuri de date

'''
2.. Declară și initializează câte o variabilă din
 fiecare din următoarele tipuri de variabilă:
 - string
 - int
 - float
 - bool
 Observație: Valorile vor fi alese de tine după preferințe.
'''
tip_apa = "sarata"
numar_etaje = 10
diagonala_tv = 81.525
casa_frumoasa = True

# 3.Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(tip_apa))
print(type(numar_etaje))
print(type(diagonala_tv))
print(type(casa_frumoasa))

'''
4.Rotunjește ‘float’-ul folosind funcția round() și salvează 
această modificare în aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
diagonala_tv = round(diagonala_tv,5)
print(type(diagonala_tv))

'''
 5.Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print(f"Este aceasta casa frumosa? {casa_frumoasa}")
print(f"Blocul are {numar_etaje} etaje.")
print(f"Un televizor de {diagonala_tv} este scump!")
print(f"In mare gasesti apa {tip_apa}.")

'''
 6.Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.

'''
numele = input('Numele meu este: ')
prenumele =input('Prenumele meu este: ')
print(f"Numele complet are {len(prenumele + numele)} caractere")

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
lungimea = int(input('Lungimea este: '))
latimea = int(input('Latimea este: '))
x = lungimea * latimea
print(f"Aria dreptunghiului este: {x}")

'''
 8.Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';

'''
string = 'Coral is either the stupidest animal or the smartest rock.'
print(string.count('the'))

'''
9. Același string:
● Inlocuieste the cu THE peste tot;
● Printează rezultatul.
'''
string = 'Coral is either the stupidest animal or the smartest rock.'
print(string.replace('the', 'THE'))

'''
10. Același string:
● Folosește un assert ca să verifici dacă acest string conține doar numere.

'''
string = 'Coral is either the stupidest animal or the smartest rock.'
assert string.isdigit()

'''
 Exercitii optionale
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''
string = input('string: ')
print(len(string))
print(string[len(string)//2]) # afiseaza caracterul din mijloc

'''
Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
string = input('Spune: ')
nume1,nume2 = string.split(' ') # imparte stringul in functie de un caracter
print(nume1) # afisare
print(nume2)

