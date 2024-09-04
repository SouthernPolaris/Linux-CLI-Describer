class CommandSummary:
    """Base class for all command summaries."""
    command_name = None

    def __init__(self, command, args):
        self.command = command
        self.args = args

    def summarize(self):
        raise NotImplementedError("This method should be overridden by subclasses")
