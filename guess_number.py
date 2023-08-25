"""guess number game"""
import random
import sys


class GuessNumber:
    """
    A class to play guess number game
    """

    # init the given number and attempt times
    def __init__(self):
        self.number = self.generate_number()
        self.attempts = 0

    def generate_number(self):
        """
        Generate a 4 digit random number
        """
        return ''.join(random.sample("0123456789", 4))

    def check_is_guess_right(self, guess):
        """
        Check if the input number is the right number.
        """
        self.attempts += 1
        result = ''
        for i in range(4):
            if guess[i] == self.number[i]:
                result += 'O'
            elif guess[i] in self.number:
                result += 'X'
            else:
                result += ' '
        if result == '    ':
            result = 'No digit is right.'
        return result

    def quit_game(self):
        """
        The function to quit game
        """
        sys.exit()

    def play_game(self):
        """
        The function to play game
        """
        print("Welcome to the number guessing game!")
        print("You can type 'q' to exit at any time.")
        while True:
            print("A new game has started.")
            self.number = self.generate_number()
            self.attempts = 0

            while True:
                guess = input("Input your guess(four-digit number): ")

                if guess == 'q':
                    self.quit_game()

                # check if the input is valid
                if len(guess) != 4 or not guess.isdigit():
                    print("Invalid input. Please enter a four digit number.")
                    continue

                result = self.check_is_guess_right(guess)

                if result == 'OOOO':  # guess the right number
                    print("Congratulation! You guess the right number.")
                    print(f"It took you {self.attempts} attempts.")
                    break
                # guess failed
                print("Clue: " + result)

            # after win the game, choose if play again.
            play_again = input(
                "type 'y' to play again, type any other word to quit:")
            if play_again != 'y':
                sys.exit()


def main():
    """
    Run the game
    """
    game = GuessNumber()
    game.play_game()


if __name__ == "__main__":
    main()
