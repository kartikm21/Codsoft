

import random

def play_game():

 print("Winning rules for winning this game that is rock, paper and scissor are")
 print("Rock vs Paper -----> Paper wins")
 print("Rock vs Scissors -----> Rock wins")
 print("Scissors vs Paper -----> Scissors wins")

 print("Enter Your Choice below")
 print("1. Rock ")
 print("2. Paper")
 print("3. Scissors")

 choice= int(input("Select the number : "))
 if choice < 1  or choice > 3:
  return print("Invalid Choice ")

 else:
    print("Choice verified")

 if choice == 1:
  print("You opted for choice Rock")
  choice_name= "Rock"

 elif choice == 2:
        print("You opted for choice Paper")
        choice_name = "Paper"

 else:
    print("You opted for choice Scissors")
    choice_name = "Scissors"


 print("Hence Your choiced option is :  " + choice_name)

 print("Now its computer turn......."
      "wait for a while")


 comp_choice= random.randint(1,3)

 while comp_choice == choice:
   comp_choice= random.randint(1,3)



 if comp_choice == 1:
     print("Computer opted for choice Rock")
     comp_choice_name= "Rock"

 elif comp_choice == 2   :
    print("Computer opted for choice Paper")
    comp_choice_name = "Paper"

 else:
     print("Computer opted for choice Scissors")
     comp_choice_name = "Scissors"




 print("Now")
 print(choice_name,"  v/s  ", comp_choice_name)

 if choice == comp_choice :

    print("Its a Draw")

 elif (choice == 1 and comp_choice == 2):
        print("Paper wins , Hence computer wins")

 elif(choice == 2 and comp_choice == 1 ):
        print("Paper wins , Hence You won")

 elif (choice == 2 and comp_choice == 3):
            print("Scissor wins , Hence computer wins")

 elif (choice == 3 and comp_choice == 2):
            print("Scissor wins , Hence You won")

 elif (choice == 3 and comp_choice == 1):
                print("Rock wins , Hence computer wins")

 elif (choice == 1 and comp_choice == 3):
                print("Rock wins , Hence You won")


 print("thanks for playing")




while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thank you for playing!")