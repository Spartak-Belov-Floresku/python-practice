"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        '''
        initiation method of the class SerialGenerator
        __________________________________________________

        property is used to operate in the class
        self.start = (int or float)

        property is used to hold the original start number
        self.default = self.start
        
        '''
        self.start = start
        self.default = self.start

    def generate(self):
        '''
        the method increases the amount of the start number by one time per run
        '''
        a = self.start
        self.start += 1
        return a
    
    def reset(self):
        '''
        the method is used to reset to the original number
        '''
        self.start = self.default

    def __repr__(self):
        '''
        returns string description of the class
        '''
        return f'<SerialGenerator start={self.start} next={self.start+1}>'


