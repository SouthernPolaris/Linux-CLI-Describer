#include <gtest/gtest.h>
#include "commands/grep_command.hpp"

class GrepCommandTest : public ::testing::Test {
protected:
    void SetUp() override {
        grep.setup();
    }

    GrepCommand grep;
};

TEST_F(GrepCommandTest, CreatesGrepCommand) {
    EXPECT_EQ(grep.getName(), "grep");
}

TEST_F(GrepCommandTest, ParseBasicOptions) {
    std::vector<std::string> args = {"-i", "-r", "pattern", "file.txt"};
    std::string result = grep.describe(args);
    EXPECT_TRUE(result.find("Case-insensitive") != std::string::npos);
}

TEST_F(GrepCommandTest, HandleEmptyInput) {
    std::vector<std::string> args;
    std::string result = grep.describe(args);
    EXPECT_TRUE(result.find("Error") != std::string::npos);
}

TEST_F(GrepCommandTest, HandleMultipleFiles) {
    std::vector<std::string> args = {"pattern", "file1.txt", "file2.txt"};
    std::string result = grep.describe(args);
    EXPECT_TRUE(result.find("file1.txt") != std::string::npos);
    EXPECT_TRUE(result.find("file2.txt") != std::string::npos);
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}