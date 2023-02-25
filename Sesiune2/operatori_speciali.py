# 1. operatori de identitate
x1 = 5
y1= 5
x2= 'hello'
y2= 'hello'
x3=[1,2,3]
y3=[1,2,3]
print(x1 is y1) # pentru tipurile de date primitive se va face egalitate la valoare
print(x1 is not y1)
print(x3 is y3) # pentru tipurile de date primitive va verifica locatia din memorie de aceea x3 nu e la fel y3
print(x3 is x3)
print("#" * 50)

# 2. operator de apartenenta
x = 'hello'
y = [1,2,3]
print("h" in x)  # 'h' exista in x
print("llo" in x)
print(4 not  in y )
print([2,3] in y) # nu verifica ce este in lista

# 3. functiile all si any
print("#"*50)
print(all([1,2,'a', None, -7]))
print(all([1,2,'a', 'v', -7]))
print("#"*50)
print(any([0, None, " ", [], 1]))
