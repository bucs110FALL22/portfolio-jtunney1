import time

class Animal:
  def __init__(self,name,type):
    self.name = name
    self.type = type
    self.code = id(self)
    self.found = time.strftime("%d/%m/%Y")
    self.adopted = None

  def setAdopted(self):
    self.adopted = time.strftime("%d/%m/%Y")

  def setDate(self,date=" "):
    self.adopted = date

def main():
  dog = Animal("Max","Dog")
  dog.setAdopted()
  print(dog)
main()
    
    

