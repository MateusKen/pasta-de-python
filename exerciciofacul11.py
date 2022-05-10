'''
Faça um programa em Python, utilizando lista que recebe de entrada 10 caratceres, armazenando cada caracter numa posição da lista.

Após a entrada de dados, o programa deve mapear a lista e contar a quantidade de vogais e a quantidade de consoantes.

Na saída de dados é esperada a quantidade de vogais e a quantidade de consoantes, nesta ordem, uma informação em cada linha.
'''
letras = ''
vogal = 0
consoante = 0
for i in range(10):
    letra = input()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vogal +=1
    else:
        consoante +=1
    letras = letras + letra
print(vogal)
print(consoante)
