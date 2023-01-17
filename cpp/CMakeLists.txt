cmake_minimum_required(VERSION 3.14)
project(cpp)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 14)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/934542165899c786cb5d8a710529c37184730183.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

file(GLOB_RECURSE sources src/*.cpp src/*.h)
file(GLOB_RECURSE sources_test tests/*.cc)

enable_testing()

add_executable(
  tests
  ${sources_test}
)
target_link_libraries(
  tests
  GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(tests)