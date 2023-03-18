'''1. Sa se scrie un program de la tastatura si afiseaza doar
primele 3 caracter diferite de spatiu primite
'''
a = input('Text: ')
a = a.replace('', '')
print(a[:3])

'''2. Sa se scrie un program de la tastatura si afiseaza urmatoarele;
a.numarul de litere a textului introdus
b.prima si ultima litera
c. textul doar scris cu litere mari
d. de cate ori apare prima litere
e. cate cuvinte are textul'''

b = input("Text: ")
print(f"a. {len(b)}")
print(f"b. {b[0]} {b[-1]}")
print(f"c. {b.upper()}")
print(f"d. {b.count(b[0])}")
print(f"e. {b.count(' ') + 1}")
