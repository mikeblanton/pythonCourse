from pyfiglet import Figlet
from termcolor import colored, COLORS

text = input("What message do you want to print? ")
color = input("What color? ")

if color not in COLORS.keys():
    color = 'white'

print(colored(Figlet().renderText(text), color))
