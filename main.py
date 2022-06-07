import random

# Declaring the needed variables
moves = ["R", "P", "S"]
chk_moves = ["Rock", "Paper", "Scissors"]
# Initializing th player
player = " "
com = random.choice(chk_moves)

# Looping through the program
while True:
    player = input("Select ur choice: ").capitalize()
    if player not in moves:
        print("Wrong Move")
        player = input("Please chose a valid choice: ").capitalize()

    if player == "R":
        player = chk_moves[0]

    if player == "P":
        player = chk_moves[1]
    if player == "S":
        player = chk_moves[2]
    if player == com:
        print(f"You both chose({com})\nIts a Tie")
        # break
    elif player == chk_moves[0]:
        if com == "Scissors":
            print(f"Player({player}): Computer({com})\nRock Beats Scissors!\nYou Win")
        else:
            print(f"Player({player}): Computer({com})\nPaper beats Rock!\nYou lose")
    elif player == chk_moves[1]:
        if com == "Rock":
            print(f"Player({player}): Computer({com})\nPaper beats Rock!\nYou Win")
        else:
            print(f"Player({player}): Computer({com})\nScissors beats Paper!\nYou lose")
    elif player == chk_moves[2]:
        if com == "Paper":
            print(f"Player({player}): Computer({com})\nScissors beat Paper!\nYou Win")
        else:
            print(f"Player({player}): Computer({com})\nRock beats Scissors!\nYou lose")

    # Ask player if he/she would like to play aagain
    play_again = input("Play again? (y/n): ")
    if play_again not in ["y","Yes","Y","YES", "yes"]:
        print("Thanks for playing,....Goodbye")

        # breaking out of the loop
        break