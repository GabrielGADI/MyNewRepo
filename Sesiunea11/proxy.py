'''
proxy - un sablon structural care permite inlocuirea unui obiect din aplicatie.
Un proxy controleaza accesul catre obiectul original, permitand un set de operatii
inainte sau dupa ce apelul ajunge catre functia original.
'''

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("Ne ocupam de request!")

class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject
    def request(self):
        if self.check_acces():
            self.real_subject.request()
            self.log_request()

    def check_acces(self):
        print("Proxy: checking acces!")
        return True # ca sa treaca if

    def log_request(self):
        print("Request finish")



rs = RealSubject()

rs.request()
print("*" * 50)
proxy = Proxy(rs)
proxy.request()

'''
Avantaje:
    - poti controla obiectul original fara ca apelantul sa stie ce se intampla de fapt
    - poti controla ciclul de viata al subiectului real 
    - obiectul proxy functioneaza chiar si atunci cand cel original nu functioneaza
Dezavantaje:
    - codul poate deveni mai complicat deoarece se introduc mai multe clase
    _ raspunsul din partea obiectului original ar putea fi intarziat 
'''