import turtle
import random
import time
tela = turtle.Screen()
pl = turtle.Turtle()
pk = turtle.Turtle()
po = turtle.Turtle()
po.speed(0)
pl.ht()
pk.ht()
pl.color("red")
pk.color("green")
pk.pu()
po.pu()
pl.pu()
po.goto(-200,0)
po.pd()
po.goto(200,0)
po.goto(200,200)
po.goto(200,-200)
po.ht()
pl.goto(-200,-100)
pl.st()
pk.goto(-200,100)
pk.st()
pl.pd()
pk.pd() 

pk.speed(1)
pl.speed(1)

while pl.xcor() < 200 and pk.xcor() < 200:	 
	pl.fd(random.randint(20, 40))
	pk.fd(random.randint(20, 40))


if pk.xcor() > pl.xcor():
	pk.pu()
	pk.goto(-100,100)
	pk.write("Luigi time" , font = ('Comic Sans MS' , 36 , 'bold'))




elif pl.xcor() > pk.xcor():
	pl.pu()
	pl.goto(-100,-100)
	pl.write("Mario time" , font = ('Comic Sans MS' , 36 , 'bold'))




elif pk.xcor() == pl.xcor():
	po.pu()
	po.goto(-100,0)
	po.write("It`s a tie!" , font = ('Comic Sans MS' , 36 , 'bold'))



pl.ht()
pk.ht()
po.ht()

turtle.mainloop()