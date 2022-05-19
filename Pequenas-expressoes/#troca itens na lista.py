#troca itens na lista
lista = ["maçã", "banana", "côco", "limão"]

def trocaPu (lst):
    lst[0], lst[-1] = lst[-1], lst[0]

print (lista)
trocaPu(lista)
print (lista)