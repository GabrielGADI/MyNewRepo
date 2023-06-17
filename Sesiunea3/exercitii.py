'''
sa se scrie un program care citeste de la tastatura si afiseaza o lista cu  fiecare caracter cu ordinea inversa
'''
text = input("introdu text")
text = text[::-1]
l = list(text)
print(l)

# 2. fie seturile s1, s2
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}
# a. sa se afiseze toate elementele care apar in set 1 si nu apara in set2
# b. --|| toate elementele care apar in ambele seturi
# c. --|| toate elementele care nu sunt comune in ambele seturi

# a.
print(set1.differenece(set2))
print(set1 - set2)

# b.
print(set1.intersection(set2))
print(set1 & set2)

# c.
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
