import random
from secrets import choice

# List of choice
choice = ["Rock", "Paper", "Scissor"]
# Bot random choice
bot = choice[random.randint(0,2)]
player = False

# Loops when player is False
while player == False:
    # Getting player choice and player with become True because have value
    player = str(input("Pick you choice : "))
    if player == bot:
        print("Tie")
    elif player == "Paper":
        if bot == "Scissor":
            print("Unfortunately you lose, your choice is {} and the opponent is {}".format(player,bot))
        else:
            print("Great, You win!, your {} smash {}".format(player,bot))
    elif player == "Rock":
        if bot == "Paper":
            print("Unfortunately you lose, your choice is {} and the opponent is {}".format(player,bot))
        else:
            print("Great, You win!, your {} smash {}".format(player,bot))
    elif player == "Scissor":
        if bot == "Rock":
            print("Unfortunately you lose, your choice is {} and the opponent is {}".format(player,bot))
        else:
            print("Great, You win!, your {} smash {}".format(player,bot))
    
    # Turn the player to False again so lpops will occur
    player = False
    # Replace the old bot choice with a new one
    bot = choice[random.randint[0,2]]


