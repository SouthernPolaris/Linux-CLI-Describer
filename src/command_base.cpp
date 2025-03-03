#include "../include/command_base.hpp"
#include <sstream>
#include <algorithm>

void CommandBase::setDescription(const std::string &description) {
    this->description = description;
}

void CommandBase::addOption(const std::string &name, const std::string &description) {
    options[name] = description;
}

void CommandBase::addExample(const std::string &example) {
    examples.push_back(example);
}

std::string CommandBase::describe(const std::vector<std::string>& args) {
    auto [options_used, pos_args] = parseArgs(args);
    std::stringstream result;
    result << "Command: " << name << "\n";
    result << "Description: " << description << "\n\n";

    if (!options_used.empty()) {
        result << "Options:\n";
        for (const auto &opt : options_used) {
            auto it = options.find(opt);
            if (it != options.end()) {
                result << "  -" << opt << ": " << it->second << "\n";
            }
        }
        result << "\n";
    }

    if(!pos_args.empty()) {
        result << "Positional arguments:\n";
        for (const auto &arg : pos_args) {
            result << "  " << arg << "\n";
        }
        // result << "\n";
    }

    return result.str();
}

std::pair<std::vector<std::string>, std::vector<std::string>> CommandBase::parseArgs(const std::vector<std::string>& args) {
    std::vector<std::string> options_found;
    std::vector<std::string> pos_args;

    for (const auto& arg : args) {
        if (arg.size() > 1 && arg[0] == '-') {
            // Case of both single hyphen and double hyphen
            std::string opt = arg.substr(1);
            if (arg[1] == '-') {
                opt = arg.substr(2);
            }

            // Split combined options (-xyz) into (-x -y -z)
            for (char c : opt) {
                options_found.push_back(std::string(1, c));
            }
        } else {
            pos_args.push_back(arg);
        }
    }

    return {options_found, pos_args};
}

std::string CommandBase::getName() {
    return name;
}