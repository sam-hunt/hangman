import random
from typing import List, Set

def getRandomWord() -> str:
    words: List[str] = ['computer', 'keyboard', 'mouse', 'software', 'storage', 'document', 'python', 'scratch']
    return random.choice(words)

def obscuredWord(word: str, guessesSoFar: Set[str]) -> str:
    return ' '.join(['_' if letter not in guessesSoFar else letter for letter in word])

def hasWon(word: str, guessesSoFar: Set[str]) -> bool:
    return word in guessesSoFar or '_' not in obscuredWord(word, guessesSoFar)

if __name__ == '__main__':
    print('\nHi ' + input('What\'s your name? ') + '!')
    playAnotherRound: str = 'y'

    while len(playAnotherRound) > 0 and playAnotherRound[0].lower() == 'y':
        livesLeft: int = 10
        guessesSoFar: Set[str] = set()
        word: str = getRandomWord()

        print('I\'m thinking of a word with ' + str(len(word)) + ' letters!')

        while livesLeft > 0 and not hasWon(word, guessesSoFar):
            print('\nYou have ' + str(livesLeft) + ' lives left.')
            print('Your guesses so far: ' + ', '.join(list(guessesSoFar)))
            print(obscuredWord(word, guessesSoFar))

            guess: str = input('Guess a letter or word: ')
            if guess in guessesSoFar:
                continue
            guessesSoFar.add(guess)
            livesLeft = livesLeft - 1

        print('\nCongratulations, you won!' if hasWon(word, guessesSoFar) else '\nYou\'ve run out of lives!')
        playAnotherRound = input('Play again? (y/N) ')
        print()

    print('Thanks for playing!')
