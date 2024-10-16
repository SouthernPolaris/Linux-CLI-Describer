from ..command_summary import CommandSummary
from ..command_registry import register_command

@register_command
class CatSummary(CommandSummary):
    command_name = "cat"

    def summarize(self):
        """Summarize the 'cat' command options and files to display."""
        options_summary, files = self.process_arguments()

        summary = self.build_summary(files, options_summary)
        
        return summary

    def process_arguments(self):
        """Process command-line arguments to identify options and files."""
        options_dict = {
            '-n': 'numbers all output lines',
            '-b': 'numbers only non-blank lines',
            '-s': 'suppress repeated empty output lines'
        }

        options_summary = []
        files = []

        for arg in self.args:
            if self.is_option(arg):
                options_summary.extend(self.get_option_summary(arg[1:], options_dict))
            else:
                files.append(arg)

        return options_summary, files

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

    def build_summary(self, files, options_summary):
        """Construct the summary output based on the files and options."""
        if not files:
            return "No file specified for cat command."

        summary = f"Displays the contents of {' and '.join(files)}"

        if options_summary:
            summary += " with the following options:\n" + "\n".join(options_summary)
        else:
            summary += "."

        return summary
