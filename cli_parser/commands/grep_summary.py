from ..command_summary import CommandSummary
from ..command_registry import register_command

@register_command
class GrepSummary(CommandSummary):
    command_name = "grep"

    def summarize(self):
        """Summarize the 'grep' command options, pattern, and files to search."""
        pattern, files, options_summary = self.process_arguments()

        summary = self.build_summary(pattern, files, options_summary)
        
        return summary

    def process_arguments(self):
        """Process command-line arguments to identify options, pattern, and files."""
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
            if self.is_option(arg):
                options_summary.extend(self.get_option_summary(arg[1:], options_dict))
            elif pattern is None:
                pattern = arg
            else:
                files.append(arg)

        return pattern, files, options_summary
    
    def is_option(self, arg):
        """Check if the argument is an option (starts with '-')."""
        return arg.startswith('-')

    def get_option_summary(self, option_string, options_dict):
        """Return summaries for each option in the given option string."""
        options_summary = []
        for char in option_string:
            option = f'-{char}'
            if option in options_dict:
                summary = f"{char}: {options_dict[option]}"
                options_summary.append(summary)
        return options_summary

    def build_summary(self, pattern, files, options_summary):
        """Construct the summary output based on the pattern, files, and options."""
        if pattern is None:
            return "Invalid grep command format."

        summary = f"Searches for all lines containing the pattern {pattern} in the file"

        if files:
            if len(files) == 1:
                summary += f" '{files[0]}'"
            else:
                summary += f"s: {', '.join(files)}"

        if options_summary:
            summary += " with the following options:\n" + "\n".join(options_summary)

        return summary + "."
