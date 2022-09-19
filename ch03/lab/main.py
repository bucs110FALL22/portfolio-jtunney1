import turtle #1. import modules
import random
import pygame
import math

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
michelangelo.down() 
leonardo.down()
michelangelo.forward(random_a)
leonardo.forward(random_b)

#reset turtles to start
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#second race
michelangelo.down() 
leonardo.down()

for i in range(10):
  michelangelo.forward(random.randint(1,11))
  leonardo.forward(random.randint(1,11))

#reset turtles to start
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
#(Step 1) Declare variables
coords = []
num_sides = 8
side_length = 10
offset = 10

#(Step 2) 
for i in range(5):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append(x, y)

#(Step 3)

window.exitonclick()
