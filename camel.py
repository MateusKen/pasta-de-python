import random
print("Bem-vindo ao Camel!")
print()
print("	Você roubou um camelo para atravessar o grande deserto de Mobi.")
print("	O dono do camelo o quer de volta e está te perseguindo!")
print("	Sobreviva ao deserto e escape do dono do camelo.")
print("	Para ganhar esse jogo você deverá percorrer apenas 50km!! ")
print("	Mas atenção! Se sua água chegar a zero ou menos, você perde.")
print("	Se o cansaço do camelo chegar a 20, você perde.")
print("	Se o dono do camelo chegar a até você ou te passar, você perde.")
print("	Boa sorte e bom jogo!")
print()
print("Obs: letras maiúsculas ou minúsculas são aceitas.")
print()
input("	aperte ENTER para continuar")
print()
km = 0 
water = 20 
tiredness = 0 
owner = -20
kmm = random.randint(3,5)
kmmm = random.randint(5,7)
waterm = random.randint(4,6)
watermm = random.randint(7,10)
tirednessm = random.randint(4,6)
tirednessmm = random.randint(7,10)
waterp = random.randint(3,5)
tirednessp = 1
tirednessk= random.randint(4,7)
while True:
	print("A. Dar água para o camelo.")
	print("B. Avançar com velocidade moderada.")
	print("C. Avançar com velocidade máxima.")
	print("D. Parar para dencansar à noite.")
	print("E. Checar o status.")
	print("Q. Sair.")
	print()
	res = input("Qual a sua escolha?	")
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
 #(1)
	if res == "Q" or res == "q":
		p1 = input("Você tem certeza? [s/n]	")
		print()
		if p1 == "S" or p1 == "s":
			break
		if p1 == "N" or p1 == "n":
			continue
		else:
			print("Resposta não válida, digite novamente")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()


#(2)
	if res == "E" or res == "e":
		print(f"Você andou {km} km")
		print(f"Água bebida {water}")
		print(f"Cansaço do camelo {tiredness}")
		print("O dono está " + str(km - owner) + " km de você")
		print()
		if 15<tiredness<20:
			print("Você deveria descasar um pouco")
		if 0<water<5:
			print("Você deveria dar água para o camelo")
		if 0<(km-owner)<10:
			print("Você deveria andar mais")
		print()	
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()

#(3)
	if res == "C" or res == "c":
		km += kmmm
		water -= watermm
		tiredness += tirednessmm
		owner += random.randint(5,6)
		print()
		print("+" + str(kmmm) + " km")
		print(f"- {watermm} água")
		print(f"+ {tirednessmm} cansaço")
		print("O dono está " + str(km - owner) + " km de você")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()

#(4)
	if res == "B" or res == "b":
		km += kmm 
		water -= waterm
		tiredness += tirednessm
		owner += random.randint(5,6)
		print()
		print("+" + str(kmm) + " km")
		print(f"- {waterm} água")
		print(f"+ {tirednessm} cansaço")
		print("O dono está " + str(km - owner) + " km de você")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()

#(5)
	if  res == "A" or res == "a":
		water += waterp
		tiredness -= tirednessp 
		owner += random.randint(5,6)
		print()
		print(f"+ {waterp} água")
		print(f"- {tiredness} cansaço")
		print("O dono está " + str(km - owner) + " km de você")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()

#(6)
	if res == "D" or res == "d":
		tiredness -= tirednessk
		owner += random.randint(5,8)
		print()
		print(f"- {tirednessk} cansaço")
		print("O dono está " + str(km - owner) + " km de você")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()


#(7)
	if tiredness >= 20:
		print("Seu camelo morreu de cansaço, você perdeu.")
		print()
		p2 = input("Tentar novamente? [s/n]	")
		print()
		if p2 == "S" or p2 == "s":
			km = 0 
			water = 20 
			tiredness = 0
			owner = -20 
			continue
		if p2 == "N" or p2 == "n":
			break 
		else:
			print("Resposta não válida")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()		
#(8)
	if water <= 0:
		print("Seu camelo morreu de sede, você perdeu.")
		print()
		p2 = input("Tentar novamente? [s/n]	")
		print()
		if p2 == "S" or p2 == "s":
	 		km = 0
	 		water = 20
	 		tiredness = 0
	 		owner = -20
	 		continue
		if p2 == "N" or p2 == "n":
			break
		else:
			print("Resposta não válida")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
#(9)
	if (km-owner) <= 0:
		print("O dono alcançastes, você perdeu.")
		print()
		p2 = input("Tentar novamente? [s/n]	")
		print()
		if p2 == "S" or p2 == "s" :
	 		km = 0
	 		water = 20
	 		tiredness = 0
	 		owner = -20
	 		continue
		if p2 == "N" or p2 == "n":
			break 
		else:
			print("Resposta não válida")
		print()	
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
#(10)
	if km >= 50:
		print("Você conseguiu fugir do dono do camelo com sucesso, parabéns você venceu.")
		print()
		p2 = input("Tentar novamente? [s/n]	")
		print()
		if p2 == "S" or p2 == "s":
			km = 0 
			water = 20 
			tiredness = 0
			owner = -20 
			continue
		if p2 == "N" or p2 == "n":
			break 
		else:
			print("Resposta não válida")
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
#(11)
	if km == random.randint(10,15):
		print()
		print("Você achou um oásis!!")
		print()
		water += 5
		tiredness -= 5
		owner += 2 
#(12)
	if (km-owner) >= 2 and (km-owner)<0 and tiredness >= 18 and tiredness <20:
		input("	aperte ENTER para continuar")
		print("Você: Tsugi wa Jotaro, kisama da!")	
		print("Dono: Yarou… DIO!")	
		print("ゴゴゴゴ")
		print("Você: Ho… mukatta kuruno ka?")
		print("Você: Nigetsu ni kono DIO ni chikazuite kuruno ka? ")
		print("Você: Sekkaku sofu no Josefu ga watashi no Za Warudo no shotai wo.")
		print("Você: Shiken shuryu chaimu chokuzen made mondai yo toitte iru jukensee ne you na?")
		print("Você: Kisshi koita kibun de wo shietekure ta to yuu no ni?")
		print("ゴゴゴゴ")
		input("	aperte ENTER para continuar")
		print("Dono: Chikadzu kanaka teme wo buchi no me tenain de na.")
		input("	aperte ENTER para continuar")
		print("Você: HO HO !")
		print("Você: Dewa juubun chikazukanai youi.")	
		print("ゴゴゴゴ")
		input("	aperte ENTER para continuar")
		print("O dono parece estar bem irritado,")
		print("ele está bem perto de você,")
		print("você está muito cansado de correr,")
		print("o que fará?!")
		while True:
			print("A. Correr e se esconder")
			print("B. Procurar por Polnareff para acabar com sua vida deixando-o (o dono) em desvantgem")
			print("C. Ativar 『The World』")
			print("Q. Sair.")
			print()
			res2 = input("O que fará??")
#(12.1)
			if res2 == "Q" or res2 == "q":
				print()
				p1 = input("Você tem certeza? [s/n]	")
				print()
				if p1 == "S" or p1 == "s":
					break
				if p1 == "N" or p1 == "n":
					continue
				else:
					print("Resposta não válida, digite novamente")
					print()
#(12.2)
			if res2 == "A" or  res2 == "a":
				print("Você ainda se acha merecedor do 『The World』?!")
				print("Um homem não foge da luta,")
				print("ainda mais contra a família Joestar.")
				input("Aperte ENTER para continuar.")
				print("Devido a esse fato você percebe ser desmerecedor de suas ambições")
				print("Você perdeu e por justa causa ainda")
				print()
				p2 = input("Tentar novamente? [s/n]	")
				print()
				if p2 == "S" or p2 == "s":
					km = 0 
					water = 20 
					tiredness = 0
					owner = -20 
					continue
				if p2 == "N" or p2 == "n":
					break 
				else:
					print("Resposta não válida")
					print()
#(12.3)
				if res2 == "C" or  res2 == "c":
					print("Dono: Ora!")
					print("Você: Noroi, noroi! Za Warudo wa saikyou no Sutando da.")
					print("Você:  Jikan wa tomezetomo,")
					print("Você:  supiido to paowa to te omae no Suta Purachina yoryuu enna no towa!")
					input("Aperte ENTER para continuar.")
					print("Dono: Ore no Suta Purachina to onaji taipu wo Sutando nara.")
					print("Dono: Enkyori enai kenai da, paowa to semitsu na bokina dekiru.")
					input("Aperte ENTER para continuar.")
					print("To be continued...")
					input("Aperte ENTER para continuar.")
					print()
					p2 = input("Tentar novamente? [s/n]	")
					print()
					if p2 == "S" or p2 == "s":
						km = 0 
						water = 20 
						tiredness = 0
						owner = -20 
						continue
					if p2 == "N" or p2 == "n":
						break 
					else:
						print("Resposta não válida")
						print()
#(12.4)
				if res2 == "B" or res2 =="b":
					print("Uma morte inevitável já lhe aguardava")
					print("com a força de um milhão de homens.")
					print("Parece que o 『Star Platinum』 realmente era melhor que o seu 『The World』")
					input("Aperte ENTER para continuar.")
					print("Você morre e perde")
					print()
					p2 = input("Tentar novamente? [s/n]	")
					print()
					if p2 == "S" or p2 == "s":
						km = 0 
						water = 20 
						tiredness = 0
						owner = -20 
						continue
					if p2 == "N" or p2 == "n":
						break 
					else:
						print("Resposta não válida")
						print()
