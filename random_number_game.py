# ITEC 2905-Capstone
# Boris Valle

import random

print('\nThis game is about you guessing the number that I am ' +
'that I am thinking. \n ')

def main():
    number_of_tries = 0
    guess_the_number = randNumber()
    # for number_taken in roll():
    number_of_tries += 1
    #checks to see if the number is too high or to low
    while True:
        guess_input = play_input()
        if guess_input < guess_the_number:
            print('Number is to low!')
        elif guess_input > guess_the_number:
            print('Number is to high!')
        else:
            break
    print('Great!')
    # if guess_input == guess_the_number:
    #     print("Good job! it only took you " + str(number_of_tries) + " tries")
    # else:
    #     print("You lose, the number that I was thinking was: " + str(guess_the_number))

# Defines the number of times the playes has before guessing the right number
# def roll():
#     return range(1, 6)

# This is the number that the computer will select.
def randNumber():
    return random.randint(1, 10)

def play_input():
    return int(input('Guess the number: '))


if __name__ == '__main__':
    main()
