#pragma once
#include "command_base.hpp"

class CurlCommand : public CommandBase {
public:
    CurlCommand();
    void setup() override;
    std::string describe(const std::vector<std::string>& args) override;
};