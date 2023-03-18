import datetime
import functools

# Decoratorul are 3 concepte: functie ca parametru, functie in interior, return functie(wrapper)
def my_decorator(func): # functie ca parametru
    def wrapper(): #functie in interior
        print("Before func")
        func() # apelare functie
        print("After func")
    return wrapper # return functie
    # return wrapper() - returneaza rezultatul functiei

@my_decorator # numele functiei decorator
def say_hi():
    print("Hi")

say_hi()


# Exercitiu: un decorator care executa functiile decorate doar pe timpul zilei

def not_during_the_night(func):
    @functools.wraps(func)
    def wrapper():
        if  8 <= datetime.date.time.now().hour < 21 :
            func()
        else:
            pass
    return wrapper


@not_during_the_night
def say_hello():
    print("Hello!")

say_hello

print(say_hello)