import turtle
import random

#create blue background and randomly generate snowflakes
def background(screen):
  x_size = 700
  y_size = 800
  screen.screensize(x_size,y_size,'blue')
  for i in range(25):
    x_cord = random.randint(-320,320)
    y_cord = random.randint(-350,350)
    branches = random.randint(5,11)
    snowflake(x_cord,y_cord,branches)

#function that determines size of the next snowball on top
def snowball_size(ball_radius=0):
  ball_radius = ball_radius * .8
  return ball_radius

#determines where to start drawing the next snowball from
def snowball_start(y_ball_start=0,ball_radius=0):
  y_ball_start = y_ball_start + ball_radius * 1.5
  return y_ball_start

#function that creates the 3 snowballs for the snowmans body
def snowman_body():
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
  
  
#creates eyes and nose for the face of the snowman
def snowman_eyes_nose():
  eye_x = -25
  eye_y = -40
  radius = 7
  turtle.color('black')
  for i in range(2):
    turtle.up()
    turtle.goto(eye_x,eye_y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    eye_x = eye_x + 50
  turtle.up()
  nose_x = 0
  nose_y = -60
  radius = 4
  turtle.goto(nose_x,nose_y)
  turtle.color('orange')
  turtle.down()
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()
  turtle.up()

#creates mouth of the snowman
def snowman_smile():
  smile_x = 0
  smile_y = -80
  radius = 4
  for i in range(3):    
    turtle.goto(smile_x,smile_y)
    turtle.color('black')
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    smile_x = smile_x + 15
    smile_y = smile_y + 4
  smile_x = -15
  smile_y = -76
  for i in range(2):
    turtle.goto(smile_x,smile_y)
    turtle.color('black')
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    smile_x = smile_x - 15
    smile_y = smile_y + 4

  
#creates buttons for snowmans chest
def snowman_buttons():
  x_button = 0
  y_button = -210
  radius = 3
  turtle.color('black')
  for i in range(3):
    turtle.up()
    turtle.goto(x_button,y_button)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    y_button = y_button + 45
  
    
#draws hat for snowman
def snowman_hat():
  x_start = 0
  y_start = -15
  turtle.up()
  turtle.goto(x_start,y_start)
  turtle.pd()
  turtle.color('black')
  turtle.right(180)
  turtle.begin_fill()
  turtle.forward(60)
  turtle.right(90)
  turtle.forward(20)
  turtle.right(90)
  turtle.forward(40)
  turtle.left(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(40)
  turtle.right(90)
  turtle.forward(20)
  turtle.right(90)
  turtle.forward(60)
  turtle.end_fill()

#draws left side arm of snowman
def left_snowman_arm():
  left_arm_x = -63
  left_arm_y = -115
  turtle.up()
  turtle.goto(left_arm_x,left_arm_y)
  turtle.pd()
  turtle.color('brown')
  turtle.width(7)
  turtle.right(20)
  turtle.forward(80)
  turtle.right(180)
  turtle.forward(20)
  turtle.right(150)
  turtle.forward(25)
  turtle.up()

#draws right side arm of snowman
def right_snowman_arm():
  left_arm_x = 63
  left_arm_y = -115
  turtle.up()
  turtle.goto(left_arm_x,left_arm_y)
  turtle.pd()
  turtle.color('brown')
  turtle.width(7)
  turtle.right(180)
  turtle.forward(80)
  turtle.right(180)
  turtle.forward(20)
  turtle.left(150)
  turtle.forward(25)
  turtle.up()
  
#funtion takes in (x,y) coordinates and number of branches and generates a snowflake there
def snowflake(x_cord,y_cord,branches):
  turtle.up()
  turtle.goto(x_cord,y_cord)
  turtle.down()
  turtle.color('light blue')
  turtle.width(3)
  angle = 360 / branches
  for i in range(branches):
    turtle.forward(20)
    turtle.right(30)
    turtle.forward(10)
    turtle.back(10)
    turtle.left(60)
    turtle.forward(10)
    turtle.back(10)
    turtle.right(30)
    turtle.back(20)
    turtle.right(angle)
  turtle.up()

def main():
  turtle.speed(0)
  screen = turtle.Screen()
  background(screen)
  snowman_body()
  snowman_buttons()
  snowman_hat()
  snowman_eyes_nose()
  snowman_smile()
  left_snowman_arm()
  right_snowman_arm()

  screen.exitonclick()
  
main()