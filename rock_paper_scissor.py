import random

choices = ('r','p','s')
user_choice = input("Rock , Paper, Scissors ? (r/p/s): ").lower()
if user_choice not in choices:
    print("Invalid choice!")
computer_choice=random.choice(choices)

print(f"You choose {user_choice}")
print(f"Computer choose {computer_choice}")

if(user_choice==computer_choice):
    print("its a draw")

elif(user_choice=='r' and computer_choice=='p'):
    print("you lost ")
elif(user_choice=='p'and computer_choice=='r'):
    print("you won")

elif(user_choice=='r'and computer_choice=='s'):
    print("you won")
elif(user_choice=='s'and computer_choice=='r') :
    print("you lost")

elif(user_choice=='s'and computer_choice=='p'):
    print("you won")
elif(user_choice=='p'and computer_choice=='s'):
    print("you lost")
