from ..command_summary import CommandSummary
from ..command_registry import register_command

@register_command
class LsSummary(CommandSummary):
    command_name = "ls"

    def summarize(self):
        """Summarize the 'ls' command options and the directory to be listed."""
        directory = 'the current directory'
        options_summary = []

        options_dict = {
            '-l': 'long format (detailed information)',
            '-a': 'including hidden files',
            '-r': 'reverse order while sorting',
            '-t': 'sort by modification time',
            '-h': 'with human-readable file sizes',
        }

        directory, options_summary = self.process_arguments(options_dict)

        summary = f"Lists the contents of {directory}"

        if options_summary:
            summary += " with the following options:\n" + "\n".join(options_summary)
        
        summary += "."

        return summary

    def process_arguments(self, options_dict):
        """Process command-line arguments to identify options and the directory."""
        options_summary = []
        directory = None

        for arg in self.args:
            if self.is_option(arg):
                options_summary.extend(self.get_option_summary(arg[1:], options_dict))
            else:
                directory = arg

        if directory is None:
            directory = 'the current directory'

        return directory, options_summary

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
