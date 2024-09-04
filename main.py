#!/usr/bin/env python3

import sys
import argparse
from cli_parser.command_registry import command_registry

import cli_parser.commands.ls_summary
import cli_parser.commands.grep_summary
import cli_parser.commands.cat_summary

def main():
    parser = argparse.ArgumentParser(description="Summarize Linux commands.")
    parser.add_argument('command_string', nargs=argparse.REMAINDER, help="The command and arguments to summarize")
    args = parser.parse_args()

    if not args.command_string:
        return "No command provided."  

    command = args.command_string[0]
    command_args = args.command_string[1:]

    summary_class = command_registry.get(command)

    if summary_class:
        summary_instance = summary_class(command, command_args)
        return summary_instance.summarize()
    else:
        return f"No summary available for command: {command}"

if __name__ == "__main__":
    main()
