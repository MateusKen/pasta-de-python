print("		Calculadora")

pergunta = input("Você deseja fazer alguma operação? [s/n]		")
while pergunta == "s":
	op = input("Qual operação desejada? [multiplicação ou mult / divisão ou div / subtração ou sub/ adição ou ad / radiciação ou rad / potenciação ou pot]		")
	if op == "multiplicação" or op == "mult":
		n1 = int(input("Digite o primeiro número.	"))
		n2 = int(input("Digite o segundo número.	"))
		print(n1 * n2)
	if op == "divisão" or op == "div":
		print ("2")
		n1 = int(input("Digite o dividendo desejado.	"))
		n2 = int(input("Digite o divisor desejado.	"))
		print(n1 / n2)
	if op == "adição" or op == "ad":
		n1 = int(input("Digite o primeiro número.	"))
		n2 = int(input("Digite o segundo número.	"))
		print(n1 + n2)
	if op == "subtração" or op == "sub":
		n1 = int(input("Digite o primeiro número.	"))
		n2 = int(input("Digite o segundo número.	"))
		print(n1 - n2)
	if op == "potenciação" or op == "pot":
		n1 = int(input("Digite a base	"))
		n2 = int(input("Digite o expoente	"))
		print(n1 ** n2)
	if op == "radiciação" or op == "rad":
		n1 = int(input("Digite o índice da raiz		"))
		n2 = int(input("Digite o radicando		"))
		print( n2 ** (1 /n1))
	
	else:
		print("Não existe essa opção digite novamente por favor.")

	pergunta = input("Você deseja fazer mais alguma operação? [s/n]		")