import requests
import dateutil.parser
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("COMMITS")
title = colored(header, color="cyan")
print(title)

user = input("Please Enter your username : ")
repo = input("Please Enter your repository name: ")

url = "https://api.github.com/repos/"+user+"/"+repo+"/commits"

commits = requests.get(url, headers = {"Accept":"application/json"}).json()

print(f">>> You have {len(commits)} commits in this repository")

for k in commits:
    datetime_str = dateutil.parser.parse(k['commit']['committer']['date'])
    print(">>>",k['sha'])
    print("Created on : ", datetime_str)
    print("Created by : ", k['commit']['author']['name'])
    print("Message : ", k['commit']['message'])

input("*****THANK YOU*****")
