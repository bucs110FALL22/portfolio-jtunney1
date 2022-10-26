import turtle

def main():
  my_turtle = turtle.Turtle() 
  my_turtle.shape('turtle')
  screen = turtle.Screen()
  x_cord = 500
  y_cord = 500
  screen.screensize(x_cord,y_cord,'blue')
  colors = ['red','orange','yellow']
  x_start = 0
  shape_sides = 5
  side_length = 50
  draw_flower(colors,x_start,shape_sides,side_length,my_turtle)
  
  screen.exitonclick() 

def shape_angle(shape_sides):
  angle = 360 / shape_sides
  return angle

def draw_shape(angle,side_length,shape_sides,turtle,color,x_start,y_start):
  turtle.color(color)
  turtle.up()
  x_draw_start = x_start - side_length / 2
  turtle.goto(x_draw_start,y_start)
  turtle.pensize(1)
  turtle.begin_fill()
  for i in range(shape_sides):
     turtle.forward(side_length)
     turtle.left(angle) 
  turtle.end_fill()

def draw_stem(x_start):
  turtle.color('green')
  turtle.pensize(8)
  turtle.up()
  turtle.goto(x_start,-250)
  turtle.down()
  y_height = 80
  turtle.forward(y_height)
  return y_height

def draw_flower(colors,x_start,shape_sides,side_length,turtle):
  y_start = draw_stem(x_start)
  angle = shape_angle(shape_sides)
  draw_shape(angle,side_length,shape_sides,turtle,colors[0],x_start,y_start)
  side_length = side_length * .8
  x_start = 10
  y_start = 10
  draw_shape(angle,side_length,shape_sides,turtle,colors[1],x_start,y_start)
  side_length = side_length * .8
  x_start = 10
  y_start = 10
  draw_shape(angle,side_length,shape_sides,turtle,colors[2],x_start,y_start)


    
main()

