import requests
import json

#specify the api parameters its a dictionary of mandatory data:API_KEY,country,year(it should be less an year equal to the previous year)

params = {
    "key":"4b65ae7f-e486-40c1-80d1-ff8c252a964d",
    "country":"Kenya",
    "year":2022
    
}
#url of the holidayapi website
url = "https://holidayapi.com/v1/countries"

#getting the data
req = requests.get(url,params=params)
print(req.json())

with open("holiday_data.json","w") as f:
    json.dump(req.json(),f)