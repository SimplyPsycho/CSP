from __future__ import print_function # must be first in file 

def food_id(food):
    '''Returns categorization of food
    
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']
    
    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()')
    # Add tests so that all lines of code are visited during test
 
    if works:
        print('food_id passed all tests')
    return works
    
def integer_thing(x):
    n = x
    if int(n)==n:
        if n % 2 == 0:
            if n % 3 == 0:
                print (n, 'is a multiple of 6')
            else:
                print (n, 'is even')
        else:
            print (n, 'is odd')
    else:
        print (n, 'is not an integer')
        
import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4 inclusive.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess < secret:
            print('Too Low, my number is ', secret, '.', sep='')
        else:
            print('Too High, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')
        
def quiz_decimal(low, high):
    print('Type a number between ', low, high)
    number = raw_input()
    number1 = int(number)
    low = int(low)
    high = int(high)
    if number1 <= high and >= low:
        print('Good!', number1)
    else:
        print("No.', number1)