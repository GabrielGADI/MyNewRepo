# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex 1. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă

nr = int(input("Alege un nr: "))

for i in range(1,nr+1):
    print(f"{i}" * i)

print(40 * "*")

# Ex 2 Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in tastatura_telefon:
    for j in i:
        print(f"Cifra curentă este {j}")