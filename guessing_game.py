import random

number = random.randint(1,10)

name = input("Hello, what is your name ? ")

print(f"Well, {name} I'm thinking of a number between 1 and 10." )

guess = int(input("Take a guess. "))

guess_count = 1

while guess_count <5:
    if guess > number:
        print("Your guess is too high.")
        guess = int(input("Take a guess. "))
        guess_count += 1
    elif guess< number:
        print("Your guess is too low.")
        guess = int(input("Take a guess. "))
        guess_count += 1
    elif guess == number:
        print(f"Congrats {name} you guessed correct in {guess_count} guesses!")
        break
        
else:
    print(f"Sorry you are out of guesses. The number I was thinking of was {number}.")
    
