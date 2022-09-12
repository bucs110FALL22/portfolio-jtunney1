import turtle

#ask for user input on shape and its size
shape_sides = int(input("How many sides?: "))
side_length = int(input("Length of sides?: "))
pick_color = (input("Shape color?: "))

#shape and color of the turtle
my_turtle = turtle.Turtle() 
my_turtle.shape('turtle')
my_turtle.color(pick_color)

angle = 360 / shape_sides

#draw shape
for i in [0]*shape_sides:
  my_turtle.forward(side_length)
  my_turtle.left(angle)

window = turtle.Screen()
window.exitonclick()