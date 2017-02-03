import unittest
from unittest.mock import patch, call
import random_number_game


class TestGame(unittest.TestCase):


    @patch('random_number_game.randNumber', return_value=4)
    @patch('random_number_game.play_input', side_effect=[3, 10, 4])
    @patch('builtins.print')
    def test_play_game(self, mock_print, mock_guesses, mock_secret):

        random_number_game.main()

        # Create a list of expected call objects. These will be compared to the actual calls made
        # to the mock_print method.
        expected_calls = [ call('Number is to low!') , call('Number is to high!') , call('Great!') ]
        self.assertEqual(expected_calls, mock_print.call_args_list)


if __name__ == '__main__':
    unittest.main()
