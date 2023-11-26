from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]
victory = 0
lose = 0

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            print("Try harder!")
            lose += 1
            print("Player: ", victory, ", Computer: ", lose)
        else:
            print("Congrats, you win!", player, "smashes", computer)
            print("So proud of you!")
            victory += 1
            print("Player: ", victory, ", Computer: ", lose)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            print("Maybe next time!")
            lose += 1
            print("Player: ", victory, ", Computer: ", lose)
        else:
            print("You win!", player, "covers", computer)
            print("What a coincidence!")
            victory =+ 1
            print("Player: ", victory, ", Computer: ", lose)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            print("Not enough darling!")
            lose += 1
            print("Player: ", victory, ", Computer: ", lose)
        else:
            print("You win!", player, "cut", computer)
            print("Nice one bro!")
            victory += 1
            print("Player: ", victory, ", Computer: ", lose)
    else:
        print("That's not a valid play. Check your spelling!")
        print("Maybe you should check it before entering your texts.")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
