class Player:
  def __init__(self):
    self.speed = 3
    self.health = 3
    self.jump_height = 10

class Enemy:
  def __init__(self,pos):
    self.position = pos
    self.lives = 1
    self.damage = -1

class Obsticles:
  def __init__(self,pos,color):
    self.position = pos
    self.color = color
    self.is_large = False
    


    
  