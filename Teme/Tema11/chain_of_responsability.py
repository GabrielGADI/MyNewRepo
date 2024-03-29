'''
a. La ce este folosit?

Chain of Responsibility(CoR, Chain of Command) - un model de design comportamental care ne permite să transmitem
cereri de-a lungul unui lanț de gestionari. La primirea unei cereri, fiecare handler decide fie să proceseze cererea,
fie să o transmită următorului handler din lanț.

Modelul Chain of Responsability - un model de design comportamental care se utilizeaza atunci când se așteaptă ca programul
nostru să proceseze diferite tipuri de solicitări în diferite moduri, dar tipurile exacte de solicitări și secvențele
lor sunt necunoscute în prealabil.

'''

'''
b. PROS & CONS

PROS:
    - puteți controla ordinea procesării cererilor.
    - principiul responsabilității unice. 
    - puteți decupla clasele care invocă operații de clasele care efectuează operații.
    - principiul deschis/închis. 
    - puteți introduce noi handleri în aplicație fără a rupe codul client existent.

CONS:
    - unele solicitări pot ajunge nerezolvate.
'''

'''
c. Exemplu cod (template, nu neaparat exemplu din viata reala)
'''


class Handler:
    def __init__(self):
        self.successor = None

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        else:
            return None


class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == 'request 1':
            return 'Handled by concrete handler 1'
        else:
            return super().handle(request)


class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == 'request 2':
            return 'Handled by concrete handler 2'
        else:
            return super().handle(request)


class ConcreteHandler3(Handler):
    def handle(self, request):
        if request == 'request 3':
            return 'Handled by concrete handler 3'
        else:
            return super().handle(request)


if __name__ == '__main__':
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()
    handler1.successor = handler2
    handler2.successor = handler3

    print(handler1.handle('request 1'))
    print(handler1.handle('request 2'))
    print(handler1.handle('request 3'))
    print(handler1.handle('unknown request'))

'''
d. (Optionala) O descriere a unde ar putea fi folosit in viata reala (nu neaparat exemplu legat de IT)

   Un complex hotelier care se ocupa cu rezervari: telefonic sau online si care pune la dispozitie clientilor, 
conform cerintelor acestora, servicii diverse. Este o implicare in lant incepand de la cameriste - care se ocupa cu
aranjarea camerelor -  coordonate de o sefa de tura care este in stransa legatura cu receptionerii; receptionerii - 
supervizati de sef de tura care este in subordinea managerului de departament; entertainerii - coordonati de 
receptioneri care le aduc la cunostinta orele cand trebuie sa creeze atmosfera de voie buna; bucatarii, ajutorii de 
bucatari - coordonati de seful bucatar; ospatarii si picolii - coordonati de seful de tura la indrumarea managerului 
restaurant care este in stransa legatura cu seful bucatar, paza - asigura siguranta clientilor, si bineinteles Managerul
hotelului care coordoneaza intreaga activitate.
   Toti poarta o responsabilitate care este strans legata unul fata de celalalt si care in cele din urma va fi rasplatita 
cu un feedback din partea clientului la finalul sejurului acestuia.
   Un complex hotelier poate fi considerat un Chain Of Responsability.
'''
