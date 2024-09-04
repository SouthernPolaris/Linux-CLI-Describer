from ..command_summary import CommandSummary
from ..command_registry import register_command

@register_command
class LsSummary(CommandSummary):
    command_name = "ls"

    def summarize(self):
        directory = 'the current directory'
        options_summary = []
        options_dict = {
            '-l': 'long format (detailed information)',
            '-a': 'including hidden files',
            '-r': 'reverse order while sorting',
            '-t': 'sort by modification time',
            '-h': 'with human-readable file sizes',
        }

        for arg in self.args:
            if arg.startswith('-'):
                for char in arg[1:]:
                    option = f'-{char}'
                    if option in options_dict:
                        options_summary.append(f"{char}: {options_dict[option]}")
            else:
                directory = arg

        summary = f"Lists the contents of {directory}"

        if options_summary:
            summary += " with the following options:\n" + "\n".join(options_summary)
        summary += "."

        return summary