'''
1.Clasa Cerc
Atribute: rază, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(self.culoare)
        print(self.raza)

    def arie(self):
        pi = 3.14
        return self.raza ** 2 * pi

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        pi = 3.14
        return 2 * pi * self.raza


c = Cerc(7,"verde")
c.descrie_cerc()
print(c.arie())
print(c.diametru())
print(c.circumferinta())

print(40 * "*")

'''
2. Clasa Dreptunghi
Atribute: lungime, lățime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Poți verifica schimbarea culorii prin apelarea metodei
descrie().
'''


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Acest dreptunghi {self.culoare} are lungimea de {self.lungime} cm si latimea de {self.latime} cm.")

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, culoare1):
        self.culoare = culoare1


d = Dreptunghi(10, 6, 'Verde')
d.descrie()
print(d.aria())
print(d.perimetrul())
d.schimba_culoarea('Portocaliu')
print(d.culoare)

print(40 * "*")

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pentru toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

class Angajat:

    def __init__(self, nume, prenume, salariu, ):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print (f"Salariatul {self.nume} {self.prenume} are un salariu de {self.salariu} lei.")

    def nume_complet(self):
        print(f"Numele salariatului este: {self.nume} {self.prenume}.")

    def salariu_lunar(self):
        print(f"Salariul lunar este: {self.salariu}.")

    def salariu_anual(self):
        print(f"Salariu anual este: {self.salariu * 12}.")

    def marire_salariu(self, procent):
        self.salariu += self.salariu * procent / 100
        # marirea de salariu adaugata in salariu (+=)


a = Angajat("Ion", "Vasile", 10000)
a.descrie()
a.nume_complet()
a.salariu_lunar()
a.salariu_anual()
a.marire_salariu(40)
a.salariu_lunar()

print(40 * "*")

'''
4. Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''


class Cont:
    def __init__(self, iban, titularCont, sold):
        self.iban = iban
        self.titularCont = titularCont
        self.sold = sold

    def salut(self):
        print(f'Buna ziua {self.titularCont}')

    def afisare_sold(self):
        print(f'Titular {self.titularCont} aveti in contul {self.iban} suma de {self.sold} lei.')

    def creditare_cont(self,suma_depusa):
        self.salut()
        self.sold += suma_depusa
        print(f'{self.titularCont} ati alimentat {suma_depusa} lei.')
        print(f'{self.titularCont} aveti in cont {self.sold} lei.')

    def debitare_cont(self, suma_cheltuita):
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f'{self.titularCont} ati cheltuit {suma_cheltuita} lei.')
            print(f'{self.titularCont} aveti in cont {self.sold} lei.')
        else:
            print(f'****Fonduri induficiente.Ne pare rau!')


iv = Cont("Ro0188683793BNR", "Ion Vasile", 9800)
iv.afisare_sold()
iv.debitare_cont(590)
iv.afisare_sold()
iv.creditare_cont(300)
iv.afisare_sold()
iv.creditare_cont(600)
iv.afisare_sold()
iv.debitare_cont(10000)
iv.afisare_sold()
iv.debitare_cont(500)
iv.afisare_sold()

print(40 * "*")