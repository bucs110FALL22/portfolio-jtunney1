from Rectangle import Rectangle

class Surface:
  def __init__(self,filename=" ",x=0,y=0,h=0,w=0):
    #takes arguments creates instance variable for rectangle with x,y,h,w. Also sets self.image to argument filename
	  #args: x,y,h,w integers and filename which is a string
	  #return: sets self.rect and self.image instance variable values
    self.rect = Rectangle(x,y,h,w)
    self.image = str(filename)

  def getRect(self):
    #returns the self.rect value
	  #args: self
	  #return: self.rect
    rect = self.rect
    return rect
    
