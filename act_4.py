# Apartado 1

import pdb
pdb.set_trace()

def mayor(lista):
    nueva = [max(i) for i in lista]
    print(nueva)
    return nueva

mayor([[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]])



# Apartado 2

def primo(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True 

lista = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(primo, lista))
print(primos)