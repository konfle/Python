# Lesson 1 - Functions and default argument values


def BuyMe(prefix, what='something niece'):
    print(prefix, what)


'''
def BuyMe(prefix = 'Please buy me', what):
    print(prefix, what)
'''

BuyMe('Please buy me', 'a new car')
BuyMe(prefix='Please buy me', what='a new car')
BuyMe(what='a new car', prefix='Please buy me')
BuyMe('Please')
BuyMe(prefix='Please buy me')
BuyMe(what='something sweet', prefix='Please')

# LAB


def show_progress(how_many, character='*'):
    print(character * how_many)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')
