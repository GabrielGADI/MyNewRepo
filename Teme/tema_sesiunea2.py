# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# if else este o conditie care evalueaza si bifurca in functie de rezultat

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = int(input("Scrieti numarul: "))
if x > 0:
    print("Numar natural")
else:
    print("Nu este numar natural")

# 3.Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = int(input("Scrieti numarul dorit: "))
if x > 0:
    print("Numar pozitiv")
elif x < 0:
    print("Numar negativ")
else:
    print("Numar neutru")

# 4.Verifică și afișează dacă x este între -2 și 13.
x = int(input("Scrieti numarul (intre -2,13) : "))
if -2 < x < 13:
    print("Este cuprins. ")
else:
    print("Nu este cuprins. ")

# 5.Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input("x: "))
y = int(input("y: "))
if x - y < 5:
    print("Diferenta mai mica decat: 5.")
else:
    print("Diferenta mai mare decat: 5.")

# 6.Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
x = int(input("Scrieti numarul(intre 5, 27): "))
if not(5 < x < 27):
    print("Nu este cuprins. ")
else:
    print("Este cuprins")

'''
7.x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''
x = int(input("x: "))
y = int(input("y: "))
if x == y:
    print('Egalitate')
if x > y:
    print(f"{x} este mai mare decat {y}")
else:
    print(f"{y} este mai mare decat {x}")

'''
 8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
x = int(input("Latura x este: "))
y = int(input("Latura y este: "))
z = int(input("Latura z este: "))
egalitate = [x == y, x == z, y == z]
if all(egalitate):
    print("Triunghi echilateral.")
elif any(egalitate):
    print("Triunghi isoscel. ")
else:
    print("Triunghi oarecare.")

# 9.Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu.
x = str(input("Litera: "))
vocale = [x == "a", x == "e", x == "i", x == "o", x == "u", x == "ă", x == "î", x == "â"]
if any(vocale):
    print(f"'{x}' este o vocala.")
else:
    print(f"'{x}' nu este o vocala.")

# 9.Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu.
x = input("litera: ")
if x in "aeiou":
    print("Este vocala.")
else:
    print("nu e vocala.")

'''
10.Transformă și printează notele din sistem românesc în >
 Peste 9 => A
 Peste 8 => B
 Peste 7 => C
 Peste 6 => D
 Peste 4 => E
 4 sau sub => F
'''
nota = int(input("scrie o nota: "))
if nota > 9 :
    print("A")
elif nota > 8:
    print("B")
elif nota > 7:
    print("C")
elif nota > 6:
    print("D")
elif nota > 4:
    print("E")
else:
    print("F")