#include <gtest/gtest.h>
#include "commands/curl_command.hpp"

class CurlCommandTest : public ::testing::Test {
protected:
    void SetUp() override {
        curl.setup();
    }

    CurlCommand curl;
};

TEST_F(CurlCommandTest, CreatesCurlCommand) {
    EXPECT_EQ(curl.getName(), "curl");
}

TEST_F(CurlCommandTest, BasicURL) {
    std::vector<std::string> args = {"http://localhost:8080"};
    std::string result = curl.describe(args);
    EXPECT_TRUE(result.find("http://localhost:8080") != std::string::npos);
}

TEST_F(CurlCommandTest, HandleEmptyInput) {
    std::vector<std::string> args;
    std::string result = curl.describe(args);
    EXPECT_TRUE(result.find("Error") != std::string::npos);
}

TEST_F(CurlCommandTest, ParseBasicOptions) {
    std::vector<std::string> args = {"-v", "http://example.com"};
    std::string result = curl.describe(args);
    EXPECT_TRUE(result.find("Verbose mode") != std::string::npos);
}