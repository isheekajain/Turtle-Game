import random
from turtle import Turtle, Screen


screen = Screen()

is_race_on = False
user_ans = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

x = -230
y = -100

# empire turtle
empire = Turtle("turtle")
empire.color("black")
empire.penup()
empire.left(90)
empire.goto(230, 150)
empire.pendown()
empire.backward(305)
empire.penup()
empire.goto(-35, 155)
empire.pendown()
empire.write("Start")
empire.penup()
empire.goto(-130, -155)
empire.hideturtle()
empire.pendown()

turtles = []


def make_a_turtle(color, xcor, ycor):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    screen.setup(width=500, height=400)
    new_turtle.goto(xcor, ycor)
    new_turtle.color(color)
    turtles.append(new_turtle)


for each in colors:
    x += 0
    y += 30
    make_a_turtle(each, xcor=x, ycor=y)

if user_ans:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 211:
            is_race_on = False
            winning_color = turtle.pencolor()
            empire.write(f" Winner: {winning_color} turtle", font="12")
            empire.penup()
            empire.goto(-130, -100)
            empire.pendown()
            if winning_color == user_ans:
                # print(f"You've won! The {winning_color} turtle is the winner!")
                screen.title(f"You've won! The {winning_color} turtle is the winner!")
            else:
                # print(f"You've lost! The {winning_color} turtle is the winner!")
                screen.title(f"You've lost! The {winning_color} turtle is the winner!")
            break
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
