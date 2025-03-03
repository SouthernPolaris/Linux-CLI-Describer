#include "commands/grep_command.hpp"
#include "commands/curl_command.hpp"
#include <iostream>
#include <map>
#include <memory>

using CommandPtr = std::unique_ptr<CommandBase>;
using CommandRegistry = std::map<std::string, CommandPtr>;

CommandPtr createCommand(const std::string &name) {
    if (name == "grep") {
        auto cmd = std::make_unique<GrepCommand>();
        cmd->setup();
        return cmd;
    }

    if (name == "curl") {
        auto cmd = std::make_unique<CurlCommand>();
        cmd->setup();
        return cmd;
    }

    // TODO: Insert new commands here
    return nullptr;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " command [options] args..." << std::endl;
        return 1;
    }

    std::string commandName = argv[1];
    auto command = createCommand(commandName);
    
    if (!command) {
        std::cout << "Unknown command: " << commandName << std::endl;
        return 1;
    }

    // Skip program name and command name
    std::vector<std::string> args(argv + 2, argv + argc);
    std::cout << command->describe(args) << std::endl;

    return 0;
}