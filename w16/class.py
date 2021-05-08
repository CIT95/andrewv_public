import sys
import requests
from hangDude import hangImg


class HangDude:
    def __init__(self):
        self.wrongGuesses = 0
        self.lettersTried = []
        self.word = ''
        self.hint = ''
        self.URL = 'http://puzzle.mead.io/puzzle'
        self.parameters = {'wordCount': 1}

    def start(self):
        self.getWord()
        self.getHint()
        self.printScreen()

    def getWord(self):
        response = requests.get(self.URL, params=self.parameters)
        if response.status_code == 200:
            self.word = response.json()['puzzle']
        else:
            print("Error: Unable to fetch data")
            sys.exit(1)

    def getHint(self):
        for letter in self.word:
            self.hint += ' ' if letter == ' ' else '_'

    def printScreen(self):
        print(hangImg[self.wrongGuesses], *self.hint)


class Hard(HangDude):
    def __init__(self):
        super().__init__()
        self.parameters = {'wordCount': 2}


class Impossible(HangDude):
    def __init__(self):
        super().__init__()
        self.parameters = {'wordCount': 4}


normal = HangDude()
hard = Hard()
impossible = Impossible()

normal.start()
hard.start()
impossible.start()
