'''
1. Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''
a = str(input("scrie:"))
assert  a[0] == a[-1], "diferite"

'''
2. Având stringul '0123456789'
● Afișează doar numerele pare
● Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
'''
a = input('Un numar:')
a = '0123456789'
if a[0::2]:
    print('Este par')
elif a[0::1]:
    print('Este impar')

#Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
#
my_str = str(input("enter string:"))
my_str = my_str.lower()
# assert  my_str[0] == my_str[-1], "not the same"


# Având stringul '0123456789'
# ● Afișează doar numerele pare
# ● Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)

str1 = "0123456789"
print(f"numerele pare sunt {str1[0::2]}")
print(f"numere impare sunt {str1[1::2]}")