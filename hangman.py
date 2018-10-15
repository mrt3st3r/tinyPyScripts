"""
A simple hangman game.
doesn't include any input data validations
"""

def main():

    secret = 'EVAPORATE'
    secret = list(secret)
    guessed = []
    word = '_' * len(secret)
    word = list(word)
    maxTry = 10
    print('>>> Welcome to Hangman! \n\n You have %i chances to guess the Secret Word!' % maxTry+'\n\n')
    for _ in range(maxTry):
        w = input(' >>> Guess a letter: ')
        w = w.upper()
        if w in secret:
            guessed.append(w)
            index = [i for i, x in enumerate(secret) if x == w]
            for _ in index:
               word[_] = w
            print(word)
            _ += 1

        else:
            print('\nIncorrect ! try another letter!\n')


if __name__ == '__main__':
    main()
