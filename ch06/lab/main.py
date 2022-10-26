import turtle

def main():
  my_turtle = turtle.Turtle() 
  my_turtle.shape('turtle')
  screen = turtle.Screen()
  x_cord = 500
  y_cord = 500
  screen.screensize(x_cord,y_cord,'green')
  shape_sides = 5
  side_length = 100
  angle = shape_angle(shape_sides)
  draw_shape(angle,side_length,shape_sides,my_turtle)
  
  screen.exitonclick() 

def shape_angle(shape_sides):
  angle = 360 / shape_sides
  return angle

def draw_shape(angle,side_length,shape_sides,turtle):
  for i in range(shape_sides):
     turtle.forward(side_length)
     turtle.left(angle) 
    
main()

