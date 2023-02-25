# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex 1
'''
1.Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
'''


class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        # del self.todo[nume]
        self.todo.pop(nume)

    def afișează_todo_list(self):
        li = []
        # li2 = []

        for k in self.todo.keys():
            li.append(k)
        print(li)
        # for k, v in self.todo.items():
        #     li2.append((k, v))
        # print(li2)

    def afișează_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.values():
            check = input("Vreti sa adaugati acest task in lista personala ? Y / N ").lower()
            if check == "n":
                print("ok, nu adaugam nimic")
            elif check == "y":
                detalii = input("Detalii ? ")
                self.todo[nume_task] = detalii


my_list = TodoList()
my_list.adauga_task("invatat python", "Mihai")
my_list.adauga_task("invatat C#", "Alex")
my_list.adauga_task("Desen tehnic", "Ion")
my_list.finalizeaza_task("Desen tehnic")
my_list.afișează_todo_list()
my_list.afișează_detalii_suplimentare("Desen tehnic")
my_list.afișează_todo_list()
