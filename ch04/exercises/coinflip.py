import turtle
import random

window = turtle.Screen()
window.screensize(500,500)
window.bgcolor('lightblue')

turtle_draw = turtle.Turtle()
turtle_draw.down()
turtle_draw.pencolor('blue')

x_cord = turtle_draw.xcor()
y_cord = turtle_draw.ycor()
while x_cord < 250 and x_cord > -250 and y_cord < 250 and y_cord > -250:
  rand = random.randint(1,2)
  if rand == 1:
    turtle_draw.right(90)
  elif rand == 2:
    turtle_draw.left(90)
    
  turtle_draw.forward(50)
  x_cord = turtle_draw.xcor()
  y_cord = turtle_draw.ycor()


window.exitonclick()