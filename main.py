import random
def get_choices():
  player_choice = input("Enter a choice -> rock,paper,scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  
  choices = {"player":player_choice,"computer":computer_choice}
  return choices
def check_win(player,computer):
  print(f"you chose {player}, computer chose {computer}")
  if player == computer:
    return "Its a TIE!"
  elif player =="rock":
    if computer=="scissors":
        return "Rock smashes scissors! YOU WIN!🏆"
    else:
       return "Paper covers Rock YOU Lose🥹"
  elif player =="paper":
    if computer=="rock":
       return "Paper  covers rock ! YOU WIN!🔥"
    else:
       return "Scissors cuts paper YOU Lose🥹"
  
  elif player == "scissors":
    if computer=="paper":
      return "Scissors cuts paper! YOU WIN!🏆"
    else: 
       return "Rock smashes scissors You Lose🥹"
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
