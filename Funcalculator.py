import random
import math
print("Welcome to the Random Fun Calculator!\n")
print("Lucky Number Generator")
lucky_number=random.randint(1, 100)
print(f"Your lucky number today is:{lucky_number}\n")
print("Random Activity Picker")
activities=[
    "read a book",
    "dance for 2 minutes",
    "take a short walk",
    "listen to music",
    "write something creative",
    "play a quick game",
    "take a power nap",
]
chosen_activity=random.choice(activities)
print(f"Your random activity is:{chosen_activity}\n")
print("Number Guessing Game")
secret_number=random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")
guess=None
while guess!=secret_number:
    try:
        guess=int(input("Take a guess: "))
        if guess<secret_number:
            print("Too low. Try again.")
        elif guess>secret_number:
            print("Too high. Try again.")
        else:
            print("Correct. You guessed the number!\n")
    except ValueError:
        print("Please enter a valid number.")
print("Math Function Demonstration")
try:
    x=float(input("Enter a number (x): "))
    y=float(input("Enter another number (y): "))
except ValueError:
    print("Invalid input. Using default values x=5.7, y=-3.")
    x=5.7
    y=-3
print("\nmath.ceil(x):",math.ceil(x))
print("math.floor(x):",math.floor(x))
print("math.fabs(y):",math.fabs(y))
print("math.copysign(x, y):",math.copysign(x, y))
a=int(x)
b=int(y)
print(f"math.gcd({a},{b}):",math.gcd(a, b))
print("\nThank you for using the Random Fun Calculator.")
print("Come back anytime for more randomness and math fun.")
