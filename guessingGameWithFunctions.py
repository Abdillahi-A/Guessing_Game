import random

def generateRandomNumber():
    randomNumber = random.randint(1,20)
    return randomNumber

def getUserInput(numberOfGuesses, randomNumber):
    while True:
        try:
            guess = int(input("Take a guess\n"))
            numberOfGuesses +=1
            if guess != randomNumber:
                print(f"You have {5 - numberOfGuesses} guesses left.")
            return guess, numberOfGuesses
        except ValueError:
            print("Oops, that didn't work. Make sure you input a number.\n")

def checkGuess(randomNumber, guess, numberOfGuesses):
    while guess != randomNumber and numberOfGuesses <5:
        if guess < randomNumber:
            print("Your guess is too low. Try Again.\n")
            guess, numberOfGuesses = getUserInput(numberOfGuesses,randomNumber)
        elif guess > randomNumber:
            print("Your guess is too high. Try Again.\n")
            guess, numberOfGuesses = getUserInput(numberOfGuesses,randomNumber)
    
    if guess == randomNumber:
        print(f"Congrats, the number I was thinking of was {randomNumber}.")
    else:
        print(f"You are out of guesses. The number I was thinking of was {randomNumber}.")

def playAgain():
    playAgain = input("\nDo you want to play again? Type 'Y' to play again or 'N' to quit.\n")
    while playAgain.upper() not in ['Y', 'N']:
        playAgain = input("Type 'Y' to play again or 'N' to quit.\n").upper()
    if playAgain.upper()[0] == 'Y':
        print("Cool let's play again.\n")
        return True
    else:
        print("That's too bad. Come back again later. Bye!")
    
def main():
    while True:
        randomNumber = generateRandomNumber()
        print("I am thinking of a random integer between 1 and 20. What number am I thinking of?\n")
        numberOfGuesses = 0
        guess, numberOfGuesses = getUserInput(numberOfGuesses,randomNumber)
        checkGuess(randomNumber, guess, numberOfGuesses)
        if not playAgain():
            break

main()
