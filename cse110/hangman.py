word = "computer"
guessed_letters = ["-"] * len(word)
incorrect = 0
guessed_char = []
#def game():
not_correct = True
while not_correct:
        print("".join(guessed_letters))
        print("".join(guessed_char))
        char_guess = input("Guess a character: ")
        character = char_guess[0]
        for index, letter in enumerate(guessed_char):
            if character == letter:
                print("You already guessed that character")
               #game()
        guessed_char.append(char_guess[0])
        contains_char = False
        for index, letter in enumerate(word):
            if character == letter:
                guessed_letters[index] = character
                contains_char = True
        if contains_char == False:
            print("Sorry, the word does not contain this character")
            incorrect += 1
        if incorrect > 5:
            print("Sorry, you lose")
            not_correct = False

#game()
print("Game Over")