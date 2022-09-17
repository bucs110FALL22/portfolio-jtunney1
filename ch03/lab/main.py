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

for i in []*10:
  michelangelo.forward(random.randint(1,11))
  leonardo.forward(random.randint(1,11))

#reset turtles to start
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here


window.exitonclick()
