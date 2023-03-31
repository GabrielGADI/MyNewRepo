'''
Api-irile(aplication programing interface) permit aplicatiilor software sa comunice intre ele
Actioneaza ca un mediator intre 2 aplicatii permitand uneia sa solicite date sau servicii de la alta si sa
primeasca un raspuns in schimb.
'''

# Rest introduction
'''
Rest(representational state transfer) - un stil arhitectural pentru furnizarea de standarde intre sistemele web
facilitand comunicarea acestora.
Sistemele compatibile REST, numite si restful se caracterizeaza prin faptul ca nu au stare(state) si separa clientul
de server.
Pentru ca un api sa fie restful trebuie sa respecte urmatoarele constrangeri:
1.arhitectura client server : clientul si serverul sunt separate si actioneaza independent permitand utilizarea mai 
multor tehnologii pentru fiecare.
2.Stateless : serverul nu stocheaza nici un context intre cereri(request) astfel incat fiecare cerere contine toate 
informatiile necesare pentru a o finaliza.
3.Capacitatea de cache: clientii pot stoca in cache datele de raspuns reducand numarul de solicitari catre server si
astfel imbunatatind performanta.
4.Utilizarea metodelor HTTP : api-urile restful utilizeaza metode http standare(GET, POST, PUT, DELETE) pentru a
interactia cu resurse unde fiecare metoda reprezinta o actiune specifica(de ex GET reia date si POST creaza o noua resursa)
5.Utilizarea codurilor de stare HTTP - folosirea codurilor specifice HTTP cum ar fi:
- 200 - succes
- 400 (esec)
- 404 (negasit/not found)
'''

# HTTP methods - metode HTTP

'''
Metodele HTTP sunt verbele standard utilizate pentru a utiliza o actiune dorita care trebuie efectuata pe o resursa  
dintr-un API.
Cele 4 metode HTTP principale sunt:
1) GET: preia date dintr-o resursa si este folosit pentru citire
2) POST: creeaza o noua resursa si este folosit pentru a trimite date catre un server
3) PUT: actualizeaza o resursa curenta si este folosit pentru a modifica datele existente
4) DELETE: sterge o resursa si este folosit pentru a elimina date
'''
