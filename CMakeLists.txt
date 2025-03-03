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
    src/command_registry.cpp
    src/commands/grep_command.cpp
    src/commands/curl_command.cpp
)

target_include_directories(cli_describer 
    PUBLIC 
    ${PROJECT_SOURCE_DIR}/include
)

add_executable(cli_describe src/main.cpp)
target_link_libraries(cli_describe 
    PRIVATE 
    cli_describer
)

add_executable(unit_tests tests/test_main.cpp)
target_link_libraries(unit_tests
    PRIVATE
    cli_describer
    GTest::gtest
    GTest::gtest_main
)


include(GoogleTest)
gtest_discover_tests(unit_tests)