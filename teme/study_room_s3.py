'''1.Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișează zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add("luni")
print(zile_sapt)

'''
2.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''
if weekend.issubset(zile_sapt):
    print("Yes weekend is a subset of zile_sapt")
else:
    print("No weekend is not a subset of zile_sapt")

# 3. Afișează diferențele dintre aceste 2 seturi.
diferenta = zile_sapt.difference(weekend)
print(diferenta)
print(zile_sapt -weekend)

print(f"Diferenta dintre 'zile_sapt' si 'weekend' este: {zile_sapt.difference(weekend)}")
print(f"Diferenta dintre 'weekend' si 'zile_sapt' este: {weekend.difference(zile_sapt)}")

# 4. Afișează intersecția elementelor din aceste 2 seturi.
intersection = zile_sapt.intersection(weekend)
print(intersection)
print(zile_sapt & weekend)
print(f"Intersectia elementelor dintre seturi este: {zile_sapt.intersection(weekend)}")


#Ex 1

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add("luni")
print(zile_sapt)

# Ex 2

if weekend.issubset(zile_sapt):
    print("Yes weekend is a subset of zile_sapt")
else:
    print("No weekend is not a subset of zile_sapt")

# Ex 3

print(f"Diferenta dintre 'zile_sapt' si 'weekend' este: {zile_sapt.difference(weekend)}")
print(f"Diferenta dintre 'weekend' si 'zile_sapt' este: {weekend.difference(zile_sapt)}")
