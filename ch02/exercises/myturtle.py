import turtle

my_turtle = turtle.Turtle() 
my_turtle.shape('turtle')

my_turtle.color('purple')
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)

my_turtle.color('red')
my_turtle.penup()
my_turtle.forward(60)
my_turtle.pendown()
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)

window = turtle.Screen()
window.exitonclick()