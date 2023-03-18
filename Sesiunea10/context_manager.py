from contextlib import contextmanager
from time import perf_counter, sleep


# La context manager trebuiesc implementate 2 functii enter si exit
# folosind clase
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, value, tr):
        self.file.close()


with FileManager("test.txt", "w") as f:
    f.write("test")


# flosind functii
@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    yield f
    f.close


with file_manager("test.txt", "w") as f:
    f.write("testare finala")


class HelloContextManager:
    def __enter__(self):
        print("Entering the contexting")
        return "Hello World"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Living the context")
        if exc_type == IndexError:
            print(f"Exeption message: {exc_val}")
            return True  # eroarea nu se mai propaga la consola altfel va apare IndexError


with HelloContextManager() as hello:  # 'hello' variabila care-i corespunde lui return "Hello World"
    print(hello)
    print(10)
    hello[100]  # accesam caracterul 100 din stringul 'Hello World" -> string index out of range

'''
 sa se scrie un context manager care sa masoare durata de executie a blocului de cod in interior
'''


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = perf_counter()
        print(self.stop - self.start)


with Timer():
    sleep(3)  # nu face nimic 3 secunde
