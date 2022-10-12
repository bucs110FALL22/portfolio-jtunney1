import turtle

my_turtle = turtle.Turtle() 
my_turtle.shape('turtle')
my_turtle.color('blue')

def drawEqShape(my_turtle,shape_sides=0,side_length=0):
  angle = 360 / shape_sides
  for i in range(shape_sides):
     my_turtle.forward(side_length)
     my_turtle.left(angle) 

drawEqShape(my_turtle,shape_sides=5,side_length=70)
window = turtle.Screen()
window.exitonclick() 