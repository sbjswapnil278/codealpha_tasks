import random

words =["python","coding","game","random","hangman"]

word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

display_word = ["_"] * len(word_to_guess)

print("Welcome to Hangamn Game ")
print("You have",max_incorrect,"incorrect guess allowed.")
print("Word to guess:"," ".join(display_word))

while incorrect_guesses< max_incorrect and "_" in display_word:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter single aplhabets only")
        continue
    if guess in guessed_letters:
        print("you already guessed that letter.")
        continue
    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
    else:
        incorrect_guesses +=1
        print(f" Wrong guess {max_incorrect - incorrect_guesses} tries left.")
        print("Word:"," ".join(display_word))
        print("Guessed letters:", ",".join(guessed_letters))

if "_" not in display_word:
    print("\n Congrats You guessed the word:", word_to_guess)
else:
    print("\n Game over. Correct word is:",word_to_guess)