class Rectangle:
  def __init__(self, x=0, y=0, h=0, w=0):
    #takes arguments and sets instance variables with those values
	  #args: x,y,h,w integers 
	  #return: set self.value as argument value
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    if self.x < 0:
      self.x = 0
    if self.y < 0:
      self.y = 0
    if self.height < 0:
      self.height = 0
    if self.width < 0:
      self.width = 0
  def __str__(self):
    #returns values of __init__ function
	  #args: self only
	  #return: returns values of self.x,self.y,self.height, and self.width
    string = str.format("(x:{}, y:{}), height:{}, width{}".format(self.x,self.y, self.height,self.width))
    return string

