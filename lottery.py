'''
An implementation of the riddle in python.
For testing purposes of other implementations for low numbers of participants.
'''

import os, sys

def main(n = 4, testFun):
    '''
    For each permutation of boxes,
    test the given function and display its success rate.
    '''

def simpleStrategy(idNumber, previousGuessesAndResults, numberOfBoxes):
    '''
    Given the id number of a participant,
    their previous guesses and their results,
    and the number of boxes total,
    return the next guess of the participant.
    _We are assuming that each participant has the same basic strategy._
    '''
    partial = 0
    if len(previousGuessesAndResults) == 0:
        partial = 0
    else:
        # add one to our previous guess
        partial = previousGuessesAndResults[-1][0] + 1

    return partial + (0 if idNumber < 51 else 50)


if __name__ == "__main__":
    main()
