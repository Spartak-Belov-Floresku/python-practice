"""Special Word Finder: cleans up a dictionary from white spaces and comments, finds random words from a dictionary."""
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):

    """
    >>> word = SpecialWordFinder()
    3 of words read

    >>> word.random() in ['dog','cat','cow']
    True

    >>> len(word.cleanUpList()) == len(['dog','cat','cow'])
    True
    
    """

    def __init__(self):
        '''
        initiation method of the class SpecialWordFinder
        ______________________________________________________

        initiating the superclass and calls cleanUpList method

        '''
        super().__init__()

    def cleanUpList(self):
        '''
        cleans up list of words of the parent class from empty elements and pound(#)
        '''
        return [word for word in self.listOfWords if not word.startswith('#') and word.strip()]

