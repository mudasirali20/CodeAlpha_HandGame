import random

def hangman_game():
    words = ["python", "hangman", "developer", "programming", "software"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("You have", attempts, "attempts to guess the word.")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        hangman_game()
    else:
        print("Thanks for playing!")

# Run the game
hangman_game()
