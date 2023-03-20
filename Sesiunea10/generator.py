# yield
#iterabil folosit in cadrul unei functii
def func():
    print("before yield")
    yield 10 # revine in functie si continua sa gaseasca urmatorul( deschide si inchide)
    print("after yield")

#i = func()
#print(next(i)) # va afisa dupa primul print si va continua daca se va repeta print(next(i))


def even_generator(n):
    generated_nrs = 0
    nr = 0
    while generated_nrs < n:
        nr += 1
        if nr % 2 == 0:
            yield nr
            generated_nrs += 1

gen = even_generator(10)
for i in gen:
    print(i)
