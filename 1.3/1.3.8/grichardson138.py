from __future__ import print_function
import random

def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
    
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Guess who you think will win
    '''
    winner = random.choice(players)
    ####
    #The following code shortens the name and prints things
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]:
        print(p+', ',end='')
    print(players[len(players)-1])
    guesses = 1
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses

def goguess():
    number = random.randint(1, 20)
    guesses = 0
    print('Guess a number between 1 and 20 inclusive.')
    while raw_input(1) != number:
        guess = raw_input(1)
        guesses += 1
        if guess > 20:
            print(guess,' is too high, Try Again')
        else:
            return
        if guess < 1:
            print(guess,' is too low, Try Again')
        else:
            return
    print('Right! My number is ', number, ' You guessed in ', guesses, ' guesses!')
    