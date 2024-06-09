hidden = "temple"
print("Welcome to the word guessing game!")
print("")
guess = ""
guessnum = 0

while guess != hidden:
    guess = input("What is your guess? ")
    guessnum += 1
    if len(guess) != len(hidden):
        print(f"Sorry, the guess must have the same number of letters as the secret word.")
        continue
    if guess == hidden:
        print("Congratulations! You guessed it!")
    else:
        print("Your guess was not correct.")

print(f"It took you {guessnum} guesses.")