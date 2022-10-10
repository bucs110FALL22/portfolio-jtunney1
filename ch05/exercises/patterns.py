def star_pyramid():
  user_number = int(input("How many lines do you want for pyramid?: "))
  for i in range(user_number + 1):
    print("*" * i)

def rstar_pyramid():
  user_input = int(input("How many lines do you want for pyramid?: "))
  for i in range(user_input):
    print("*" * (user_input - i))

star_pyramid()
rstar_pyramid()
