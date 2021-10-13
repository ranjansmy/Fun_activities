import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 to {x}: '))
        if guess < random_number:
            print('Little low, try more: ')
        elif guess > random_number:
            print('Oops, you are high, little less: ')

    print(f'Awesome, you have clicked the jackpot {random_number}')

guess(100)
