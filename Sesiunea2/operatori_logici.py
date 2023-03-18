x = True
y = False
print('x and y is', x and y)
print('x or y is', x or y)
print('Not x is', not x )
print('Not y is', not y )

x = 0 or 4   # 'or' va evalua fiecare operand si se opreste la primul care e adevarat --> 0 e fals, se opreste la 4
print(x)
y = 7 or 9
print(y)

z = 7 and 0
print(z)
z = 7 and 5 #merge pana la capat si returneaza 5
print(z)

