'''
A template implementation of the functions for both the participants and the beneficiary.
'''

import os, sys
from lottery import main

def simpleStrategy(idNumber, previousGuessesAndResults, numberOfBoxes):
    '''
    Given the id number of a participant,
    their previous guesses and their results,
    and the number of boxes total,
    return the next guess of the participant as an index [0, n).
    _We are assuming that each participant has the same basic strategy._
    '''
    partial = 0
    if len(previousGuessesAndResults) == 0:
        return 0 if idNumber < numberOfBoxes // 2 \
            else numberOfBoxes // 2
    else:
        # add one to our previous guess
        return previousGuessesAndResults[-1][0] + 1


def identityConfiguration(configuration):
    return configuration


def makeConfigurationAscending(configuration):
    pivot = len(configuration) // 2
    for index in range(pivot):
        if configuration[index] >= pivot:
            # then start looking for a small number to the right of pivot
            for switchIndex in range(pivot, len(configuration)):
                if configuration[switchIndex] < pivot:
                    # then swap the two numbers
                    temp = configuration[index]
                    configuration[index] = configuration[switchIndex]
                    configuration[switchIndex] = temp

                    return configuration

    # else given configuration works
    return configuration


if __name__ == "__main__":
    main(6, simpleStrategy, makeConfigurationAscending)
