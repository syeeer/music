#!/usr/bin/env python

import random

  

def main():
    """Start a music genre guessing game."""
    print("\nGuess the music genre game! You have 5 times to try.")
    print("######################################")
    
  
    music = ["pop music","jazz","hip hop","heavy mental","rock","rap","art music"]
 
    x = random.choice(music)

    guess = None 
    score = 100

    for count in range(5):
     
        guess = str(input("\nWhat kind of music genre am I thinking of?"))
        if x == guess:
            print("\nYou guessed {}. Congratulations, you got it right!".format(guess))
            break
        else:
            print("\nYou guessed {}. Sorry, you got the wrong answer. Please try again!".format(guess))
            score -= 20
    else:
        print("\nThe correct answer is:",x)
    print("\nYour score is: ", score)



main()

