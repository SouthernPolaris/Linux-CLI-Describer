#pragma once
#include "command_base.hpp"
#include "commands/curl_command.hpp"
#include "commands/grep_command.hpp"
#include <map>
#include <memory>
#include <string>

using CommandPtr = std::unique_ptr<CommandBase>;

class CommandRegistry {
public:
    CommandPtr createCommand(const std::string &name);
    static CommandRegistry& instance();

private:
    CommandRegistry() = default;
    std::map<std::string, CommandPtr> commands;
};