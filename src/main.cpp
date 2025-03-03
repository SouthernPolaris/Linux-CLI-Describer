#include "command_registry.hpp"
#include <vector>
#include <iostream>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " command [options] args..." << std::endl;
        return 1;
    }

    std::string commandName = argv[1];
    auto command = CommandRegistry::instance().createCommand(commandName);
    
    if (!command) {
        std::cout << "Unknown command: " << commandName << std::endl;
        return 1;
    }

    // Skip program name and command name
    std::vector<std::string> args(argv + 2, argv + argc);
    std::cout << command->describe(args) << std::endl;

    return 0;
}