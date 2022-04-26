#    Elabore um programa que calcule e apresente o valor de S, dado por:

#         S = 1/N + 2/N-1 + 3/N-2 + ... + N-1/2 + N
 
#    Em que N  é fornecido pelo usuário.

s = 0

n = int(input())

for i in range(1,n+1,1):
    
    s += i / (n - i + 1)
    
print(s)
