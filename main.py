import tkinter as tk
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

display = ["_" for _ in range(len(chosen_word))]
guesses = 0
guessed_letters = []


def update_display():
    word_display.set(" ".join(display))
    guessed_display.set("Guessed letters: " + " ".join(guessed_letters))
    hangman_display.set(HANGMANPICS[guesses])


def guess_letter():
    global guesses
    the_guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if len(the_guess) != 1 or not the_guess.isalpha():
        message.set("Please enter a single letter.")
        return

    if the_guess in guessed_letters:
        message.set("You already guessed that letter. Try again.")
        return

    guessed_letters.append(the_guess)

    if the_guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == the_guess:
                display[position] = the_guess
        message.set("Correct!")
    else:
        message.set("Wrong")
        guesses += 1

    update_display()

    if "".join(display) == chosen_word:
        message.set("You win!")
        guess_button.config(state=tk.DISABLED)
    elif guesses >= 6:
        message.set(f"You lose. The word was: {chosen_word}")
        guess_button.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Hangman Game")

word_display = tk.StringVar()
guessed_display = tk.StringVar()
hangman_display = tk.StringVar()
message = tk.StringVar()

word_display.set(" ".join(display))
guessed_display.set("Guessed letters: ")
hangman_display.set(HANGMANPICS[guesses])
message.set("")

title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 20))
word_label = tk.Label(root, textvariable=word_display, font=("Helvetica", 18))
guessed_label = tk.Label(root, textvariable=guessed_display, font=("Helvetica", 14))
hangman_label = tk.Label(root, textvariable=hangman_display, font=("Helvetica", 14))
message_label = tk.Label(root, textvariable=message, font=("Helvetica", 14), fg="red")
guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Helvetica", 14))

title_label.pack(pady=10)
word_label.pack(pady=10)
guessed_label.pack(pady=10)
hangman_label.pack(pady=10)
message_label.pack(pady=10)
guess_entry.pack(pady=10)
guess_button.pack(pady=10)

root.mainloop()
