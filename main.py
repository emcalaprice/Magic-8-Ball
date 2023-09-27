from random import *
import turtle
tommy = turtle.Turtle()
tommy.speed(0)


def drawBall():
  tommy.penup()
  tommy.goto(0,-200)
  tommy.pendown()
  tommy.color("black")
  tommy.begin_fill()
  tommy.circle(200)
  tommy.end_fill()
  tommy.penup()
  tommy.goto(0,-100)
  tommy.pendown()
  tommy.color("white")
  tommy.begin_fill()
  tommy.circle(100)
  tommy.end_fill()
  tommy.penup()
  tommy.color("black")
  tommy.goto(0,-100)
  tommy.write("8",align="center",font=("Garamond",130))
  tommy.hideturtle()

drawBall()

answers = ['Yes', 'No', 'Maybe', 'For sure','Ask later', 'Most likely', 'Idk', 'Absolutely', 'Not a chance', 'Stop being annoying']
turtle.Screen().textinput('Ask a question','Or type quit to exit')
turtle.color("#8ab5ff")
turtle.write(answers[randint(0,2)],align='center',font=('Garamond',70,'bold'))
turtle.done()