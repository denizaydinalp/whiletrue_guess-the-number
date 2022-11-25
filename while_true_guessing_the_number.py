"""
This is a basic guessing number game. program creates a random number,
and we try the number. we can type "done" or just press enter to
exit the system. Good point to understand Try-Except block and While True Loop.
"""
import random

number = random.randint(1, 10)
print("Random number is ", number)
print("Type 'done' to exit the code")
guess = input("Take a guess between 1 to 10.... ")
while True:
    try:
        guess_int = int(guess)
        if len(guess) < 1:
            print("Terminated by user... ")
            break
        elif guess_int == number:
            print("That's great!.... ")
            break
        else:
            guess = input("Give another shot... ")
    except:
        if guess == "done":
            print("Terminated by user..... ")
            break
        else:
            print("Numeric input only... ")
            guess = input("Enter a numeric value or type 'done' to exit code: ")
