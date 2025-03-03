#include <gtest/gtest.h>
#include "single_tests/test_grep.hpp"
#include "single_tests/test_curl.hpp"

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}