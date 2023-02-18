# Intro
All data structure and algo are written in C++. Testing is done using Googletest. The folder structure is kept simple and shown below:
cpp
|- src
   |- .*h
   |- .cc
|- tests
   |- .cc
|- CMakeLists.txt
|- README.md

## Setup
The setup for testing follows the guide for **CMake** provided by GoogleTest which can be found [here](https://google.github.io/googletest/quickstart-cmake.html). If your preference is **Bazel**, please refer to [this](https://google.github.io/googletest/quickstart-bazel.html) and ignore the setup here.

The only difference in the [CMakeLists.txt](./CMakeLists.txt) compared to what is described in the GoogleTest doc is:
```txt
file(GLOB_RECURSE sources src/*.cpp src/*.h)    #load all the source files recursively
file(GLOB_RECURSE sources_test tests/*.cc)      #load all the test files recursively

enable_testing()

add_executable(
  tests
  ${sources_test}                               # Add executable by passing the testfile              #
)
```
