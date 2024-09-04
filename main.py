#!/usr/bin/env python3

import sys
import argparse

command_registry = {}

def register_command(cls):
    """Decorator to register command summary classes."""
    command_registry[cls.command_name] = cls
    return cls

class CommandSummary:
    """Base class for all command summaries."""
    command_name = None

    def __init__(self, command, args):
        self.command = command
        self.args = args

    def summarize(self):
        raise NotImplementedError("This method should be overridden by subclasses")


@register_command
class LsSummary(CommandSummary):
    command_name = "ls"

    def summarize(self):
        directory = '.'
        long_format = False
        show_all = False
        reverse_order = False
        sort_by_time = False
        human_readable = False

        options_dict = {
            '-l': 'long format (detailed information)',
            '-a': 'including hidden files',
            '-r': 'reverse order while sorting',
            '-t': 'sort by modification time',
            '-h': 'with human-readable file sizes',
        }

        options_summary = []

        for arg in self.args:
            if arg.startswith('-'):
                for char in arg[1:]:
                    option = f'-{char}'
                    if option == '-l':
                        long_format = True
                    elif option == '-a':
                        show_all = True
                    elif option == '-r':
                        reverse_order = True
                    elif option == '-t':
                        sort_by_time = True
                    elif option == '-h':
                        human_readable = True
                    if option in options_dict:
                        options_summary.append(f"{char}: {options_dict[option]}")
            elif not arg.startswith('-'):
                directory = arg

        summary = f"Lists the contents of {directory}"

        if options_summary:
            summary += " with the following options:\n" + "\n".join(options_summary)
        else:
            summary += "."

        return summary


@register_command
class GrepSummary(CommandSummary):
    command_name = "grep"

    def summarize(self):
        options_summary = []
        pattern = None
        files = []

        options_dict = {
            '-c': 'prints only a count of the lines with the pattern',
            '-h': 'displays matched lines but not the filenames',
            '-i': 'ignores case distinctions in the pattern',
            '-l': 'prints only the names of files with matching lines',
            '-n': 'prints line numbers with output lines',
            '-v': 'inverts the match to select non-matching lines',
            '-w': 'matches only whole words',
            '-r': 'searches directories recursively',
            '-A': 'prints N lines of trailing context after matching lines',
            '-B': 'prints N lines of leading context before matching lines',
            '-C': 'prints N lines of context around matching lines'
        }

        for arg in self.args:
            if arg.startswith('-'):
                for char in arg[1:]:
                    option = f'-{char}'
                    if option in options_dict:
                        options_summary.append(f"{char}: {options_dict[option]}")
            elif pattern is None:
                pattern = arg
            else:
                files.append(arg)

        summary = f"Searches for all lines containing the pattern '{pattern}'"

        if files:
            if len(files) == 1:
                summary += f" in the file '{files[0]}'"
            else:
                summary += f" in the files: {', '.join(files)}"

        if options_summary:
            summary += " with the following options:\n" + "\n".join(options_summary)

        return summary if pattern else "Invalid grep command format."


@register_command
class CatSummary(CommandSummary):
    command_name = "cat"

    def summarize(self):
        options_dict = {
            '-n': 'numbers all output lines',
            '-b': 'numbers only non-blank lines',
            '-s': 'suppress repeated empty output lines'
        }

        options_summary = []
        files = []

        for arg in self.args:
            if arg.startswith('-'):
                for char in arg[1:]:
                    option = f'-{char}'
                    if option in options_dict:
                        options_summary.append(f"{char}: {options_dict[option]}")
            else:
                files.append(arg)

        if not files:
            return "No file specified for cat command."

        summary = f"Displays the contents of {' and '.join(files)}"

        if options_summary:
            summary += " with the following options:\n" + "\n".join(options_summary)
        else:
            summary += "."

        return summary

def main():
    parser = argparse.ArgumentParser(description="Summarize Linux commands.")
    parser.add_argument('command_string', nargs=argparse.REMAINDER, help="The command and arguments to summarize")
    args = parser.parse_args()

    if not args.command_string:
        print("No command provided.")
        return

    command = args.command_string[0]
    command_args = args.command_string[1:]

    summary_class = command_registry.get(command)

    if summary_class:
        summary_instance = summary_class(command, command_args)
        print(summary_instance.summarize())
    else:
        print(f"No summary available for command: {command}")

if __name__ == "__main__":
    main()
