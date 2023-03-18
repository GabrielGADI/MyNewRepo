'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o.
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
'''
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
note1 = note_muzicale[::-1]
print(note1)


# 2. De câte ori apare ‘do’?
print(note_muzicale.count("do"))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
liste1 = [3, 1, 0, 2]
liste2 = [6, 5, 4]
print(liste1 + liste2)
liste1.extend(liste2)
print(liste1)

''' 4.
● Sortează și afișează lista generată la exercițiul anterior.
● Stergeti numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
liste1.sort()
print(liste1)
liste1.remove(0)
print(liste1)

'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
● Lista este goală.
● Lista nu este goală.
'''

if len(liste1) == 0:
    print("lista este goala")
else:
    print("lista nu este goala")

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
liste1.clear()
print(liste1)

'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''
if len(liste1) ==0 :
    print("lista este goala")
else:
    print("lista nu este goala")


'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5
         }
print(list(dict1.keys()))

'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
print(f"Ana a luat nota: {dict1['Ana']}")
print(f"Gigel a luat nota: {dict1['Gigel']} ")
print(f"Dorel a luat nota: {dict1['Dorel']}")

'''
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
dict1['Dorel'] = 6 # suprascriere
dict1.update({'Dorel':6})
print(dict1)

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
dict1.pop('Gigel')
print(dict1)
dict1.setdefault('Ionica', 9)
print(dict1)
print(dict1.keys())