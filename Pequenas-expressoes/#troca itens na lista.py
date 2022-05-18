#troca itens na lista
lista = ["maçã", "banana", "côco", "limão"]
lst = lista
def trocaPu (lst):
    lst[0], lst[-1] = lst[-1], lst[0]

print (lst)
trocaPu(lst)
print (lst)