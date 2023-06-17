def say_hi():
    return ("HEllo!")  # return opreste executia functiei, dupa el nu se mai afiseaza
    print("Salut!")


a = say_hi()
print(a)


# fara return nu apare nimic
def print_first50():
    for i in range(50):
        print(i)
    # return None s
    # return


# print_first50 are valoare implicit none sau se poate specifica explicit cu cele 2 variante de mai sus
# (ele sunt echivalente)

b = print_first50()
print(b)


def iterare():
    for i in range(5):
        return i  # return 0 pentru ca este dedesubtp i


print(iterare())


def doar_daca():
    if False:
        return 1  # in caz True va da return 1
    print("Nu e False")


print(doar_daca())
