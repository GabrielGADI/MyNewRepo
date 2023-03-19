'''
1.Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.

'''
import functools
import timeit
import time


def measure_time(unit="s"):
    def decorator_measure_time(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000 if unit == "ms" else end_time - start_time
            print(f"Function {func.__name__} executed in {elapsed_time:.5f} {unit}")
            return result

        return wrapper

    return decorator_measure_time


@measure_time(unit="s")
def real_time():
    print("This is elapsed!")


real_time()

print(real_time())

'''
2. Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator. 
Comparati diferenta de timp necesara generarii.
'''

'''
 - generam numere prime pana la n si verfificam daca fiecare numar este prim.
 - pentru aceasta creeam o lista goala
'''


def get_primes_list(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            if len(primes) == 100:
                break
    return primes


'''
 - vom genera elemente separate ca si generator pentru primele 100 numere prime
 - returneaza fiecare numar prim individual prin intermediul cuvant cheia yield
'''


def get_primes_generator(n):
    count = 0
    for num in range(2, n + 1):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        if is_prime:
            count += 1
            if count <= 100:
                yield num
            else:
                break


'''
- folosim modulul tiemit pentru a compara diferenta de timp intre cele 2 abordari
- utilizand functia lambda si cuvantul cheie 'number-1' se va executa fiecare functie 
exact o data si va masura timpul necesar.
'''

n = 1000

list_time = timeit.timeit(lambda: get_primes_list(n), number=1)
generator_time = timeit.timeit(lambda: list(get_primes_generator(n)), number=1)

print(f"Time taken to generate the first 100 primes using lists: {list_time:.6f} seconds")
print(f"Time taken to generate the first 100 primes using a generator: {generator_time:.6f} seconds")

'''
3.Scrieti un decorator care primeste ca argument numele unui fisier si pentru orice functie apelata,
el va scrie in acel fisier numele functiei, lista de argumente ca si string si rezultatul apelului.
Fisierul este de tip csv. Functiile decorate pot primi oricate argumente
'''

import csv


def log_result_to_csv(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_name, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                result = func(*args, **kwargs)
                func_args = ", ".join([repr(arg) for arg in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
                csv_writer.writerow([func.__name__, func_args, result])
                return result

        return wrapper

    return decorator


@log_result_to_csv('results.csv')
def my_function(x, y):
    return x + y


with open('results.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
