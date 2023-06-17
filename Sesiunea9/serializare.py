# metoda lunga - mod citire
def read(filename):
    f = open(filename, "r")  # "r" - mode deschidere-read
    try:
        return f.readlines()  # mode de afisare
    except:
        print("Error reading file")
    finally:
        f.close()  # este oblogatoriu sa inchidem fisierul


# context manager - folosim metoda scurta - include inchiderea fisierului - mod citire - metoda uzuala
def read_safe(filename):  # mai simplu si corect
    with open(filename, "r") as f:  # with se ocupa de inchiderea fisierului
        return f.readlines()


read("data.txt")
print(read("data.txt"))
print(read_safe("data.txt"))  # apelare metoda context manager


# mod de scriere - nu returneaza nimic - doar scrie
def write(filename, data):  # parametru data - ceea ce scrii in fisier
    with open(filename, "w") as f:  # "w"- metoda de deschidere
        f.writelines(data)


# fisierul supracsris complet, pierzi datele
write("data2.txt", ["abc\n", "123\n", "per\n"])  # data2.txt- fisierul cu lista[...] \n - scriere new line


# mod de adaugare
def append(filename, data):
    with open(filename, "a") as f:  # "a" - metoda de deschidere
        f.writelines(data)


# adaugam noi date la fisier
append("data2.txt", ["14567"])
