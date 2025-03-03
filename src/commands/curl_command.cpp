#include "commands/curl_command.hpp"

CurlCommand::CurlCommand() {
    name = "curl";
}

void CurlCommand::setup() {
    setDescription("Transfer data to/from a server");

    addOption("v", "Verbose mode");
}

std::string CurlCommand::describe(const std::vector<std::string>& args) {
    if (args.empty()) {
        return "Error: curl requires a URL argument";
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

    if (!pos_args.empty()) {
        result += "URL:\n";
        for (const auto& arg : pos_args) {
            result += arg + " ";
        }
        result += "\n";
    }

    return result;
}