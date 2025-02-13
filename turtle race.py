from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput('make your bet',"which turtle will win the race ? enter your color:  ")
print(user_bet)
colors=['red','green','orange','blue','purple']
all_turtle=[]
tim=Turtle()
tim.color('blue')
tim.shape('turtle')
tim.penup()
tim.hideturtle()
hero=Turtle('turtle')
all_turtle.append(hero)
hero.color('red')
hero.penup()
hero.goto(x=-230,y=50)
hero1=Turtle('turtle')
all_turtle.append(hero1)
hero1.color('green')
hero1.penup()
hero1.goto(x=-230,y=100)
hero2=Turtle('turtle')
all_turtle.append(hero2)
hero2.color('orange')
hero2.penup()
hero2.goto(x=-230,y=150)
hero_3=Turtle('turtle')
all_turtle.append(hero_3)
hero_3.color('purple')
hero_3.penup()
hero_3.goto(x=-230,y=-50)
hero4=Turtle('turtle')
all_turtle.append(hero4)
hero4.color('black')
hero4.penup()
hero4.goto(x=-230,y=-100)
aryan=Turtle('turtle')
all_turtle.append(aryan)
aryan.color('teal')
aryan.penup()
aryan.goto(x=-230,y=0)
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print('you won!')
            else:
                print('you lose')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()