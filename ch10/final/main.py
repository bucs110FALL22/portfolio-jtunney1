from Holidays import Holidays

def main():
  holidays = Holidays()
  get = holidays.get()
  result = holidays.most_cases_day(get)
  holidays.end_message(result)
  
main()