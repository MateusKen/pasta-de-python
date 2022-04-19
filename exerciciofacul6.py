#Elaborar um programa em Python fazendo uso do comando while que leia um conjunto de dados numéricos do tipo real (positivos ou negativos) 
#de tamanho N (N > 0, lido do usuário), encontre e apresente o menor e maior valor do  conjunto, cada um deles mostrados em uma linha diferente.  
#Caso o tamanho de N seja menor ou igual a zero escrever a mensagem de erro: “Tamanho inválido!”. Obs.: A mensagem de erro  deve ser igual ao informado. 
#Então, copie e cole esse texto para evitar erro de digitação, ok!
N = int(input())
i = 0
if N>0:
    while i < N:
        num = float(input())
        if i == 0:
            menor = num
            maior = num
        else:
            if num < menor:
                menor = num
            elif num > maior:
                maior = num
        i = i+1
    print(menor)
    print(maior)
else:
    print('Tamanho inválido!')

