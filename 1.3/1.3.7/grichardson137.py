import matplotlib.pyplot as plt
import random

def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

plt.ion()
def picks():
    a = [] # make an empty list

    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]
    plt.hist(a)
    plt.show()
    
def dice(n):
    n = [n]
    a = 0
    for times in n:
        a += random.choice([1, 2, 3, 4, 5, 6])
    print(a)
    
def matches(ticket, winners):
    n = 0
    for num in ticket:
        if num in winners:
            n += 1
        else:
            n += 0
    print(n)