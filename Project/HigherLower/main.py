##### HigherLower #####

# Import libraries
from art import logo, vs
from game_data import data
import random
from replit import clear

### Break down the problem ###
# Display Logo
print(logo)

## use if statement if guess is correct
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Format the account data to printable format
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# Score keeping
score = 0
game_should_continue = True

# move position B to position A
account_b = random.choice(data)

# keep the game playing
while game_should_continue:
    # Generate game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Condition to check the answer
    ## loop through the follwer of the account data and compare with guess
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # clear the screen
    clear()
    print(logo)
    
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, You're wrong. Final score: {score}")
        game_should_continue = False
        



