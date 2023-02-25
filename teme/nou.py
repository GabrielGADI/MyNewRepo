x = 'hello world'
print(x[2:5]) # de la 2 pana la 5(fara 5)
print(x[:5]) # de la inceput pana la 5(fara 5)
print(x[2:]) # de la caracterul al 2-lea pana la final
print(x[5:-2]) # indexare negativa
print(x[-1:-5:-1]) # indexare in sens invers

nume = 'alabala, portocala'
prim = nume[0] # stocare prima litera din variabila
ultim = nume[-1]
nume = nume[1:-1] #al doilea element si penultimul
prim_val = prim.upper
print(nume)
nume = f'{prim}{nume}{ultim}'
print(nume)
