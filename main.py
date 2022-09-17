import random
from art import rock, paper, scissors
choice = [rock, paper, scissors]

your_choice = (int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")))
you_chose = choice[your_choice]
print(you_chose)

computer_choice = random.choice(choice)
print(f"Computer chose: {computer_choice}")

if you_chose == rock and computer_choice == scissors:
  print("You win!")
elif you_chose == scissors and computer_choice == paper:
  print("You win!")
elif you_chose == paper and computer_choice == rock:
  print("You win!")
elif you_chose == computer_choice:
  print("Tie game.")
else:
  print("You lose.")
