import random
while True:
    user_gesture = input("Enter a choice ROCK,PAPER,SCISSOR:\n")
    from_user = ["ROCK","PAPER","SCISSOR"]
    from_computer = random.choice(from_user)
    print(f"You selected : {user_gesture}\nComputer selected: {from_computer}")
    if user_gesture==from_computer:
        print(f"Both selected {user_gesture}...It is a tie!")
    elif user_gesture=="ROCK":
        if from_computer=="SCISSOR":
            print(f"{user_gesture} smashes SCISSOR! So, You win.")
        else:
            print("You lose!")
    elif user_gesture=="PAPER":
        if from_computer=="ROCK":
            print(f"{user_gesture} covers ROCK.So, you win!")
        else:
            print("You lose!")
    elif user_gesture=="SCISSOR":
        if from_computer=="PAPER":
            print(f"{user_gesture} cuts PAPER..So, you win!")
        else:
            print("You lose!")
    repeat_game = input("Do you want to repeat the game?[y/n]") 
    if repeat_game.lower()=="y":
        print(user_gesture)
    else:
        print("END OF THE GAME!")
        break
