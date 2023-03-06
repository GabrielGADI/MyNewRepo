'''
Sa se scrie o functie care primeste ca parametru un intreg si returneaza:
 - *35 daca numarul este divizibil cu 3 si 5
 - *3 daca numarul este divizibil cu 3
 - *5 daca numarul este divizibil cu 5
'''
def is_div_3_5(n):
    if n % 3 == 0 and n % 5 == 0:
        return 35
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5


'''
Exercitiu
 Sa se scrie o functie care primeste ca parametru o lista si arunca o exceptie 
specifica daca lista contine si altceva decat intregi
'''
class NotInException(Exception):
    pass

def only_ints(lst):
    for elem in lst:
        if not isinstance(elem, int):
            raise NotInException(f"{elem} is not an Int.")