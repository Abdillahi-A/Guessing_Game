import random

name = input("Hello, what is your name ? ")

print(f"Well, {name} I'm thinking of a number between 1 and 20." )

play = 'yes'

while play.lower()[0] == 'y':

    secretnumber = random.randint(1,20)
    
    guess = 0
    
    guess_count = 0
      
    while guess_count <5 and guess != secretnumber:
        guess = int(input("Take a guess "))
        guess_count += 1
        if guess < secretnumber:
            print("Your guess is too low. ")
        elif guess > secretnumber:
            print("Your guess is too high.")
                      
    if guess != secretnumber:   
         print(f"Sorry you are out of guesses. The number I was thinking of was {secretnumber}.")
    else:
        print(f"Congrats, you guessed correct in {guess_count} guesses!")
        
    play = input("Do you want to play again? Y or N ? ")
    while play.lower()[0] not in ['y','n']:
        play = input("Please type 'Y' to play again or 'N' to exit ? ")
        
    if play.lower()[0] == 'y':
        print("Cool! Let's play again!")
        
else:
    print("That's too bad. Come back again later. Bye!")
    
        
