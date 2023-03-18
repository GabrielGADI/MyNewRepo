# 1. Functii ca argument
def say_hello(name):
    return f"Hello {name}"


def say_hi(name):
    return f"Hi {name}"


def greet_Bob(func):
    return func("Bob")

# transmitere functie ca si parametru
print(greet_Bob(say_hi))
print(greet_Bob(say_hello))


# 2. Functii interioare

def parent():
    print("Parent")

    def first_child():
        print("First child")

    def second_child():
        print("Second child")

    second_child()
    first_child()


parent()


# 3. Returnare de functii

def parent(m):
    def first_child():
        return "First child"

    def second_child():
        return "Second Child"

    if m == 1:
        return first_child
    else:
        return second_child


f = parent(1) # va returna "First child"
print(type(f))
print(f())
f  = parent(2) # va returna "Second Child"
print(f())