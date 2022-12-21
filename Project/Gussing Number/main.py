from random import randint

# check answer function
def check_answer(guess_num, random_num, turns):
    if guess_num == random_num:
        print(f"You got it! The answer was {random_num}")
    elif guess_num > random_num:
        print(f"Your guess is {guess_num}, Too high")
        return turns - 1
    else:
        print(f"Your guess is {guess_num}, Too low")
        return turns - 1

# set up attempt for easy and hard difficulty
def set_difficulty():
    # choose game difficulty
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

EASY_LEVEL = 10
HARD_LEVEL = 5

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    # random number between 1 and 100
    answer = randint(1, 100)
    print(answer)

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        # show the total attempts
        print(f"You have {turns} attempts remaining to guess the number.")

        # create guess variable to contain the guess number for each attempt
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You're ran out of turns. You Lose!")
            return
        elif guess != answer:
            print("Guess again!")

game()