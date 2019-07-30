import requests
from pyfiglet import figlet_format
from termcolor import colored

#for support in windows of pyfiglet and termcolor
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
#-----------------------------------------------

header = figlet_format("Movies API by OMDB", font = "digital")
title = colored(header, color="cyan")
print(title)
print("*API used is OMDB API*")

url = "http://www.omdbapi.com/?apikey=1e7224be&"

print("Please Enter the details that you know, skip the rest:")
imdb_id = input("> IMDB ID : ")
title = input("> Title : ")
type_ = input("> Type(series,movie,episode) : ")
y = input("> Year of Release : ")

key = dict()
key['i'] = imdb_id
key['t'] = title
key['type'] = type_
key['y'] = y

r = requests.get(url, params = key).json()

try:
    print(colored(figlet_format((f"{r['Title']}"), font = "digital"), color = "red"))
    print(colored("Year : ", color = "red"), end="");print(f"{r['Year']}")
    print(colored("Rated : ", color = "red"), end="");print(f"{r['Rated']}")
    print(colored("Released : ", color = "red"), end="");print(f"{r['Released']}")
    print(colored("Genre : ", color = "red"), end="");print(f"{r['Genre']}")
    print(colored("IMDB Rating : ", color = "red"), end="");print(f"{r['imdbRating']}")
    print(colored("Box Office Collection : ", color = "red"), end="");print(f"{r['BoxOffice']}")
    print(colored("Production : ", color = "red"), end="");print(f"{r['Production']}")
except:
    print("Something went wrong")
input("\n*****THANK YOU*****")
