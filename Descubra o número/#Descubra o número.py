#Descubra o número
x=int(input("Entre com o número a ser descoberto:\n "))
y=int(input("Chute um número:\n "))
while y!=x:
    if x>y:
        print("O número é mais alto que isso!")
    else:
        print("O número é menor que isso!")
    y=int(input("Chute um número:\n "))    
print("ACERTOU!\n"*3)