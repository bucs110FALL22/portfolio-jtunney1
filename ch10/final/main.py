import turtle

def bg(screen):
  #Sets size and background color of screen
  #Args: what screen you want to set color and size of
  #Returns demensions of screen
  screen_size = [400,400]
  screen.screensize(screen_size[0],screen_size[1],'black')

def draw_sun():
  color = 'orange'
  sun_radius = 100
  center_y = circle_cords(sun_radius)
  center_x = 0
  sun_circle(sun_radius,color,center_x,center_y)

def circle_cords(radius):
  center_y_cord = 0 - radius
  return center_y_cord

def sun_circle(radius,color,x_pos,y_pos):
  turtle.up()
  turtle.goto(x_pos,y_pos)
  turtle.color(color)
  turtle.down()
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()

def draw_star(x_pos,y_pos,color):
  turtle.up()
  turtle.goto(x_pos,y_pos)
  turtle.color(color)
  turtle.down()
  turtle.begin_fill()
  #instead draw triangle then draw second triangle facing other direction
  for i in range(5):
    turtle.forward(50)
    turtle.left(144)
  turtle.end_fill()

def place_stars():
  color = 'yellow'
  draw_star(-170,0,color)
  draw_star(-50,-150,color)
  draw_star(150,-100,color)
  draw_star(100,130,color)
  draw_star(65,-190,color)

def main():
  turtle.speed(0)
  window = turtle.Screen()
  bg(window)
  draw_sun()
  place_stars()
  window.exitonclick()

main()