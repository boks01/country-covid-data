from email import message
import requests
import smtplib
import datetime as dt
import requests

covid_url = "https://coronavirus-19-api.herokuapp.com/countries"

now_date = dt.datetime.now()
date = now_date.strftime("%d-%b-%y  %X")
world_data = None
country_data = None
response = requests.get(covid_url)
result = response.json()

for i in result:
    if i['country'] == "World" or i['country'] == "Indonesia":
        country_name = i['country']
        country_cases = i['cases']
        country_today_cases = i['todayCases']
        country_total_recovered = i['recovered']
        country_today_death = i['deaths']
        if country_name == "World":
            world_data = {
                "country_name" : country_name,
                "total_cases" : country_cases,
                "today_cases" : country_today_cases,
                "recovered" : country_total_recovered,
                "death" : country_today_death,
            }

        else:
            country_data = {
                "country_name" : country_name,
                "total_cases" : country_cases,
                "today_cases" : country_today_cases,
                "recovered" : country_total_recovered,
                "death" : country_today_death,
            }

# add to sheety
sheety_url = "https://api.sheety.co/073f31df6c60be1e403436d7f3df689e/countryCovidData/datas"
params = {
    "data":{
        "date" : date,
        "name" : country_data['country_name'],
        "total" : country_data['total_cases'],
        "today" : country_data['today_cases'],
        "recovered" : country_data['recovered'],
        "death" : country_data['death'],
        }
}
response = requests.post(sheety_url, json=params)
print(response.text)
# add to sheety

# print(f"Subject:World and indonesia today cases\n\n\n{date}\n{world_data}\n{country_data}")