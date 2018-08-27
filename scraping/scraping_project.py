# Game which scrapes quotes from http://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
from random import choice


def scrape_birth(url):
    response = requests.get(f"http://quotes.toscrape.com{url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    birth_year = soup.select('.author-born-date')[0].get_text()
    birth_place = soup.select('.author-born-location')[0].get_text()
    return f"The author was born on {birth_year} {birth_place}"


def scrape_quote(quote):
    text = quote.find(itemprop='text').get_text()
    author = quote.find(itemprop='author').get_text()
    name_parts = author.split()
    first_initial = name_parts[0][0]
    last_initial = name_parts[len(name_parts) - 1][0]
    bio = quote.find('a')['href']
    return {'text': text, 'author': author, 'bio': bio, 'first_initial': first_initial, 'last_initial': last_initial}


def scrape_quotes():
    has_more = True
    quotesArray = []
    url = 'http://quotes.toscrape.com'
    while has_more:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.select('.quote')
        for quote in quotes:
            quotesArray.append(scrape_quote(quote))
        next = soup.select('.next')
        if len(next) == 1:
            nextUrl = next[0].find('a')['href']
            url = f"http://quotes.toscrape.com{nextUrl}"
            has_more = True
        else:
            has_more = False

    return quotesArray


def guess_quote(quotes):
    quote = choice(quotes)
    print(quote['text'])
    print()
    incorrect = True
    num_guesses = 4
    while incorrect:
        guess = input(f"Who said this? Guesses remaining: {num_guesses}. ")
        num_guesses -= 1
        if (guess == quote['author']):
            print("You guess correctly! Congratulations!")
            incorrect = False
        else:
            if (num_guesses == 3):
                print(f"Here's a hint: {scrape_birth(quote['bio'])}")
            elif (num_guesses == 2):
                print(f"Here's a hint: The author's first name starts with {quote['first_initial']}")
            elif (num_guesses == 1):
                print(f"Here's a hint: The author's last name starts with {quote['last_initial']}")
            else:
                incorrect = False
                print(f"Sorry! You guessed incorrectly! The author is {quote['author']}.")


def play():
    cont = True
    quotes = scrape_quotes()
    while cont:
        guess_quote(quotes)
        print()
        more = input("Would you like to play again (y/n)? ")
        if (more != 'y'):
            cont = False
            print("Ok! Maybe next time then...")
        else:
            print("Great! Here we go again...")
            print()


print('Loading quotes, please wait...')
print()
play()
