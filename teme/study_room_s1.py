# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - inlocuieste 'the cu 'THE'
# - afișează de câte ori apare cuvântul 'the';
x = 'Coral is either the stupidest animal or the smartest rock'
print(x.replace('the' , 'THE'))
print(x.count('the'))

# Folosește un assert ca să verifici dacă acest string conține doar numere.
# assert x.isdigit()

# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.
nume = 'alabala, portocala'
prim = nume[0] # stocare prima litera din variabila
ultim = nume[-1]
nume = nume[1:-1] #al doilea element si penultimul
prim_val = prim.upper()
print(nume)
nume = prim[0] + nume[1:-1].replace(prim, prim_val) + ultim[-1]
print(nume)

the_string = input("Introduceti un string: ")
first_character = the_string[0]
the_string = the_string[0] + the_string[1:-1].replace(first_character, first_character.upper()) + the_string[-1]
print(the_string)

'''
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
 afișeze corect.
 eg: parola abc => ***
 parola abcd => ****
'''
user = input('User name: ')
parola = input('Parola :')
size_parola = len(parola)
hide = '*' * size_parola
print(hide)
print(f'Parola pentru user {user} este {hide} si are {size_parola} caractere' )

# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
string = input('string: ')
print(len(string))
print(string[len(string)//2]) # impartim la 2  slice

'''
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
 '''
string = input('Spune 2: ')
nume1,nume2 = string.split(' ') # imparte stringul in functie de un caracter
print(nume1) # afisare
print(nume2)
