# 1.sa se crie un program care citeste de la tastatura numere pana cand se introduce nr. 0
# pentru fiecare nr. introdus se verifica daca este par, iar la final se vor afisa intr-o lista toate nr. pare

# numar = -1
# numere_pare = []
# while numar:  # !=0 nu se mai scrie, se subantelege
#     numar = int(input("Introdu numar:"))
#     if numar % 2 == 0:
#         numere_pare.append(numar)
# print(numere_pare)
# 2. sa se scrie un program care citeste un text de la tastatura si va afisa un dictionar cu toate caracterele
# din text in care cheile vor fi caracterele si valorile, daca caracterul cheie este vocala sau consoana

dct = {}
txt = input("Introdu un text: ")
for char in txt:
    if not char.isalpha(): # distinge string de int
        continue
    char_type = "vocala" if char in "a,e,i,o,u" else "consoana"
    dct[char] = char_type
print(dct)

# 3. sa se scrie un program care citeste  de la tastatura 6 numere si apoi le afiseaza
# pe cele mai mari  decat 9
numbers = []
for _ in range(6) :
    x = int(input("Introdu un numar: "))
    if x > 9:
        numbers.append(x)
print(numbers)

# 4 . sa se scrie un program care citeste de la tastatura litere pana se introduce
#  un caracter care nu-i litera la final va afisa toate literele unice si sortate

litera = set()
while True:
    caracter = input("Introdu un caracter: ")
    if not caracter.isalpha() :
        break
    litera.add(caracter)
lst_litera = list(litera)
lst_litera.sort()
print(lst_litera)
