import turtle
tela = turtle.Screen()
tela.bgcolor("black")
popu = turtle.Turtle()

popu.speed(7)

popu.goto(-80,55)

popu.color("red")
popu.begin_fill()
for p in range(2):
	popu.fd(160)
	popu.rt(90)
	popu.fd(110)
	popu.rt(90)
popu.end_fill()

popu.color("white")

popu.pu()
popu.goto(-80,45)
popu.pd()
popu.begin_fill()
for p in range(2):
	popu.fd(160)
	popu.rt(90)
	popu.fd(10)
	popu.rt(90)
popu.end_fill()

popu.pu()
popu.goto(-80,25)
popu.pd()
popu.begin_fill()
for p in range(2):
	popu.fd(160)
	popu.rt(90)
	popu.fd(10)
	popu.rt(90)
popu.end_fill()

popu.pu()
popu.goto(-80,5)
popu.pd()
popu.begin_fill()
for p in range(2):
	popu.fd(160)
	popu.rt(90)
	popu.fd(10)
	popu.rt(90)
popu.end_fill()

popu.pu()
popu.goto(-80,-15)
popu.pd()
popu.begin_fill()
for p in range(2):
	popu.fd(160)
	popu.rt(90)
	popu.fd(10)
	popu.rt(90)
popu.end_fill()

popu.pu()
popu.goto(-80,-35)
popu.pd()
popu.begin_fill()
for p in range(2):
	popu.fd(160)
	popu.rt(90)
	popu.fd(10)
	popu.rt(90)
popu.end_fill()

popu.color("blue")
popu.pu()
popu.goto(-80,55)
popu.pd()
popu.begin_fill()
for p in range(2):
	popu.fd(90)
	popu.rt(90)
	popu.fd(60)
	popu.rt(90)
popu.end_fill()

popu.pu()
popu.goto(-80,50)
for p in range(9):
	popu.fd(5); popu.dot(5,"white"); popu.fd(5)

popu.pu()
popu.goto(-80,40)
for p in range(9):
	popu.fd(5); popu.dot(5,"white"); popu.fd(5)

popu.pu()
popu.goto(-80,30)
for p in range(9):
	popu.fd(5); popu.dot(5,"white"); popu.fd(5)

popu.pu()
popu.goto(-80,20)
for p in range(9):
	popu.fd(5); popu.dot(5,"white"); popu.fd(5)

popu.pu()
popu.goto(-80,10)
for p in range(9):
	popu.fd(5); popu.dot(5,"white"); popu.fd(5)

	popu.pu()
popu.goto(-80,0)
for p in range(9):
	popu.fd(5); popu.dot(5,"white"); popu.fd(5)

popu.ht()

turtle.mainloop()