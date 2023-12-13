


#This is a number guessing game
import random 
secretNumber = random.randint(1,20)
print("i'm thinking of a secret number between 1 and 20")

#Ask the player to take a guess 6x
for guesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!!')
    else: 
        break       #this condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed correct in ' + str(guesTaken) + " ")
else:
    print('Nope, good guess though lol, the number I was thinking of was ' + str(secretNumber) + ' ')
