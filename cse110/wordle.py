import random
def wordle():
    word_bank = ["computer", "campus", "rexburg", "honor", "devote", "spirit", "faith", "values", "service", "mentor", "alumni"]
    word = random.choice(word_bank)
    word_length = len(word)
    incorrect_guess = 0
    while incorrect_guess <= 5:
        guess = input("Guess the word: ").lower()     
        if len(guess) != word_length:
            print(f"Your guess must be {word_length} letters long.")
            continue
        feedback = ""
        for index in range(word_length):
            if guess[index] == word[index]:
                feedback += guess[index].upper()
            elif guess[index] in word:
                feedback += guess[index].lower()
            else:
                feedback += "_"
        print(feedback)
        if guess == word:
            print("You win")
            print(f"It took you {incorrect_guess + 1} guess(es)")
            print("Game Over")
            break
        incorrect_guess += 1
    if incorrect_guess > 4:
        print("Sorry, had five incorrect guesses, you lose")
        print("Game Over")
wordle()
