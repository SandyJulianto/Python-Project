import random
from secrets import choice

choice = ["Rock", "Paper", "Scissor"]
bot = choice[random.randint(0,2)]
player = False

while player == False:
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
    
    player = False
    bot = choice[random.randint[0,2]]


