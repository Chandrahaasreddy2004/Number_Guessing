logo="""
 _______               ___.                    ________                             
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >
        \/            \/    \/     \/                \/            \/     \/     \/ """
import random
print(logo)
print("""Welcome to the number guessing name
I'm thinking of a number between 1 to 100""")
game_mode=input("Type easy or difficult\n")
numbers=[]
for i in range(101):
  numbers.append(i)
choice=random.choice(numbers)
#print(choice)
if(game_mode=="easy"):
  number_of_turns=10
  while(number_of_turns>=1):
    print(f"you have {number_of_turns} attempts")
    number_of_turns=number_of_turns-1
    guess=int(input("enter a number"))
    if(guess<0 or guess>100):
      print("you entered a invalid number")
    elif(guess==choice):
      print(f"you got it!The answer is {guess}.You win")
      number_of_turns=-9
    elif(guess>choice):
      print("Too high")
      print("Guess again")
    else:
      print("Too low")
      print("Guess again")
  if(number_of_turns==0):
    print("you lost.Better luck next time")
    Print(f"The original  number is {choice}")
  
else:
  number_of_turns=5
  while(number_of_turns>=1):
    print(f"you have {number_of_turns} attempts")
    number_of_turns=number_of_turns-1
    guess=int(input("enter a number"))
    if(guess<0 or guess>100):
      print("you entered a invalid number")
    elif(guess==choice):
      print(f"you got it!The answer is {guess}.You win")
      number_of_turns=-9
    elif(guess>choice):
      print("Too high")
      print("Guess again")
    else:
      print("Too low")
      print("Guess again")

  if(number_of_turns==0):
    print("you lost.Better luck next time")
    print(f"The original answer is {choice}")
