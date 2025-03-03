#pragma once
#include "command_base.hpp"

class GrepCommand : public CommandBase {
public:
    GrepCommand();
    void setup() override;
    std::string describe(const std::vector<std::string>& args) override;

};