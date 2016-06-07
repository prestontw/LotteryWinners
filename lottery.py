'''
An implementation of the riddle in python.
For testing purposes of other implementations for low numbers of participants.
'''

import os, sys
from itertools import permutations

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


def main(n = 4, participantStrategyFunction = simpleStrategy, beneficiaryStrategyFunction = identityConfiguration):
    '''
    For each permutation of boxes,
    test the given function and display its success rate.
    '''

    boxes = [x for x in range(n)]

    numConfigurations = 0
    passedConfigurations = 0
    
    for configuration in permutations(boxes):
        # try the strategies
        possiblyAlteredConfiguration = beneficiaryStrategyFunction(list(configuration))
        successful = testConfiguration(possiblyAlteredConfiguration, participantStrategyFunction)

        print(configuration, "->", possiblyAlteredConfiguration, ":", end=" ")
        if successful:
            passedConfigurations += 1
            print("passes")
        else:
            print("fails")
        numConfigurations += 1

    print("Out of", numConfigurations, "the strategy worked for", passedConfigurations)
    print(passedConfigurations / numConfigurations * 100, "%", sep="")


def testConfiguration(configuration, strategy):
    '''
    Return whether the given strategy works for the configuration of boxes.
    '''
    for participant in range(len(configuration)):
        if not testParticipant(configuration, participant, strategy):
            return False
    # else strategy works for everyone
    return True


def testParticipant(configuration, participantID, strategyFunction):
    '''
    Given a configuration of boxes,
    return if the participant can find their number.
    '''
    results = []
    for numAttempts in range(len(configuration) // 2):
        boxIndex = strategyFunction(participantID, results, len(configuration))
        boxNumer = configuration[boxIndex]
        if boxNumer == participantID:
            return True
        else:
            results.append((boxIndex, boxNumer))

    return False


if __name__ == "__main__":
    main()
