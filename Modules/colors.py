from pyfiglet import Figlet
from termcolor import colored, COLORS

text = input("What message do you want to print? ")
color = input("What color? ")

if color not in COLORS.keys():
    color = 'white'

# this is a really long comment that probably should be set over a couple
# of lines and cleaned up.
print(colored(Figlet().renderText(text), color))
