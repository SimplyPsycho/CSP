def add_tip(total, tip_percent):
    ''' Return the total amount including tip
    '''
    tip = tip_percent*total
    return total + tip
    
def mean(a, b, c):
    tot = a + b + c
    avg = tot / 3.0
    return avg

def hyp(leg1, leg2):
    c = leg1**2 + leg2**2
    hyp = c**0.5
    return hyp
    
def perimeter(base, height):
    per = base * 2 + height * 2
    return per