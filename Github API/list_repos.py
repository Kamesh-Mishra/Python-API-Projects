import requests
import dateutil.parser
from pyfiglet import figlet_format
from termcolor import colored

#for support in windows of pyfiglet and termcolor
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
#-----------------------------------------------

header = figlet_format("REPOS")
title = colored(header, color="cyan")
print(title)

user = input("Please Enter your username : ")

url = "https://api.github.com/users/"+user+"/repos"

repos = requests.get(url, headers = {"Accept":"application/json"}).json()

print(f">>> You have {len(repos)} Repositories.")

for k in repos:
    datetime_str = dateutil.parser.parse(k['created_at'])
    print(">>>",k['name'])
    print("Created on : ", datetime_str)
    print("Clone URL : ", k['clone_url'])
    print("Forks : ", k['forks'])
    print("Open Issues : ", k['open_issues_count'])
    
input("*****THANK YOU*****")
