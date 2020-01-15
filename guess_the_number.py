import random

number = random.randint(1,100)

user_guess = int(input('Guess a number 1-100: '))

while user_guess != number:
    if user_guess > number:
        print('You guessed too high!')
    else:
        print('You guessed too low')
    user_guess = int(input('Guess again! '))
    
print('You guessed correct! The number is ' + str(number))