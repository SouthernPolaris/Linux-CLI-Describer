import unittest
from main import main
from unittest.mock import patch
import sys

class TestMain(unittest.TestCase):
    @patch('sys.stdout')
    def test_no_command(self, mock_stdout):
        with patch.object(sys, 'argv', ['main.py']):
            output = main()
        self.assertEqual(output, "No command provided.") 

    @patch('sys.stdout')
    def test_ls_command(self, mock_stdout):
        with patch.object(sys, 'argv', ['main.py', 'ls', '-la']):
            output = main()
        
        expected_output = (
            "The output of 'ls -la' is:\n"
            "Lists the contents of the current directory with the following options:\n"
            "l: long format (detailed information)\n"
            "a: including hidden files.\n"
        )
        self.assertEqual(output, expected_output)

    @patch('sys.stdout')
    def test_grep_command(self, mock_stdout):
        pattern = 'current'
        expected_output = (
            "The output of 'grep current' is:\n"
            "Searches for all lines containing the pattern current in the file."
        )

        with patch.object(sys, 'argv', ['main.py', 'grep', pattern]):
            output = main()

        self.assertEqual(output.strip(), expected_output.strip())

    @patch('sys.stdout')
    def test_cat_command(self, mock_stdout):
        with patch.object(sys, 'argv', ['main.py', 'cat', 'example.txt']):
            output = main()

        expected_output = (
            "The output of 'cat example.txt' is:\n"
            "Displays the contents of example.txt."
        )

        self.assertEqual(output.strip(), expected_output.strip())

    @patch('sys.stdout')
    def test_invalid_command(self, mock_stdout):
        with patch.object(sys, 'argv', ['main.py', 'unknowncmd']):
            output = main()
        self.assertEqual(output, "No summary available for command: unknowncmd\n")

if __name__ == "__main__":
    unittest.main()
