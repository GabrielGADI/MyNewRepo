'''
listele sunt utilizate pentru a stoca mai multe valori (colectie) intr-o singura variabila
listele sunt modificabile, ordonate si permit valori duplicate
listele sunt indexabile
cand se adauga un element in lista acesta se va adauga la final
'''

# create
fruits = ["apple", "banane", "cherry"]  # parantezele drepte definesc o lista
numbers = [3, 1, 2, 3, 4, 5]
cars = list(("bmw", "audi", "tesla"))
print(type(numbers))
print(len(fruits))

# indexing
print(20 * " - ", "indexing", 20 * " - ")

print(numbers[0])
print(numbers[-1])  # de la 0 la -1
print(numbers[::2])  # doar numere pare pasul (cate elemente sare la o parcurgere)
print(numbers[1:-1:2])  # [-1] inseamna final

# index prin inversare
print(numbers[::-1])

# insert (adaugare alt element)

print(20 * " - ", "add element", 20 * " - ")
numbers.append(10)
print(numbers)
numbers.insert(0, 10)  # indexare element intr-o anumita locatie
print(numbers)

# remove element (elimina element)

print(20 * " - ", "remove element", 20 * " - ")
elem = numbers.pop()  # elimina de la final
print(elem)
print(numbers)
elem2 = numbers.pop(0)  # elimina de la elementul specificat
print(elem2)
print(numbers)
numbers.remove(3)  # elimina prima aparitie a valorii date
print(numbers)

# clear (sterge toate elementele din lista)
numbers.clear
print(numbers)
numbers = [3, 4, 5, 6, 7, 9]

# replace element (inlocuieste)

print(20 * " - ", "replace element", 20 * " - ")

fruits = ["apple", "banane", "cherry"]
print(fruits)
fruits[1] = "pear"
print(fruits)

# count (numara de cate ori)

print(20 * " - ", "count element", 20 * " - ")

print(numbers.count(3))

# add 2 lists (uneste 2 liste)

print(20 * " - ", "add 2 lists", 20 * " - ")
numbers1 = [1, 3, 6, 7, 8]
print(numbers + numbers1)  # creeaza o lista noua
numbers.extend(numbers1)  # modifica lista initiala
print(numbers)

# reverse (inverseaza ordinea)

print(20 * " - ", "reverse", 20 * " - ")
print(fruits[::-1])  # nu modifica list initiala
print(fruits)
fruits.reverse()  # inplace(pe loc) modifica lista initiala
print(fruits)

# sort

print(20 * " - ", "sort", 20 * " - ")
numbers.sort()  # modifica lista initiala inplace
print(numbers)
numbers.sort(reverse=True)
print(numbers)
