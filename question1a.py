import random

number=random.randint(1,100)
attempts=0
guess=0

print("Guess the number between 1 and 100")

while guess!=number:
      guess=int(input("Enter your guess:"))
      attempts=attempts+1
      if guess<number:
          print("Too low") 
      elif guess>number:
           print("Too high") 

print(f"Correct! You guessed it in {attempts} attempts. ")

