import getpass

def game():
    while True:
        print("Welcome to Rock Paper Scissors game!")
        user_1 = getpass.getpass("Enter user 1 choice:").lower()
        user_2 = getpass.getpass("Enter user 2 choice:").lower()

        print("\n")
        print(f"User_1 entered {user_1}")
        print(f"User_2 entered {user_2}")
        print("\n")
        
        if user_1 in ["rock", "scissors", "paper"]:
            if user_2 in ["rock", "scissors", "paper"]:
                if user_1 == user_2:
                    print("It is a tie")
        
                elif (user_1 == "rock" and user_2 == "scissors") or \
                     (user_1 == "paper" and user_2 == "rock") or \
                     (user_1 == "scissors" and user_2 == "paper"):
                    print("Congrats! User_1 wins")
        
                else:
                    print("Congrats! User_2 wins")    
            else:
                print("Invalid Choice")
        else:
            print("Invalid Choice")

        print("\n")
        play_again = input("Do you want to play again?").lower()
        print("\n")
    
        if play_again == "yes":
            game()
        elif play_again == "no":
            print("Thanks for Playing")
            break
        else:
            print("Invalid Choice! Thank you")
            break

game()