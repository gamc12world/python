import random
x1=random.randint(1,100)
print(x1)
counter_var=0
all_the_guesses=[]
while x1:
    counter_var+=1
    player_guess=int(input("enter your guess"))
    all_the_guesses.append(player_guess)
    if player_guess==str():
        print("error")
        break
    else:
        if x1==player_guess:
            print(f"The no of guesses are {all_the_guesses}")
            print(f"No.of tries are {counter_var}")
            print("you won")
            break
        else:
            if player_guess>100 or player_guess<1:
                print("out of range")
                break
            else:
                if player_guess<=10 and x1<=10:
                    print("warm")
                else:
                    print("cold")

