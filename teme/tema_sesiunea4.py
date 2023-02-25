print(20 * " - ", "Exercitiul 1", 20 * " - ")
# 1.Având lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

'''
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
'''
for i in range(len(masini)):
    print(f"Masina mea preferata este: {masini[i]}")

# ● Fă același lucru cu un for each.
for masina in masini:
    print(f"Masina mea preferata este: {masina}")

# ● Fă același lucru cu un while.
index = 0
while index < len(masini):
    print(f" Masina mea preferata este :{masini[index]}")
    index += 1

print(20 * " - ", "Exercitiul 2", 20 * " - ")
'''
2. Aceeași listă:
Folosește un for else
'''
for m in masini:
    print(f"Masina mea preferata este:",m)
else:
    print(f"STOP!")

'''În for
- Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
- Printează lista.
'''
masini[:] = [masina.upper() for masina in masini[:]]
print(masini)

print(20 * " - ", "Exercitiul 3", 20 * " - ")
'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
import random

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
while True:
    x = random.choice(masini)
    if x == "Mercedes":
        print("Am gasit masina dorita de dvs.")
        break
    else:
        print(f"Am gasit masina: {x}, mai cautam.")

print(20 * " - ", "Exercitiul 4", 20 * " - ")
'''
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''
for masina in masini:
    if masina in ["Trabant", "Lastun"]:
        continue
    print(f"S-ar putea sa va placa masina: {masina}")

print(20 * " - ", "Exercitiul 5", 20 * " - ")
'''
5. Modernizează parcul de mașini:
  ● Crează o listă goală, masini_vechi.
'''
masini_vechi = []

'''
 ● Iterează prin mașini.
 Când găsesti Lăstun sau Trabant:
 Salvează aceste mașini în masini_vechi.
'''
for item in masini:
    if item in ["Trabant", "Lastun"]:
        masini.remove(item)
        masini_vechi.append(item)

# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
masini.append("Tesla")

# ● Printează Modele vechi: x.
print(f"Modele vechi: {masini_vechi}")

# ● Modele noi: x.
print(f"Modele noi: {masini}")

print(20 * " - ", "Exercitiul 6", 20 * " - ")
# 6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
'''
Vine un client cu un buget de 15000 euro.
● Iterează prin dict.items() și accesează mașina și prețul.
'''

buget = 15000
for k, v in pret_masini.items():
    if v <= buget:
        print(k)

#  Prezintă doar mașinile care se încadrează în acest buget.

for k, v in pret_masini.items():
    if v <= buget:
        print(f"Avem {k} la pretul de {v}e")

# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină x

for k, v in pret_masini.items():
    if v <= buget:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașina: {k}")

print(20 * " - ", "Exercitiul 7", 20 * " - ")
# 7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count)

index = 3
x = 0
for i in numere:
    if i == index:
        x += 1
print(f" Cifra '3' apare de {x} ori")

print(20 * " - ", "Exercitiul 8", 20 * " - ")
'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
s = 0
for i in numere:
    s += i
print(f"Suma numerelor este: {s}")

print(20 * " - ", "Exercitiul 9", 20 * " - ")
'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
m = numere[0]
for i in numere:
    if i > m:
        m = i
print(m)

print(20 * " - ", "Exercitiul 10", 20 * " - ")
'''
 10. Aceeași listă:
  ● Iterează prin ea.
  ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
  Ex: dacă e 3, să devină -3
  ● Afișază noua listă.

'''
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)





