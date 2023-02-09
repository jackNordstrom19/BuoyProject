'''
buoy_io - The input and output handler for the terminal
'''


class buoy_io:

    '''
    __init__ - The buoy_io constructor
    '''

    def __init__(self):

        pass

    '''
    display - Displays the incoming string

    param string: The incoming string
    '''

    def display(self, string):

        print(string)

    '''
    getInput - Gets input from the buoy

    param input: The incoming input
    '''

    def getInput(self, input):

        return input.readline()
