import unittest
from cli_parser.commands.grep_summary import GrepSummary

class TestGrepSummary(unittest.TestCase):
    
    def test_grep_basic(self):
        grep = GrepSummary("grep", ["pattern", "file.txt"])
        self.assertEqual(grep.summarize(), "Searches for all lines containing the pattern pattern in the file 'file.txt'.")

    def test_grep_with_options(self):
        grep = GrepSummary("grep", ["-i", "pattern", "file.txt"])
        self.assertEqual(grep.summarize(), "Searches for all lines containing the pattern pattern in the file 'file.txt' with the following options:\ni: ignores case distinctions in the pattern.")

    def test_grep_with_multiple_files(self):
        grep = GrepSummary("grep", ["-l", "pattern", "file1.txt", "file2.txt"])
        self.assertEqual(grep.summarize(), "Searches for all lines containing the pattern pattern in the files: file1.txt, file2.txt with the following options:\nl: prints only the names of files with matching lines.")

    def test_grep_invalid(self):
        grep = GrepSummary("grep", [])
        self.assertEqual(grep.summarize(), "Invalid grep command format.")

if __name__ == '__main__':
    unittest.main()
