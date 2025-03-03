#include "command_registry.hpp"

CommandPtr CommandRegistry::createCommand(const std::string &name) {
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
    return nullptr;
}

CommandRegistry &CommandRegistry::instance() {
    static CommandRegistry instance;
    return instance;
}