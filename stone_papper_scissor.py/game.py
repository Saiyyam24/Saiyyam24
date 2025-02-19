import random


while True:
    hand = ["rock","paper","scissors"]
    gesture=random.choice(hand)
    user_input = input("Enter your choices: rock,paper or scissors or exit: ")
    if user_input == "exit":
        print("Game Over")
        break
    if user_input not in hand:
        print("invalid_input")
        continue
    else:
        print("user_input",user_input)
        print("computer_input",gesture)

        if user_input == gesture:
            print("Tie")
        elif user_input == "rock" and gesture == "scissors":
            print("You win")
        elif user_input == "scissors" and gesture == "paper":
            print("You win")
        elif user_input == "paper" and gesture == "rock":
            print("you win")       
        else:
            print("You lose")    