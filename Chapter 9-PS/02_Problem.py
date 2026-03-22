"""
The game() function in a program lets a user play a game and returns the score as an integer.
You need to read a file "Hi-score.txt" which is either blank or contains the previous Hi-score. 
You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
"""

import random #To generate random numbers

def game(): # Game function
    print("You are playing the game...")
    score = random.randint(1,100) # Going to generate random number between 1 to 100.

    with open(r"D:\Python\Chapter 9-PS\highscore.txt") as f:
        high_score = f.read() # Reading the high score
        if (high_score != ""): # If the high score is not blank, then convert it to an integer
            high_score = int(high_score) # Converting the high score to an integer
        else:
            high_score = 0 # If the high score is blank, then set it to 0
    
    print(f"Your Score: {score}") # Printing the score of the user
    if (score>high_score): # If the score of the user is greater than the high score, then update the high score
        print("Congratulations! You have broken the high score!")

        with open (r"D:\Python\Chapter 9-PS\highscore.txt","w") as f: # Opening the high score file in write mode to update the high score
            f.write(str(score)) # Writing the new high score to the file
        
    return score # Returning the score of the user

game()