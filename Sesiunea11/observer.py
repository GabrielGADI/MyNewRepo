'''
Observer - un sablon comportamental care permite definirea unui mecanism de subscriptie pentru a notifica
mai multe obiecte despre evenimente care se intampla asupra obiectelor pe care le observa.
'''

from abc import ABC, abstractmethod


class Observer(ABC):  # cel care va fi modificat
    @abstractmethod
    def update(self):
        pass


class Observable(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Subject(Observable):  # cel la care ne uitam
    _observers = []

    def __init__(self, message):
        self.__message = message

    @property
    def message(self, ):
        return self.__message

    @message.setter
    def message(self, msg):
        self.__message = msg
        self.notify()

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observ in self._observers:
            observ.update(self)


class RealObserverA(Observer):
    def update(self, observable):
        if observable.message.startswith("a"):
            print("Observer a fost notificat")


class RealObserverB(Observer):
    def update(self, observable):
        if observable.message.startswith("b"):
            print("Observer b fost notificat")


a = RealObserverA()
b = RealObserverB()

s = Subject("Salut")
s.register_observer(a)
s.register_observer(b)
s.message = "ana are mere"


'''
Avantaje:
    - poti stabili relatii intre obiecte in momentul rularii codului
Dezavantaje:
    - subscriberii sunt notificati in ordine aleatoare
'''