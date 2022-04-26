#Uma empresa deseja reajustar o salário de seus empregados conforme a seguinte tabela:
#Salário
#Acréscimo
#superior ou igual a 3.000,00
#8%
#inferior a 3.000,00 mas superior ou igual a 2.000,00
#10%
#inferior a 2.000,00
#12%

#Para cada empregado será digitado seu salário.

 #Elabore um programa que leia a quantidade de empregados e em seguida os dados de cada empregado (salário). Calcule e mostre:

#a)  para cada empregado, o salário reajustado (conforme tabela);

#b)  a quantidade de empregados que receberam reajuste de 10%;

#c)  o salário médio (após o reajuste) entre os empregados;

#OBS: Lembre-se de que as operações com dinheiro devem conter duas casas decimais para indicar os centavos. 
#Formate a saída para adequar o programa a esse contexto (Não arredondar antes da formatação).

funcionarios = int(input())
for x in range(funcionarios):
    salario = float(input())
    if (salario >3000):
        oitoporcent = salario+salario*(1/8)
        print(oitoporcent)
    elif (salario>=2000):
        dezporcent = salario+salario/10
        print(dezporcent)
    else:
        dozeporcent = salario+salario*(3/25)
        print(dozeporcent)
        
