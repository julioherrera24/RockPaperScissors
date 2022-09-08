import random

userScore = 0
computerScore = 0
options = ["rock", "paper", "scissors"]

while True:
  userInput = input("\nType Rock - Paper - Scissors or Q to quit: ").lower()
  if userInput == "q":
    print("Thanks for playing!")
    break  #this will break from the while loop & end program
    
  if userInput not in options:
    print("\nPlease type either rock / paper/ scissors")
    continue #this will re ask them to type r/p/s

  randomNumber = random.randint(0, 2)
  #rock: 0. paper: 1. scissors: 2
  computerPick = options[randomNumber]
  print("\nThe computer chose:", computerPick + ".")

  if userInput == "rock" and computerPick == "scissors":
    print("You win!")
    userScore += 1

  elif userInput == "paper" and computerPick == "rock":
    print("You win!")
    userScore += 1

  elif userInput == "scissors" and computerPick == "paper":
    print("You win!")
    userScore += 1
  
  elif userInput == "rock" and computerPick == "rock":
    print("You both chose rock, its a tie!")
  
  elif userInput == "paper" and computerPick == "paper":
    print("You both chose paper, its a tie!")

  elif userInput == "scissors" and computerPick == "scissors":
    print("You both chose scissors, its a tie!")
  
  else:
    print("You lost!")
    computerScore += 1

  print("\nYou've won", userScore, "times.")
  print("The computer won", computerScore, "times.")
  print("\nPlay again!")
  print("________________________________________________________")