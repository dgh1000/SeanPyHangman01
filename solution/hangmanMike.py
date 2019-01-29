# http://www.gwicks.net/dictionaries.htm

import re
from functools import partial

# not really necessary


def mapl(f, l):
    return list(map(f, l))

def filterl(f, l):
    return list(filter(f, l))

def snd(t):
    return t[1]


def fst(t):
    return t[0]


# ------------------------------------------------------------
# more necessary


def mkLetter(c):
    return (c, False)

def matchesLetter(l, t):
    return l == t[0]

    
def setLetterStatus(l, t):
    letter, _ = t
    if l == letter:
        return (letter, True)
    else:
        return t

def numMatched(word):
    return sum(mapl(snd, word))

def toDisplay(word):
    xs = [c if flag else '_' for (c, flag) in word]
    return "".join(xs)

def getInput(alreadyGuessed):
    while True:
        s = input("Enter a letter:")
        if re.match(r'[a-z]$', s):
            if s in alreadyGuessed:
                print("You already guessed that. Try something else.")
            else:
                return s
        else:
            print("You must enter a single lowercase letter.")
    
def countUnmatched(word):
    return sum([0 if flag else 1 for _, flag in word])

def testDict():        
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        for l in lines[100000:100100]:
            print(l.strip())

def main():
    word = [(c, False) for c in "ham"]
    alreadyGuessed = set()
    numWrong = 0
    maxNumWrong = 4
    while numWrong < maxNumWrong:
        print(toDisplay(word))
        newLetter = getInput(alreadyGuessed)
        alreadyGuessed.add(newLetter)
        if any([matchesLetter(newLetter, c) for c in word if not c[1]]):
            print("A match!")
            word = [setLetterStatus(newLetter, c) for c in word]
            if countUnmatched(word) == 0:
                print(" AND YOU WIN!")
                print(toDisplay(word))
                quit()
        else:
            print ("Sorry, dude. Bad guess.")
            numWrong += 1
            print ("You've made {} mistakes so far.".format(numWrong))
            print (("And have {} mistakes remaining " +
                    "before it's all over.").format(maxNumWrong - numWrong))
    print("Sorry to inform you, this is the end. Good luck in the afterlife.")


testDict()
