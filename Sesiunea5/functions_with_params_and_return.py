def product(a, b):
    return (a * b)


p = product(3, 2)
p2 = product(8, 5)
print(p)
print(p2)


def get_all_even_numbers(numbers):
    numere_pare = []
    for number in numbers:
        if number % 2 == 0:
            numere_pare.append(number)
    return numere_pare


all_even = get_all_even_numbers([2, 3, 5, 7])
print(all_even)
