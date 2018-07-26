from pyfiglet import Figlet
from termcolor import colored
import requests
from random import randint

print(colored(Figlet().renderText("Dadjokinator"), "blue"))

topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={
        "Accept": "application/json"
    },
    params={
        "term": topic
    }
)

# print(response.json()["results"])
results = response.json()["results"]
resultsLen = len(results)
if (resultsLen == 0):
    print(f"Sorry, I don't have any jokes about {topic}! Please try again")
elif (resultsLen == 1):
    print(f"I've got one joke about {topic}. Here it is:")
    print(results[0]["joke"])
else:
    index = randint(0, resultsLen - 1)
    print(f"I've got {resultsLen} jokes about {topic}. Here's one:")
    print(results[index]["joke"])
