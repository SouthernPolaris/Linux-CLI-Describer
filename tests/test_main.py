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
        expected_output = "Lists the contents of the current directory with the following options:\nl: long format (detailed information)\na: including hidden files."

        self.assertEqual(output, expected_output)

    @patch('sys.stdout')
    def test_invalid_command(self, mock_stdout):
        with patch.object(sys, 'argv', ['main.py', 'unknowncmd']):
            output = main()
        self.assertEqual(output, "No summary available for command: unknowncmd")

if __name__ == "__main__":
    unittest.main()
