# 1. lungime
name = 'Dragos'
print(len(name))

# 2. majuscule
name = 'Dragos'
print(name.upper())  # transforma litere mici in majuscule

# 3  litere mici
name = 'Dragos'
print(name.lower())  # transforma toate litere in mici

# 4.  Numarare
name = 'anamaria'
print(name.count('a'))  # numarul de aparitii a caracterului in string
print(name.count('i'))

# 5. replace
name = 'Anamaria'
name = name.replace('a', 'b')  # toate aparitiile caracterului 'a' au fost inlocuite cu 'b'
print(name)

food = 'pizza'
print(food.replace('zz', 't'))

name = 'anamaria'
print(name.replace('a', 'b', 2))  # inlocuieste de 2 ori caracterul 'a' cu caracterul 'b'

# 6. indedx
name = 'John'
print(name.index('0'))  # arata pe ce locatie este, se incepe de la 0
print(name[0])
print(name[-1])
print(name[len(name) - 1])

# 7.Sliceing
b = 'hello World'
print(b[2:5])  # de la 2 la 5(fara 5)
print(b[:5])  # se ia de la inceput pana la 5 (fara 5)
print(b[2:])  # de la caracterul al doliea pana la final

# 8.indexare negativa
print(b[-5:-2])  # se ia tot de la final incepand
