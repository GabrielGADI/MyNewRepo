# Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
# nevoie de Google).

# Ex 1

impar = "abcdefg"
print(f"{impar[int((len(impar) - 1) / 2)]}")
print(f"{impar[(len(impar) - 1) // 2]}")

# Ex2

ala1 = "alabala portocala"
cuv1, cuv2 = ala1.split(" ")
print(cuv1)
print(cuv2)

# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

# Ex1
'''
1. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
ala2 = "alabala portocala"
ala2_prim = ala2[0]
ala2_ult = ala2[-1]
ala2_UP = ala2_prim.upper()
ala2 = ala2[1:-1]
ala2 = ala2.replace(ala2_prim, ala2_UP)
ala2 = f"{ala2_prim}{ala2}{ala2_ult}"
print(ala2)

# Ex2

user = input("User: ")
passw = input("Pass: ")
secret_pass = len(passw) * "*"

print(f"Parola pt user {user} este {secret_pass} și are {len(passw)} caractere")
