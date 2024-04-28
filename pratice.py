import random
def rock_paper_scissors():
    player_input=input("your choice")
    choice=["rock","paper","scissor"]
    computer=random.choice(choice)
    print(computer)
    while computer:
        if player_input=="rock" and computer=="scissor":
            print("you won")
        elif player_input=="paper" and computer=="rock":
            print("you won")
        elif player_input=="scissor" and computer=="paper":
            print("you won")
        else:
            print("you lose and computer won")
        break
rock_paper_scissors()