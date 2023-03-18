# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google

# Ex 1
'''
1. Clasa Factură
Atribute: seria (va fi constantă, nu trebuie constructor, toate
facturile vor avea aceeași serie), număr, nume_produs, cantitate,
pret_buc
Constructor: toate atributele, fără serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pentru dată:
https://www.geeksforgeeks.org/get-current-date-using-python/
'''
class Factura:
    seria = 5478

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.nr = numar
        self.nume_prod = nume_produs
        self.cant = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cant):
        self.cant = cant

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_prod = nume

    def genereaza_factura(self):
        # print(f"Factura seria {self.seria} numar {self.nr}")
        # print(f"Data: {date.today()}")
        # print(f"{self.nume_prod} | cantitate | pret bucata | Total")
        # print(f"0746 098 769 | {self.cant : ^9} | {self.pret_buc : ^9} | {self.cant * self.pret_buc : >9}")

        print(f"Factura seria {self.seria} numar {self.nr}\n"
              f"Data: {date.today()}\n"
              f"{self.nume_prod} | cantitate | pret bucata | Total\n"
              f"0746 098 769 | {self.cant : ^9} | {self.pret_buc : ^9} | {self.cant * self.pret_buc : >9}")


fact = Factura(1, "Cascaval", 1, 100)
fact.genereaza_factura()
fact.schimba_cantitatea(2)
fact.schimba_pretul(150)
fact.schimba_nume_produs("Miere")
fact.genereaza_factura()


# Ex 2
'''
Clasa Mașină
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori
disponibile (set), înmatriculată (bool)
Culoare = gri - toate mașinile când ies din fabrică sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
Culori disponibile = alege tu 5-7 culori
Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e
negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
'''
class Masina:
    marca = "BMW"
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"Albastru", "Verde", "Negru", "Rosu", "Gri Metalizat", "Galben"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.max = viteza_maxima

    def descrie(self):
        matr = None
        if self.inmatriculata == True:
            matr = "Da"
        else:
            matr = "Nu"
        print(
            f"Marca {self.marca} - viteza {self.viteza_actuala} - culoare {self.culoare} - inmatriculare - {self.inmatriculata}")

        print(f"Marca {self.marca} - viteza {self.viteza_actuala} - culoare {self.culoare} - inmatriculata - {matr}")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, cul):
        if cul in self.culori_disponibile:
            self.culoare = cul
        else:
            raise "Aceasta culoare nu exista !"

    def accelereaza(self, vit):
        if vit < 0:
            raise "Viteza nu poate scade sub 0"
        elif vit > self.max:
            self.viteza_actuala = self.max
        else:
            self.viteza_actuala = vit

    def franeaza(self):
        self.viteza_actuala = 0


bmw = Masina("X5", 350)
bmw.descrie()
bmw.vopseste("Albastru")
bmw.descrie()
bmw.accelereaza(360)
bmw.descrie()
bmw.franeaza()
bmw.descrie()
