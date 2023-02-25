# dictionarele sunt folosite pt a stoca date in perechi de forma key:valoare

# Create

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1990,
}

car2 = dict(brand="Ford", model="Mustang", year=1990)

# Accessing elements

print(20 * "-", "Accessing elements", 20 * "-")

print(car["brand"])
# print(car["is_new"]) # arunca eroare pt ca nu exista aceea cheie in dictionar
print(car.get("is_new"))
print(car.get("is_new", True))

# Add elements

print(20 * "-", "Adding elements", 20 * "-")

car["is_new"] = False
print(car)

v = car.setdefault("is_new", True)
print(car)
print(v)
car.setdefault("price", 7900)
print(car)

# Replace elements

print(20 * "-", "Replacing elements", 20 * "-")

car["price"] = 9700
print(car)
car.update({"price": 10000, "color": "black"})
print(car)

# Remove elements

print(20 * "-", "Removing elements", 20 * "-")

car.pop("is_new")
print(car)

car.popitem()  # elimina ultimul element inserat
print(car)

del car["year"]
print(car)

a = {1: "first", 2: "second"}
a.clear()
print(a)

# All keys

print(20 * "-", "All keys", 20 * "-")

print(car.keys())
print(list(car.keys()))

# All values

print(20 * "-", "All values", 20 * "-")

print(list(car.values()))

# All items

print(20 * "-", "All items", 20 * "-")

print(list(car.items()))

# Length

print(20 * "-", "Length", 20 * "-")

print(len(car))  # numarul de chei