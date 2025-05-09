import random

choices=['rock','paper','scissors']
user=input("Choose rock,paper or scissors:").lower()

computer=random.choice(choices)

print(f"You choose {user},computer choose {computer}")

if user==computer:
    print("it is a  tie")
elif (user=='rock'and computer=='scissors') or \
     (user=='paper'and computer=='rock') or \
     (user=='scissors' and computer=='paper'):
    print("You win")
else:
    print("You loose")