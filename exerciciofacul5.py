#Elaborar um programa em Python fazendo uso do comando de repetição while que solicita ao usuário números inteiros e determina: 
#a soma, a quantidade e a média de números digitados, enquanto o usuário não digitar -1. 
#Ao final devem ser apresentados os resultados na seguinte ordem: soma, quantidade e média de números digitados, exceto o -1, 
#cada um deles mostrados em uma linha diferente. Se o usuário digitar -1 logo no começo, apresentar a mensagem: “Nenhum número foi digitado!”. 
#Obs.: Essa mensagem deve ser igual ao informado. Então, copie e cole esse texto para evitar erro de digitação, ok!
num = int(input())
soma = 0
i = 0
if num == -1:
    print('Nenhum número foi digitado!')
else:    
    while num != -1:
        soma = soma+num
        num = int(input())
        i = i+1
    print(soma)
    print(i)
    print(soma/i)
