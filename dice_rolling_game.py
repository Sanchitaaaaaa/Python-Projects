import random

while True:
  inp=input("Do you want to roll the dice : y/n ")
  if(inp=='y'):
    die1=random.randint(1,6)
    die2 = random.randint(1, 6)
    print(f'({die1},{die2})')
  elif (inp=='n'):
    print("thankyou for playing")
    break
  else:
    print("Invalid input !")

