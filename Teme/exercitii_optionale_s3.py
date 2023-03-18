 # Ex optionale - var 1
'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3'''
jucatori = ["Mihai", "Bogdan", "Ionut", "Alin", "Mircea"]
schimbari_max = 3
schimbari_efectuate = 0
jucator = "Mihai"

'''
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișază a intrat x, a ieșit y, mai ai z schimbări
'''
if jucator in jucatori and schimbari_max > 0:
    exit = jucatori.pop(jucatori.index("Mihai"))
    jucatori.append("George")
    enter = jucatori[-1]
    schimbari_max -= 1
    schimbari_efectuate += 1
elif jucator not in jucatori:
    print("nu se poate efectua schimbarea deoarece jucatorul x nu e in teren")

print(f"A intrat {enter} a iesit {exit}, mai sunt {schimbari_max} schimbari")


'''
Dacă jucătorul nu e în teren:
- Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
'''
jucator = "Ion"

if jucator in jucatori and schimbari_max > 0:
    exit = jucatori.pop(jucatori.index("Mihai"))
    jucatori.append("George")
    enter = jucatori[-1]
    schimbari_max -= 1
    schimbari_efectuate += 1
elif jucator not in jucatori:
    print(f"nu se poate efectua schimbarea deoarece jucatorul {jucator} nu e in teren")
    print(f"Mai sunt {schimbari_max} schimbari")



# Ex 1 - Optional - var 2

'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3'''
jucatori = ["Mihai", "Ion", "Gica", "Bogdan", "Alex"]
schimbari_max = 3
schimbari_efectuate = 0

'''
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișază a intrat x, a ieșit y, mai ai z schimbări
'''
jucator = "Mihai"
jucator_nou = "Aurelian"

if jucator in jucatori and schimbari_max > 0:
    jucatori.remove(jucator)
    exit = jucator
    jucatori.append(jucator_nou)
    schimbari_max -= 1
    schimbari_efectuate += 1
    print(f"A intrat {jucator_nou}, a iesit {exit}, mai ai {schimbari_max} schimbari")
elif jucator not in jucatori:
    print(f"nu se poate efectua schimbarea deoarece jucătorul {jucator} nu e în teren")
    print(f"mai ai {schimbari_max} schimbari")

'''
Dacă jucătorul nu e în teren:
- Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
'''
jucator = "Sebi"
jucator_nou = "Mandu"

if jucator in jucatori and schimbari_max > 0:
    jucatori.remove(jucator)
    exit = jucator
    jucatori.append(jucator_nou)
    schimbari_max -= 1
    schimbari_efectuate += 1
    print(f"A intrat {jucator_nou}, a iesit {exit}, mai ai {schimbari_max} schimbari")
elif jucator not in jucatori:
    print(f"nu se poate efectua schimbarea deoarece jucătorul {jucator} nu e în teren")
    print(f"mai ai {schimbari_max} schimbari")