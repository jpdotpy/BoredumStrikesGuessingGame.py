
# BoredumStrikeGuessingGame 🎲
# Welcome to the BoredumStrikeGuessingGame! 🚀 Test your intuition and guess the secret number between 1 and 20. Will you strike it lucky or succumb to boredom? Let's find out! 😎

# How to Play
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/BoredumStrikeGuessingGame.git
Navigate to the project directory:

bash
Copy code
cd BoredumStrikeGuessingGame
Run the game:

bash
Copy code
python boredum_strike_guessing_game.py
Start guessing! You have 6 attempts to discover the secret number. 🤞

Game Code
python
Copy code
# This is a number guessing game
import random

# Generate a random secret number between 1 and 20

secretNumber = random.randint(1, 20)
print("I'm thinking of a secret number between 1 and 20")

# Ask the player to take a guess 6 times
```
for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input()) ```

    if guess < secretNumber:
        print('Your guess is too low! 📉')
    elif guess > secretNumber:
        print('Your guess is too high! 📈')
    else:
        break  # This condition is the correct guess!

# Check if the player guessed correctly

```
if guess == secretNumber:
    print('Good job! You guessed correctly in ' + str(guessTaken) + ' attempts! 🎉')
else:
    print('Nope, good guess though LOLs. The number I was thinking of was ' + str(secretNumber) + ' 😜')
Have fun playing the BoredumStrikeGuessingGame! May the odds be ever in your favor! 🌟 If you enjoy it, give it a ⭐️! Feel free to contribute and make it even more exciting! 🚀 
``` 
