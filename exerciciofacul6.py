#Elaborar um programa em Python fazendo uso do comando while que leia um conjunto de dados numéricos do tipo real (positivos ou negativos) 
#de tamanho N (N > 0, lido do usuário), encontre e apresente o menor e maior valor do  conjunto, cada um deles mostrados em uma linha diferente.  
#Caso o tamanho de N seja menor ou igual a zero escrever a mensagem de erro: “Tamanho inválido!”. Obs.: A mensagem de erro  deve ser igual ao informado. 
#Então, copie e cole esse texto para evitar erro de digitação, ok!
N = int(input())
cont = 0
while cont < N:
    nro = float(input())
    if cont == 0: 
        menor = nro
        maior = nro
    else:
        if nro < menor:
            menor = nro
        elif nro > maior:
            maior = nro
    cont+=1

if N > 0:
    print(f"{menor}\n{maior}")
else:
    print("Tamanho inválido!")

    
N = int(input())
i2 = 0
if N>0:
    while i2 <= i:
        
else:
    print('Tamanho inválido!')
