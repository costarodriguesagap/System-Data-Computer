# lista2 = [v for v in range(300_000_000)]
# for i in lista2:
#     print(i)
#     break

# lista2 = (v for v in range(300_000_000))
# for i in lista2:
#     print(i)

def a(limite=10):
    n = 0
    while True:
        if n < limite:
            n += 1
            yield n

def pares(limite=10):
    n = 2
    while True:
        yield n
        n += 2
        if n > limite:
            # Se não colocar o return, quando chamar a função 
            # novamente, nao vai reiniciar os dados da função, 
            # ou seja, nao liberta o yield 
            return 

def impares(limite=10):
    n = 1
    while True:
        yield n
        n += 2
        if n > limite:
            # Se não colocar o return, quando chamar a função 
            # novamente, nao vai reiniciar os dados da função, 
            # ou seja, nao liberta o yield 
            return 
        
def currente(g1,g2):
    yield from g1
    yield from g2

# for i in currente(impares(),pares()):
#     print(i)
a = currente(impares(),pares())
print(next(a))
print(next(a))
print(next(a))
print(next(a))