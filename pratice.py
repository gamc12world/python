import random
def rock_paper_scissors():
    computer_counter=0
    player_counter=0
    while True:
        player_input=input("your choice")
        choice=["rock","paper","scissor"]
        computer=random.choice(choice)
        if player_input=="rock" and computer=="scissor":
            player_counter+=1
            print("you won")
        elif player_input=="paper" and computer=="rock":
            player_counter+=1
            print("you won")
        elif player_input=="scissor" and computer=="paper":
            player_counter+=1
            print("you won")
        elif player_counter>3:
            print("you finally winner")
            break
        elif computer_counter>3:
            print("computer is finally winner")
            break
        else:
            print("computer won")
            computer_counter+=1
rock_paper_scissors()