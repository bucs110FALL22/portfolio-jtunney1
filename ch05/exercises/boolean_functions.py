def percentage_to_letter(score=0):
   if score >= 90:
     return "A"
   elif score > 80:
     return "B"
   elif score > 70:
     return "C"
   elif score > 60:
     return "D"
   else:
     return "F"
def is_passing(letter=None):
  if letter == "A" or letter == "B" or letter == "C":
    return True
  else:
    return False
def main_function():
  grade = int(input("Input grade percentage as whole number: "))
  letter_grade = percentage_to_letter(score=grade)
  pass_or_fail = is_passing(letter=letter_grade)
  return pass_or_fail
print(main_function())