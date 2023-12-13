# BoredumStrikeGuessingGame 🎲

Welcome to the BoredumStrikeGuessingGame! 🚀 Test your intuition and guess the secret number between 1 and 20. Will you strike it lucky or succumb to boredom? Let's find out! 😎

## How to Play

```bash
# Clone the repository


# Navigate to the project directory
cd BoredumStrikeGuessingGame

# Run the game
python boredum_strike_guessing_game.py
# Ask the player to take a guess 6 times
for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low! 📉')
    elif guess > secretNumber:
        print('Your guess is too high! 📈')
    else:
        break  # This condition is the correct guess!

# Check if the player guessed correctly
if guess == secretNumber:
    print('Good job! You guessed correctly in ' + str(guessTaken) + ' attempts! 🎉')
else:
    print('Nope, good guess though LOLs. The number I was thinking of was ' + str(secretNumber) + ' 😜')
Have fun playing the BoredumStrikeGuessingGame! May the odds be ever in your favor! 🌟 If you enjoy it, give it a ⭐️! Feel free to contribute and make it even more exciting! 🚀

csharp
Copy code

Copy and paste the above Markdown code into your `README.md` file on GitHub.
