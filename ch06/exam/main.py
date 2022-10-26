import turtle
#snowman

def background(screen):
  x_size = 700
  y_size = 800
  screen.screensize(x_size,y_size,'light blue')

def snowball_size(ball_radius=0):
  ball_radius = ball_radius * .8
  return ball_radius

def snowball_start(y_ball_start=0,ball_radius=0):
  y_ball_start = y_ball_start + ball_radius * 1.5
  return y_ball_start

def snowman_body(turtle):
  x_start = 0
  y_start = -400
  radius = 100
  turtle.color('white')
  for i in range(3):
   turtle.up()
   turtle.goto(x_start,y_start)
   turtle.down()
   turtle.begin_fill()
   turtle.circle(radius)
   y_start = snowball_start(y_ball_start=y_start,ball_radius=radius)
   radius = snowball_size(ball_radius=radius)
   turtle.end_fill()
  
  

def snowman_face():
  pass

def snowman_buttons():
  x_button = 0
  y_button = -210
  radius = 3
  turtle.color('black')
  turtle.begin_fill()
  for i in range(3):
    turtle.up()
    turtle.goto(x_button,y_button)
    turtle.down()
    turtle.circle(radius)
    y_button = y_button + 45
  turtle.end_fill()
    

def snowman_hat(turtle):
  x_start = 0
  y_start = 600
  turtle.up()
  turtle.goto(x_start,y_start)
  turtle.color('black')
  turtle.down()
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(60)
  turtle.right(90)
  turtle.forward(40)
  turtle.right(90)
  turtle.forward(60)
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()

def snowman_arms():
  pass

def snowflake():
  pass

def main():
  my_turtle = turtle.Turtle() 
  my_turtle.shape('turtle')
  my_turtle.speed(0)
  screen = turtle.Screen()
  background(screen)
  snowman_body(my_turtle)
  snowman_buttons()
  snowman_hat(my_turtle)

  screen.exitonclick()
main()