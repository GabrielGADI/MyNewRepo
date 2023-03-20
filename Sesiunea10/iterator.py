# iterabil folosit in cadrul unei clase
# trebuiesc implementate 2 functii iter si next
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.generated_nrs = 0 # cate numere a dat
        self.nr = 0 # numarul de la care incepem

    def __iter__(self):
        return self
# mecanism de iterare
    def __next__(self):
        self.nr += 1 # incepem cu cate 1
        if self.generated_nrs >= self.n:
            raise StopIteration # cand termina afiseaza eroarea
        elif self.nr % 2 == 0: # daca este par
            self.generated_nrs += 1 # cand gasim un numar
            return self.nr # afisare
        return self.__next__() # apelare direct functia next daca nu gaseste niciuna din cele de mai sus


it = EvenIterator(10) # apelare iterator metodata 'for'
for i in it:
    print(i)

it = EvenIterator(10) # apelare iterator 'while' ,'True'
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break # iese din bucla infinita 'While' 'True'