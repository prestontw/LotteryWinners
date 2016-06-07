'''
An implementation of the riddle in python.
For testing purposes of other implementations for low numbers of participants.
'''

import os, sys
from itertools import permutations

def simpleStrategy(idNumber, previousGuessesAndResults, numberOfBoxes):
    '''
    Sample strategy used by default in running of the lottery program.
    ***
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


def makeConfigurationAscending(configuration):
    '''
    Sample strategy of the beneficiary used in running of the lottery.
    '''
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

def main(n = 4,\
         participantStrategyFunction = simpleStrategy,\
         beneficiaryStrategyFunction = makeConfigurationAscending):
    '''
    For each permutation of boxes,
    test the given function and display its success rate.
    '''

    boxes = [x for x in range(n)]

    numConfigurations = 0
    passedConfigurations = 0
    prepassedConfigurations = 0

    output = ""
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'
    
    for configuration in permutations(boxes):
        # try the strategies
        possiblyAlteredConfiguration = beneficiaryStrategyFunction(list(configuration))

        unalteredSuccessful = testConfiguration(list(configuration), participantStrategyFunction)
        successful = testConfiguration(possiblyAlteredConfiguration, participantStrategyFunction)

        print((GREEN if unalteredSuccessful else RED) + str(configuration) + END + \
              " -> " + \
              (GREEN if successful else RED) + str(possiblyAlteredConfiguration) + END, sep = "")
        if successful:
            passedConfigurations += 1
        if unalteredSuccessful:
            prepassedConfigurations += 1
        numConfigurations += 1

    print(output)
    print("Out of", numConfigurations, "the strategy worked for", prepassedConfigurations, "before the beneficiary")
    print("Out of", numConfigurations, "the strategy worked for", passedConfigurations, "after the beneficiary")
    print(prepassedConfigurations / numConfigurations * 100, "% versus ",\
          passedConfigurations / numConfigurations * 100, "%", sep="")


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
    main(4, simpleStrategy, makeConfigurationAscending)
