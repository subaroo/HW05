#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """
    Takes one integer from user
    Determines if even or odd
    Prints determination
    returns None
    """
    While True:
        user_integer = raw_input("Please give me an integer: \n")
        try:
            user_number = int(user_integer)
        except: 
            print("Try again by giving me a number.")
            return even_odd()       
        else:
            if user_number % 2 == 0:
                print("even")
            else:
                print("odd")
            return
    

def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    pass


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    pass

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()

if __name__ == '__main__':
    main()
