"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    """
    >>> word = WordFinder()
    3 of words read

    >>> word.random() in ['dog','cat','cow']
    True
    
    """

    def __init__(self, path = "words.txt"):
        '''
        initiation method of the class WordFinder
        __________________________________________________________________

        att is used to operate in the class
        self.path = (default pyth to the txt file)

        att is used to hold all words for the text file as a list
        self.arrayOfWords = []

        the method starts to read a text file and sends the words to the list
        self.readFile()

        '''
        self.path = path
        self.listOfWords = []
        self.readFile()

    def readFile(self):
        '''
        the method starts to read the text file and sends the words to the list, also it prints out amount of words that are read
        '''
        with open(self.path) as f:
            self.listOfWords = [word.rstrip() for word in f]
        print(f'{len(self.listOfWords)} of words read')
    
    def random(self):
        '''
        the method is used to get a random word from the list
        '''
        return self.listOfWords[random.randint(0, len(self.listOfWords)-1)]

