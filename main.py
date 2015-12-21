

def main():
    baseWord = getMainWord()
    baseWordSplat = list(baseWord)
    wordList = []
    getWords(wordList)
    compTotalResultList = engine(wordList, baseWordSplat)
    print('\nDifferences from', baseWord, 'based on ASCII values per character (somewhat pointless): \n')

    for each in range (0, len(compTotalResultList)):
        if compTotalResultList[each] < 0:
            print(wordList[each], ' - ', -1*compTotalResultList[each] )
        else:
            print(wordList[each], ' - ', compTotalResultList[each] )

    ending()


def ending():
    yn = input('\nWould you like to try again? Y/N\n')

    if yn == 'y' or yn == 'Y':
        main()
    elif yn == 'n' or yn == 'N':
        exit()
    else:
        print('Please type Y to continue or N to exit\n')
        ending()


def engine(wordList, baseWordSplat):
    compTotalResultList = []
    baseTotal = 0

    for letter in baseWordSplat:
        baseTotal += ord(letter)

    for word in wordList:
        compTotalResult = 0
        wordSplat = list(word)
        for letter in wordSplat:
            compTotalResult += ord(letter)
        compTotalResultList.append(baseTotal - compTotalResult)

    return(compTotalResultList)


def getMainWord():
    baseWord = input('Please type the main word you wish to compare against.\n')

    if baseWord.isalpha() == False:
        print('Only letters. No numbers.')
        getMainWord()

    return(baseWord)


def getWords(wordList):
    currentWord = input('Please type the words you wish to compare to the main word. Type nothing and Press enter when finished.\n')

    if currentWord == '':
        return(wordList)
    elif currentWord not in wordList:
        wordList.append(currentWord)
        getWords(wordList)
    else:
        print('Word already registered\n')
        getWords(wordList)



main()