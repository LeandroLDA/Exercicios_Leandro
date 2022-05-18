#pequenas expressões

'Trabalhando listas'

list=[]

i=0
while i <5:
    x=eval(input("Entre com o dado desejado:\n"))
    list.append(x)
    i=i+1
list.sort()
print ("A lista é composta por estes ítens: ",list,"\n")
print("O tamanho total da lista é: ", len(list)," Itens.\n")
print("O menor valor da lista é: ", min(list),"\n")
print("O maior valor da lista é: ", max(list),"\n")