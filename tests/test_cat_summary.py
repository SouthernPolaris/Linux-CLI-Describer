import unittest
from cli_parser.commands.cat_summary import CatSummary

class TestCatSummary(unittest.TestCase):

    def test_cat_basic(self):
        cat = CatSummary("cat", ["file.txt"])
        self.assertEqual(cat.summarize(), "Displays the contents of file.txt.")

    def test_cat_with_options(self):
        cat = CatSummary("cat", ["-n", "file.txt"])
        self.assertEqual(cat.summarize(), "Displays the contents of file.txt with the following options:\nn: numbers all output lines")

    def test_cat_multiple_files(self):
        cat = CatSummary("cat", ["-b", "file1.txt", "file2.txt"])
        self.assertEqual(cat.summarize(), "Displays the contents of file1.txt and file2.txt with the following options:\nb: numbers only non-blank lines")

    def test_cat_no_file(self):
        cat = CatSummary("cat", [])
        self.assertEqual(cat.summarize(), "No file specified for cat command.")

if __name__ == '__main__':
    unittest.main()
