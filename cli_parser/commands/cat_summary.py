from ..command_summary import CommandSummary
from ..command_registry import register_command

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
