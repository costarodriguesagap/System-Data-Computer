lista2 = [v+1 for v in range(10)]
print(lista2)
lista2 = [(v,w) for v in [1,2,3] for w in [4,5,6]]
print(lista2)
lista2 = [(v,w) for v in [1,2,3] for w in [4,5,6] if v % 2 == 0]
print(lista2)
lista2 = [(v,w) for v in [1,2,3] if v % 2 == 0 for w in [4,5,6]]
print(lista2)
lista3 = [ [i for i in range(4)] for v in range(4)]
print(lista3)
