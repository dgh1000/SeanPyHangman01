def main():
    while True:
        if "y" == input('Type "y" to Continue').lower():
            response = True
        else:
            response = False

        if response:
            gameloop()
        else:
            break

def wordGuess():

    letter_guess = input("Guess a letter").lower()

    return letter_guess


def wordPresent(word):
    for t in word:
        print(t[0] if t[1] else " _ ")

def createWordpule(word):

    wordpule = []

    for letter in word:
        wordpule.append((letter, False))

    return wordpule



def guessCheck(letter_guess, letterList):

    elcount = 0
    letter_found = False

    for l,v in letterList:

        if letter_guess == l:
            letter_found = True
            letterList[elcount] = (letter_guess, True)

        elcount += 1

    if letter_found:
        print("Yay {} is in the word.".format(letter_guess))

    else:
        print("Sorry fool")

def gameCheck(wordList):

    gCheck = []
    for l,v in wordList:
        gCheck.append(v)

    if False in gCheck:
        return False
    else:
        return True

    '''   
    if False in wordList[:][1]:
        return False

    else:
        return True
    '''

def gameloop():
    print("Gameloop Run")

    wordtoguess = "michaelmos"


    wordListuple = createWordpule(wordtoguess)

    gameOn = True
    guessCount = 0

    while gameOn:

        wordPresent(wordListuple)
        guessCheck(wordGuess(),wordListuple)


        if gameCheck(wordListuple):
            print("YOU WIN")
            break

        elif guessCount >= (len(wordtoguess) + 4):
            print("YOU LOSE")
            break
        else:
            guessCount += 1




 #   wordier = [("m", True), ("i", False), ("c", True), ("h", False), ("a", True), ("e", True), ("l", False)]






def presentGallow():
    pass

def checkWin():
    pass

if __name__ == '__main__':
    main()


'''
HIGHLEVEL
- Loop through game decision options
---- Accept entry of whether or not the person wants to play again
---- if yes:
-------- call gameloop()
---- else:
-------- end the game by breaking game decision loop


Def gameloop():
- Select a word
- Present word and gallows (should it go here?)
- Loop until player wins or loses:
---- Present word and body parts (should it go here also, or only?)
---- Accept guess of letter
---- Check if letter is in selected word
-------- If letter is in selected word
------------ If the player has guessed all of the letters in the word
---------------- Present the “You Win” message
---------------- break
-------- If letter is not in selected word
------------ If the player has guessed incorrectly 6 times
---------------- Present “Game Over” message
---------------- break

MIDDLE LEVEL
X Select a word
- From a table, select a list of words that have not been flagged as guessed
- Assign selected word to a list called "word"
- Split the word into tuples where the letter is the first element of the tuple
and "False" is the second element of the tuple.
- Present word and gallows (should it go here?)
- Print an em
- Loop until player wins or loses:
---- Present word and gallows (should it go here also, or only?)
---- Accept guess of letter
---- Check if letter is in selected word
-------- If letter is in selected word
------------ If the player has guessed all of the letters in the word
---------------- Present the “You Win” message
---------------- Present Do you want to play again message
------------ If the player has not guessed all of the letters in the word
---------------- Present all instances of letter in word, in their appropriate space
---------------- Accept guess of letter
-------- If letter is not in selected word
------------ If the player has guessed incorrectly 6 times
---------------- Present “Game Over” message
---------------- Present Do you want to play again message
------------ If the player has guessed incorrectly less than 6 times
---------------- Present next body part
---------------- Accept guess of letter
'''
