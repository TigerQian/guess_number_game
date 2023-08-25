"""Test the function of guess number game"""
import unittest
from unittest.mock import patch
from guess_number import GuessNumber


class TestGuessTheNumber(unittest.TestCase):
    """The class to test the function of guess number game"""
    game = GuessNumber()

    def test_generate_number(self):
        """
        test if generate_number function is successfully
        generate a 4 digit random number.
        """
        number = self.game.generate_number()
        self.assertEqual(len(number), 4)
        self.assertTrue(number.isdigit())

    def test_guess_correct(self):
        """
        test the condition that the input number is right.
        """
        self.game.number = "1234"
        result = self.game.check_is_guess_right("1234")
        self.assertEqual(result, 'OOOO')

    def test_guess_wrong(self):
        """
        test the condition that the input number is wrong.
        """
        self.game.number = "1234"
        self.assertEqual(self.game.check_is_guess_right("4321"), 'XXXX')
        self.assertEqual(self.game.check_is_guess_right("1111"), 'OXXX')
        self.assertEqual(self.game.check_is_guess_right("1999"), 'O   ')
        self.assertEqual(self.game.check_is_guess_right("9299"), ' O  ')
        self.assertEqual(self.game.check_is_guess_right("9939"), '  O ')
        self.assertEqual(self.game.check_is_guess_right("9934"), '  OO')
        # No digit is right or contained in given number
        # will return 'No digits are correct.'
        self.assertEqual(self.game.check_is_guess_right("9999"),
                         'No digit is right.')

    def test_count_attempts(self):
        """
        test if the attempt times is right.
        """
        self.game.number = "1234"
        self.game.check_is_guess_right("4321")
        self.game.check_is_guess_right("1324")
        self.assertEqual(self.game.attempts, 2)

    def test_quit_game(self):
        """
        test if the game will quit successfully.
        """
        with self.assertRaises(SystemExit):
            self.game.quit_game()

    @patch('builtins.input',
           side_effect=['123', 'ww', '1111', '2211', '2222', '1234', 'aaa'])
    @patch('random.sample', return_value=['1', '2', '3', '4'])
    def test_play_game(self, _, __):
        """
        test if the game will run successfully and return the right attempts.
        The first two input is wrong input. The 6th number is right number,
        then put any word to quit game.
        """
        game = GuessNumber()
        with self.assertRaises(SystemExit):
            game.play_game()
        # check if the attempt times is 4,
        # the wrong input is not counted.
        self.assertEqual(game.attempts, 4)


if __name__ == '__main__':
    unittest.main()
