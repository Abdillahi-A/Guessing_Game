import random

def generateRandomNumber():
    randomNumber = random.randint(1,20)
    return randomNumber

def checkUserInputtedNumber(guess):
    while True:
        try:
            guess = int(guess)
            break
        except ValueError:
            guess = input("Oops that didn't work. Please make sure you choose a valid number\n")
    return guess

def checkIfGuessIsCorrect(guess,randomNumber, number_of_guesses):
        if guess == randomNumber:
            print(f"Congrats, you guessed correctly in {number_of_guesses} guesses! The number I was thinking of was {randomNumber}.")
        
        elif guess < randomNumber and number_of_guesses <5:
            
            guess = input("Your guess is too low. Try again.\n")
            guess = checkUserInputtedNumber(guess)
            number_of_guesses += 1
            checkIfGuessIsCorrect(guess,randomNumber, number_of_guesses)

        elif guess > randomNumber and number_of_guesses <5:
            guess = input("Your guess is too high. Try again.\n")
            guess = checkUserInputtedNumber(guess)
            number_of_guesses += 1
            checkIfGuessIsCorrect(guess,randomNumber, number_of_guesses)

        else:
            print(f"Sorry you are out of guesses. The number I was thinking of was {randomNumber}.")

def play_again():
    playAgain = input("Do you want to play again? Type 'Y' to play again or 'N' to exit.\n").upper()
    while playAgain.upper() not in ['Y','N']:
        playAgain = input("Please type 'Y' to play again or 'N' to exit.\n").upper()

    if playAgain == 'Y':
        return True
        
def main():
    while True:
        randomNumber = generateRandomNumber()
        guess = input("I am thinking of a number between 1 and 20. What number am I thinking of?\n")
        guess = checkUserInputtedNumber(guess)
        number_of_guesses = 1
        checkIfGuessIsCorrect(guess,randomNumber, number_of_guesses)
        if not play_again():
            print("That's too bad. Come back again later. Bye!")
            break
        else:
            print("Cool! Let's play again!\n")
    

main()