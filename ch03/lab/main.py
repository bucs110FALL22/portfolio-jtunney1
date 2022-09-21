import turtle #1. import modules
import random
import pygame
import math

pygame.init()

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#variables for first race
random_a = random.randint(1,101)
random_b = random.randint(1,101)

#first race
michelangelo.forward(random_a)
leonardo.forward(random_b)
pygame.time.wait(500)

#reset turtles to start
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#second race
for i in range(10):
  michelangelo.forward(random.randint(1,11))
  leonardo.forward(random.randint(1,11))
  #so we can see result
  pygame.time.wait(100)

#so we can see result
pygame.time.wait(500)

#reset turtles to start
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()

# PART B - complete part B here

#triangle
#(Step 1) Declare variables
window = pygame.display.set_mode()
coords = []
num_sides = 3
side_length = 50
offset = 100

#(Step 2) generates the points for polygon
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x , y])

#(Step 3) 
pygame.draw.polygon(window, 'blue', coords)
pygame.display.flip()
pygame.time.wait(1000)

#reset screen
window.fill('black')
pygame.display.flip()


#square
window = pygame.display.set_mode()
coords = []
num_sides = 4
side_length = 50
offset = 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x , y])

pygame.draw.polygon(window, 'blue', coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('black')
pygame.display.flip()

#hexagon
window = pygame.display.set_mode()
coords = []
num_sides = 6
side_length = 50
offset = 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x , y])

pygame.draw.polygon(window, 'blue', coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('black')
pygame.display.flip()

#nonagon
window = pygame.display.set_mode()
coords = []
num_sides = 9
side_length = 50
offset = 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x , y])

pygame.draw.polygon(window, 'blue', coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('black')
pygame.display.flip()

#circle
window = pygame.display.set_mode()
coords = []
num_sides = 360
side_length = 50
offset = 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x , y])

pygame.draw.polygon(window, 'blue', coords)
pygame.display.flip()
pygame.time.wait(1000)

window.fill('black')
pygame.display.flip()

