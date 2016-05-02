cmake_minimum_required(VERSION 3.5)
project(Cpp_Programming_Introduction)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(Cpp_Programming_Introduction ${SOURCE_FILES})