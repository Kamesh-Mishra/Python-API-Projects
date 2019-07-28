import requests
from pyfiglet import figlet_format
from termcolor import colored

#for support in windows of pyfiglet and termcolor
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
#-----------------------------------------------

header = figlet_format("Google Books", font = "digital")
title = colored(header, color="cyan")
print(title)

url = "https://www.googleapis.com/books/v1/volumes?key=AIzaSyDxvPq1jVAW3lQX4Mb9qqgehj6a9dF8q8Q&q="
print("Search a book by \n > Title\n > Author\n > Publisher\n > ISBN")
print("How would you like to search for the book? \n*You can enter multiple search parameters*\n*Press Enter Key when done* : ")
search_list = []
allowed_par = ['title', 'author', 'publisher', 'isbn']
while True:
	a = input().lower()
	if a =="":
		print("**Parameters Taken for Search")
		break
	if a not in allowed_par:
		print("**This is not an allowed parameter. Enter again>>")
		continue
	search_list.append(a)

max_res = input("How many results do you want: ")

q = dict()
print("Enter the details : ")
for i in search_list:
	q[i] = input(f"{i} : ")

if 'title' in search_list:
	url = url + q['title']
if 'author' in search_list:
	url = url + "+inauthor:" + q['author']
if 'publisher' in search_list:
	url = url + "+inpublisher:" + q['publisher']
if 'isbn' in search_list:
	url = url + "+isbn:" + q['isbn']

res = requests.get(url, params={'maxResults':max_res}).json()

res = res['items']
print("****************")
for i in range(len(res)):
	print(colored(figlet_format((f"Title : {res[i]['volumeInfo']['title']}"), font = "digital"), color = "red"))
	if 'subtitle' in res[i]['volumeInfo'].keys():
		print(colored("SubTitle : ", color = "red"), end="");print(f"{res[i]['volumeInfo']['subtitle']}")
	if 'description' in res[i]['volumeInfo'].keys():
		print(colored("Description : ", color = "red"), end="");print(f"{res[i]['volumeInfo']['description']}")
	a = [x for x in res[i]['volumeInfo']['authors']]
	print(colored("Authors : ", color = "red"), end="");
	for j in a:
		print(j,end =",")
	print("")
	print(colored("Publisher : ", color = "red"), end="");print(f"{res[i]['volumeInfo']['publisher']}")
	print(colored("Published Year : ", color = "red"), end="");print(f"{res[i]['volumeInfo']['publishedDate']}")
	print(colored("ISBN10 : ", color = "red"), end="");print(f"{res[i]['volumeInfo']['industryIdentifiers'][0]['identifier']}")
	print(colored("ISBN13 : ", color = "red"), end="");print(f"{res[i]['volumeInfo']['industryIdentifiers'][1]['identifier']}")
	print("****************")


input("\n*****THANK YOU*****")
