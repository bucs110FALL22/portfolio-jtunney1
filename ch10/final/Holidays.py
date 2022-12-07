import requests
import json
from Covid import Covid

class Holidays():
  def __init__(self):
    #initializes Holidays class 
    #only arguement is self
    #sets api_url for class
    self.api_url = "https://date.nager.at/api/v3/PublicHolidays/2021/US"

  def get(self):
    #gets json data from url
    #only argument is self
    #returns the json from the url
    response = requests.get(self.api_url).json()
    #print(response)
    return response

  def most_cases_day(self,response):
    #Finds which US holiday in 2021 had highest covid cases
    #arguments are self and response which is json file
    #returns a tuple of name of holiday with highest cases and that days amount of cases
    highest_cases = 0
    list_length = len(response) - 1
    for index in range(list_length):
      day_name = response[index]['name']
      day_date = response[index]['date']
      call = Covid()
      cases = call.get(day_date)
      if cases > highest_cases:
        highest_cases = cases
        highest_day = day_name
    highest_list = (str(highest_day),str(highest_cases))
    return highest_list

  def end_message(self,message):
    #takes the holiday and amount of cases and prints it in context
    #args: self and message which is a tuple with the amount of cases and name of holiday
    #prints the message
    message = 'The holiday with the most amount of recorded Covid-19 cases in the United States in 2021 was: ' + message[0] + ' with: ' + message[1] + " number of positive cases"
    print(message)
