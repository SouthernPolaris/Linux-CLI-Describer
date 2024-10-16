import unittest
from cli_parser.commands.ls_summary import LsSummary

class TestLsSummary(unittest.TestCase):
    
    def test_ls_basic(self):
        ls = LsSummary("ls", ["-l"])
        self.assertEqual(
            ls.summarize(), 
            "Lists the contents of the current directory with the following options:\n"
            "l: long format (detailed information)."
        )

    def test_ls_with_directory(self):
        ls = LsSummary("ls", ["-la", "/home"])
        self.assertEqual(
            ls.summarize(), 
            "Lists the contents of /home with the following options:\n"
            "l: long format (detailed information)\n"
            "a: including hidden files."
        )

    def test_ls_multiple_options(self):
        ls = LsSummary("ls", ["-ltrh", "/var/log"])
        self.assertEqual(
            ls.summarize(), 
            "Lists the contents of /var/log with the following options:\n"
            "l: long format (detailed information)\n"
            "t: sort by modification time\n"
            "r: reverse order while sorting\n"
            "h: with human-readable file sizes."
        )

if __name__ == '__main__':
    unittest.main()
