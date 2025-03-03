cmake_minimum_required(VERSION 3.14)
project(cli_describer)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG main
)

FetchContent_MakeAvailable(googletest)

enable_testing()

add_library(cli_describer
    src/command_base.cpp
    src/commands/grep_command.cpp
    src/commands/curl_command.cpp
)

target_include_directories(cli_describer 
    PUBLIC 
    ${PROJECT_SOURCE_DIR}/include
)

add_executable(command_base src/main.cpp)
target_link_libraries(command_base 
    PRIVATE 
    cli_describer
)

add_executable(test_grep tests/test_grep.cpp)
target_link_libraries(test_grep
    PRIVATE
    cli_describer
    GTest::gtest
    GTest::gtest_main
)

add_executable(test_curl tests/test_curl.cpp)
target_link_libraries(test_curl
    PRIVATE
    cli_describer
    GTest::gtest
    GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(test_grep)
gtest_discover_tests(test_curl)