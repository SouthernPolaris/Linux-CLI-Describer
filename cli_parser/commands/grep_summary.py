from ..command_summary import CommandSummary
from ..command_registry import register_command

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

        summary += "."

        return summary if pattern else "Invalid grep command format."

