import random

rand_num = int(random.randint(1,11))
chosen_num_one = int(input("Guess a number between 1 and 10! (3 tries): "))

if rand_num < chosen_num_one:
  result = "wrong"
  print("Too high")

if rand_num > chosen_num_one:
  result = "wrong"
  print("Too low")

if rand_num == chosen_num_one:
  result = "correct"
  print("correct!")
  print("random number was ", rand_num)

if result == "wrong":
  chosen_num_one = int(input("Guess a number between 1 and 10! (2 Tries left): "))

  if rand_num < chosen_num_one:
    result = "wrong"
    print("Too high")

  if rand_num > chosen_num_one:
   result = "wrong"
   print("Too low")

  if rand_num == chosen_num_one:
   result = "correct"
   print("correct!")
   print("random number was ", rand_num)

  if result == "wrong":
   chosen_num_one = int(input("Guess a number between 1 and 10! (1 Tries left): "))

   if rand_num < chosen_num_one:
     result = "wrong"
     print("Too high")

   if rand_num > chosen_num_one:
     result = "wrong"
     print("Too low")

   if rand_num == chosen_num_one:
     result = "correct"
     print("correct!")
     print("random number was", rand_num)

  if result == "wrong":
   print("Out of guesses")
   print("random number was", rand_num)