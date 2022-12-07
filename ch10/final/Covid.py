import requests
import json

class Covid():
  def __init__(self):
    #initalizes Covid class
    #only argument is self
    #no return values
    pass

  def get(self,date):
    #gets json data for chosen date
    #agrs: self and which date
    #returns cases on choosen day or 0 if no data exists
    self.api_url = "https://api.covidtracking.com/v2/us/daily/" + str(date) + "/simple.json"
    response = requests.get(self.api_url).json()
    check_status = requests.get(self.api_url)
    if check_status.status_code == 200:
      cases_on_day = response['data']['cases']['total']
      return cases_on_day
    else:
      return 0

