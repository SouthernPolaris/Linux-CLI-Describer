#include "commands/grep_command.hpp"

GrepCommand::GrepCommand() {
    name = "grep";
}

void GrepCommand::setup() {
    setDescription("Search for a pattern in a file");
    addOption("i", "Case-insensitive search");
    addOption("r", "Recursive search");
    addOption("c", "Count matches");
    addOption("n", "Show line numbers");
    addOption("l", "Show only the names of files with matches");
}

std::string GrepCommand::describe(const std::vector<std::string>& args) {
    if (args.empty()) {
        return "Error: grep requires a pattern and file argument";
    }

    auto [options, pos_args] = parseArgs(args);
    std::string result = "Command: " + name + "\n";
    result += "Description: " + description + "\n\n";

    if (!options.empty()) {
        result += "Options:\n";
        for (const auto& opt : options) {
            if (this->options.count(opt)) {
                result += "  -" + opt + ": " + this->options.at(opt) + "\n";
            }
        }
        result += "\n";
    }

    if (pos_args.empty()) {
        return result + "Error: No pattern or files specified";
    }

    result += "Pattern: '" + pos_args[0] + "'\n";
    if (pos_args.size() > 1) {
        result += "Files: ";
        for (size_t i = 1; i < pos_args.size(); ++i) {
            result += pos_args[i] + " ";
        }
        result += "\n";
    }

    return result;
}