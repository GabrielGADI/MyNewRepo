# seturile sunt folosite pentru a stoca mai multe elemente intr-o singura variabila dar fara duplicate

# create
print(20 * "-", "create", 20 * "-")

fruits = {"apple", "banana", "cherry"}
cars = set()  # set gol

# length
print(20 * "-", "length", 20 * "-")

print(len(fruits))

# add elements

print(20 * "-", "Add elements", 20 * "-")
fruits.add("pear")
tropical = {"mango", "papaya"}
fruits.update(tropical)
print(fruits)
fruits.update(["kiwi", "orange"])
print(fruits)

fruits.add("apple")
print(fruits)  # nu poate avea duplicate

# remove elements
print(20 * "-", "remove", 20 * "-")
fruits.remove("banana")  # elimina in functie de valoare, face operatia intr-un singur apel(colectie mare)
print(fruits)
# fruits.remove("grapes")# arunca eroare pentru ca nu exista elementul
# print(fruits)
fruits.discard("grapes")
print(fruits)
fruits.pop()  # elimina ultimul element inserat
print(fruits)

a = {1, 2, 3}
a.clear()
print(a)

# join
print(20 * "-", "join", 20 * "-")
s1 = {"a", "b", "c"}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)
print(s1 | s2)  # forma prescurtata union

# intersection
print(20 * "-", "intersection", 20 * "-")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
print(x & y)  # forma prescurata de intersection

# difference
print(20 * "-", "difference", 20 * "-")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
print(x - y)  # prescurtare la difference

# symetric difference
print(20 * "-", "symetric difference", 20 * "-")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print(x ^ y)

# issubset si issuperset
print(20 * "-", "issubset si issuperset", 20 * "-")

x = {"a", "b", "c"}
y = {"a", "b", "c", "d", "e", "f"}
print(x.issubset(y))
print(y.issuperset(x))
