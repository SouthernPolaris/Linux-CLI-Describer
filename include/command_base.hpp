#pragma once

#include <string>
#include <vector>
#include <memory>
#include <map>

class CommandBase {
public:
    CommandBase() = default;
    virtual ~CommandBase() = default;
    virtual void setup() = 0;
    virtual std::string describe(const std::vector<std::string>& args);

protected:
    std::string name;
    std::string description;
    std::map<std::string, std::string> options;
    std::vector<std::string> examples;

    void setDescription(const std::string &description);
    void addOption(const std::string &name, const std::string &description);
    void addExample(const std::string &example);
    // std::string describe(const std::vector<std::string>& args);
    std::pair<std::vector<std::string>, std::vector<std::string>> parseArgs(const std::vector<std::string>& args);
public:
    std::string getName();
};