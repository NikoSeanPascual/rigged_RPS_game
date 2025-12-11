import random

hangman = [
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    r"""
     +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========="""
]

questions = {
    "What is the capital of France?": "paris",
    "What is the largest planet in our solar system?": "jupiter",
    "Who wrote 'Hamlet'?": "shakespeare",
    "What is the speed of light?": "299792458",
    "What is the smallest ocean on Earth?": "arctic"
}


def random_question():
    question, answer = random.choice(list(questions.items()))
    return question, answer.lower()


def print_game_state(answer, guessed_letters, wrong_guesses):
    word_state = "".join([letter if letter in guessed_letters else "_" for letter in answer])
    print(f"Word: {word_state}")
    print(hangman[wrong_guesses])
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Remaining wrong guesses: {6 - wrong_guesses}")


def guess(letter, answer, guessed_letters, wrong_guesses):
    if len(letter) > 1:
        if letter == answer:
            return True, guessed_letters, wrong_guesses
        else:
            wrong_guesses += 1
            return False, guessed_letters, wrong_guesses

    if letter in guessed_letters:
        print("You already guessed that letter!")
        return False, guessed_letters, wrong_guesses

    guessed_letters.append(letter)

    if letter in answer:
        print(f"Good guess! {letter} is in the word!")
        return False, guessed_letters, wrong_guesses
    else:
        print(f"Oops! {letter} is not in the word.")
        wrong_guesses += 1
        return False, guessed_letters, wrong_guesses


def play_game():
    question, answer = random_question()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print(f"Question: {question}")

    while wrong_guesses < max_wrong_guesses:
        print_game_state(answer, guessed_letters, wrong_guesses)

        letter = input("Enter a letter: ").lower()

        if len(letter) > 1:
            is_correct, guessed_letters, wrong_guesses = guess(letter, answer, guessed_letters, wrong_guesses)
        elif len(letter) == 1:
            is_correct, guessed_letters, wrong_guesses = guess(letter, answer, guessed_letters, wrong_guesses)
        else:
            print("Please enter at least one letter.")
            continue

        if all(letter in guessed_letters for letter in answer):
            print(f"Congratulations! You guessed the word: {answer}")
            print(f"You win! The correct answer was '{answer}'")
            break

        if wrong_guesses == max_wrong_guesses:
            print(f"You lost! The correct answer was: {answer}")
            break

if __name__ == "__main__":
    play_game()
