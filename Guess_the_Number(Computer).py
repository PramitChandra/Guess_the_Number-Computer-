# We will have a secret number and computer will guess the number.

import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':  # and low != high:
        if low != high:
            comp_guess = random.randint(low, high)
        else:
            comp_guess = low  # could also be high 'cause low = high

        feedback = input(f"Is {comp_guess} High (h), Low (l), or Correct (c)?: ")
        if feedback == 'h':
            high = comp_guess - 1
        elif feedback == 'l':
            low = comp_guess + 1

    print(f"Computer guessed your Number, {comp_guess}, correctly!")


computer_guess(10)
