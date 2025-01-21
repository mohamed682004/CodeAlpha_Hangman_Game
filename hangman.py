import random
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    """Return a random word for the game."""
    words = ['python', 'programming', 'computer', 'algorithm', 'database', 
             'network', 'software', 'developer', 'debugging', 'application']
    return random.choice(words).upper()

def display_hangman(tries):
    """Return the hangman stages based on remaining tries."""
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def play_hangman():
    """Main game function."""
    word = get_word()
    word_letters = set(word)  # letters in the word
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()  # letters guessed by user

    tries = 6  # number of tries before game over

    # Game loop
    while len(word_letters) > 0 and tries > 0:
        clear_screen()
        print('\nYou have', tries, 'tries left.')
        print('\nUsed letters:', ' '.join(sorted(used_letters)))

        # Display the word with guessed letters
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(display_hangman(tries))
        print('Current word:', ' '.join(word_list))

        # Get player input
        guess = input('\nGuess a letter: ').upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print('\nGood guess!')
            else:
                tries -= 1
                print('\nWrong guess.')
        elif guess in used_letters:
            print('\nYou already used that letter. Please try again.')
        else:
            print('\nInvalid character. Please enter a letter.')

    # Game ended - display final state
    clear_screen()
    print(display_hangman(tries))
    if tries == 0:
        print(f'Sorry, you lost! The word was {word}')
    else:
        print(f'Congratulations! You guessed the word {word}!!')

def main():
    """Main game loop with play again functionality."""
    while True:
        play_hangman()
        if input("\nPlay again? (Y/N) ").upper() != 'Y':
            break
    print("\nThanks for playing!")

if __name__ == '__main__':
    main()