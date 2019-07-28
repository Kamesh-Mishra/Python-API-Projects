import requests
import dateutil.parser
from pyfiglet import figlet_format
from termcolor import colored

#for support in windows of pyfiglet and termcolor
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
#-----------------------------------------------

header = figlet_format("WEATHER", font = "digital")
title = colored(header, color="cyan")
print(title)

city = input("Please Enter the city for weather: ")
url = "http://api.openweathermap.org/data/2.5/weather?appid=69f8b71e3891d8308a7ff76d950cfee8&q="+city
res = requests.get(url).json()
print(f"The current whether shows it to be {res['weather'][0]['main']} - {res['weather'][0]['description']}")

input("\n*****THANK YOU*****")
