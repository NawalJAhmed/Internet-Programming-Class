#Author: Nawal Ahmed
#Assignment 5
#Must have requests imported in Pycharm else it will not work

import requests
import datetime as dt

user_id ="nawaljahmed"
user_apiid = "52cc6258a39ae74095b40b8da8a89fb4"

zipcode="30043"      # Zipcode of city (Current is Lawrencevile, GA)
country="US"     # Specify in two letters if not specified default US will be considered.
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?zip="+zipcode+","+country+"&appid="+user_apiid)

# Get json data
data=response.json()

# Printing Table

print('{0:30}  {1}'.format("Name:", data['name']))
print('{0:30}  {1} {2}'.format("Current Temperature:",
                           data['main']['temp']," degrees Kelvin"))
print('{0:30}  {1} {2}'.format("Atmospheric Pressure:", data['main']['pressure'] , " hPa"))
print('{0:30}  {1} {2}'.format("Wind Speed:", data['wind']['speed']," mph"))
print('{0:30}  {1}'.format("Wind Direction:", data['wind']['deg']))
print('{0:30}  {1}'.format("Time of Report:", dt.datetime.utcfromtimestamp(
    data['dt']).strftime('%m-%d-%Y %H:%M:%S' " UTC")))


"""
Sample Output
Name:                     KSU
Current Temperature:      64.5 degrees Fahrenheit
Atmospheric Pressure:     992.52 hPa
Wind Speed                10.6 mph
Wind Direction            289.5
Time of Report            2017-03-10 11: 13: 24
"""
