import random

game = True

while game:
    print("\n")
    print("1. Rock 2. Paper 3. Scissors")
    input_choice = int(input("Enter your choice: "))
    if input_choice == 1:
        player = "Rock"
    elif input_choice == 2:
        player = "Paper"
    else:
        player = "Scissors"
    
    chances = ["Rock", "Paper", "Scissors"]
    computer = random.choice(chances)

    print("Player's choice is:", player)
    print("Computer's choice is:", computer)

    if player == computer:
        print("Tie!!!")
    elif player == "Rock":
        if computer == "Paper":
            print("Winner is computer")
        elif computer == "Scissors":
            print("Winner is player")
    elif player == "Paper":
        if computer == "Rock":
            print("Winner is player")
        elif computer == "Scissors":
            print("Winner is computer")
    elif player == "Scissors":
        if computer == "Paper":
            print("Winner is player")
        elif computer == "Rock":
            print("Winner is computer")

    print("\n")
    print("1. Quit  2. Play")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        game = False
