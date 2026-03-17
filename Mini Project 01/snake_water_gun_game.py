import random # Importing random module to let computer choose randomly

game_list = ["snake","water","gun"] # List of all possible choices in the game

win_rules = { # Dictionary to define which choice beats which
    "snake": "water",     # Snake beats water
    "water": "gun",       # Water beats gun
    "gun": "snake"        # Gun beats snake

}

computer_choice = random.choice(game_list) 
# Computer randomly selects one option from the list

user = input("Enter snake, water, gun: ").lower()
# Takes input from user and converts it to lowercase

print("Computer Choice: ",computer_choice)
# Displays what computer selected

if user == computer_choice:
    # Checks if both user and computer selected the same thing
    print("It's a Draw 🤝")

elif user in game_list:
     # Checks if user entered a valid choice (snake, water, or gun)
    if win_rules[user] == computer_choice:
        # Checks if user's choice defeats computer's choice
        # Example: win_rules["snake"] → "water"
        # If computer_choice is "water", user wins
        print("You Win")
    else:
        # If it's not a draw and not a win, then user loses
        print("You Lose")
else:
    # If user entered something invalid (not in list)
    print("Invalid Choice")