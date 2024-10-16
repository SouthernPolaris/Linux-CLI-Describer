#!/usr/bin/env python3

import sys
import argparse
from cli_parser.command_registry import command_registry

import cli_parser.commands.ls_summary
import cli_parser.commands.grep_summary
import cli_parser.commands.cat_summary

def execute_command(command_string):
    command_strings = ' '.join(command_string).split('|')
    previous_output = None  # To hold the output from the previous command
    output_collection = []  # To collect all outputs

    for idx, cmd_string in enumerate(command_strings):
        cmd_string = cmd_string.strip()  # Clean up any extra spaces
        command_parts = cmd_string.split()

        command = command_parts[0] # Command
        command_args = command_parts[1:] # Arguments

        summary_class = command_registry.get(command)

        if summary_class:
            summary_instance = summary_class(command, command_args)
            output = summary_instance.summarize()  # Get the summary output

            if previous_output is not None and idx > 0:
                input_context = f"The output of '{command_strings[idx - 1].strip()}' serves as input for '{command}'."
                output = f"{input_context}\n[output of previous command]{command_args[0].strip('\'\"')}\n\n{output}"

            output_collection.append(f"The output of '{cmd_string}' is:\n{output}\n")
            previous_output = output
        else:
            output_collection.append(f"No summary available for command: {command}\n")

    return ''.join(output_collection)

def main():
    parser = argparse.ArgumentParser(description="Summarize Linux commands.")
    parser.add_argument('command_string', nargs=argparse.REMAINDER, help="The command and arguments to summarize")
    args = parser.parse_args()

    if not args.command_string:
        return "No command provided."  # Return value for testing

    # Execute the command logic and return the result
    return execute_command(args.command_string)

if __name__ == "__main__":
    result = main()
    if result:
        print(result)