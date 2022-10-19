def multiply(x=0,y=0):
  num = 0
  for i in range(y):
    num = num + x
  return num
def exponent(x=0,y=0):
  num = 1
  for i in range(y):
    num = num * x
  return num
def square(num=0):
  square = multiply(x=num,y=num)
  return square

def main():
  print(multiply(5,7))
  print(exponent(3,4))
  print(square(3))

main()