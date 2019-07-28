import requests
import dateutil.parser
from pyfiglet import figlet_format
from termcolor import colored

#for support in windows of pyfiglet and termcolor
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
#-----------------------------------------------

header = figlet_format("github")
title = colored(header, color="cyan")
print(title)

user = input("Please Enter your username : ")

url = "https://api.github.com/users/"+user

pro = requests.get(url, headers = {"Accept":"application/json"}).json()

print(f">>> Welcome {pro['name']} to github app.")
print(f"***{pro['name'].upper()}***")
print(f">> Email: {pro['email']}")
print(f">> Location: {pro['location']}")
print(f">> Bio: {pro['bio']}")
print(f">> Followers: {pro['followers']}")
print(f">> Your URL: {pro['html_url']}")

url_repo = "https://api.github.com/users/"+user+"/repos"

repos = requests.get(url_repo, headers = {"Accept":"application/json"}).json()

print(f">> Total Repositories: {pro['public_repos']}")
print(">> Here are your Repositories:")

for k in repos:
    print(">> ",k['name'])

    
input("*****THANK YOU*****")
