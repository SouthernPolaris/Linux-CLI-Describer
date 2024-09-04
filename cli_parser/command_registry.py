command_registry = {}

def register_command(cls):
    """Decorator to register command summary classes."""
    command_registry[cls.command_name] = cls
    return cls
