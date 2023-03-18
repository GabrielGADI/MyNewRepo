# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google

# Ex 1. Funcție care primește o lună din an și returnează câte zile are acea lună.

def zile_luna(a):
    ian = 31
    feb = 28
    mar = 31
    apr = 30
    mai = 31
    iun = 30
    iul = 31
    aug = 31
    sep = 30
    oct = 31
    noi = 30
    dec = 31

    if a == "ian":
        return ian
    elif a == "feb":
        return feb
    elif a == "mar":
        return mar
    elif a == "apr":
        return apr
    elif a == "mai":
        return mai
    elif a == "iun":
        return iun
    elif a == "iul":
        return iul
    elif a == "aug":
        return aug
    elif a == "sep":
        return sep
    elif a == "oct":
        return oct
    elif a == "noi":
        return noi
    elif a == "dec":
        return dec

'''
from calendar import monthrange
from datetime import datetime

def month_days_number(month):
    year = datetime.today().year
    return monthrange(year, month)[1]
    
print(month_days_number(9))
'''

print(zile_luna("mar"))


# Ex 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
'''În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)

● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''
def ops(a, b):
    summ = a + b
    dif = a - b
    prod = a * b
    div = a / b

    return summ, dif, prod, div


x, y, z, u = ops(3, 4)

print(f"Suma: {x}")
print(f"Diferenta: {y}")
print(f"Inmultirea: {z}")
print(f"Impartirea: {u}")

'''
def calculator(x, y):
    return x+y, x-y, x*y, x/y

a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
'''

# Ex 3. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def frequency(a):
    dct = {}

    for i in a:
        dct[i] = a.count(i)

    return dct


print(frequency([0, 0, 1, 2, 4, 4, 4, 5, 0]))

'''
# v1
def digits_count_v1(digits):
    dct = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for d in digits:
        dct[d] += 1
    
    return dct

print(digits_count_v1([1, 3, 1, 5, 9, 7, 7, 5, 5]))


# v2
def digits_count_v2(digits):
    dct = {}
    for d in digits:
        if d in dct:  
            dct[d] += 1
        else:
            dct[d] = 1
    return dct

print(digits_count_v2([1, 3, 1, 5, 9, 7, 7, 5, 5]))
'''

# Ex 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.

def maxim(a, b, c):
    return max(a, b, c)


print(maxim(1, 2, 3))

'''
def maximum(x, y, z):
    return max(x, y, z)

print(maximum(5, 3, 7))
'''

# Ex 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

def summ_all(a):
    s = 0

    for i in range(a + 1):
        s += i

    return s


print(summ_all(5))

'''
def sum_til_nr(nr):
    s = 0
    for x in range(nr+1):
        s += x
    return s

print(sum_til_nr(3))
'''

# Exerciții Opționale - Bonus

# Ex 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune.
#
# Exemplu:
# list1 = [1, 1, 2, 3]
#
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

def intersect(a, b):
    return set(a) & set(b)


print(intersect([1, 1, 2, 2, 3], [2, 3, 3, 4, 5, ]))

'''
def common_numbers(lst1, lst2):
    return set(lst1) & set(lst2)

print(common_numbers([1, 1, 2, 3],[2, 2, 3, 4]))
'''

# Ex 2. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110%
# e invalidă.

def reduct(a, red):
    if 0 < red < 100:
        final = a - red / 100 * a
        return int(final)
    else:
        final = f"Invalid discount"
        return final


print(reduct(1000, 15))

'''
def discount(price, discount_percent=10):
    if 0 <= discount_percent <= 100
        return price - price * discount_percent/100
    print("Reducerea aplicata nu este valida")
        
print(discount(100, 50))
print(discount(100))
'''