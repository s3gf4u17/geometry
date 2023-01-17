cmake_minimum_required(VERSION 3.22.1)

project(cpp-libraries)

add_executable(${PROJECT_NAME} main.cpp)

add_subdirectory(lib)

add_subdirectory(import/glfw)

target_include_directories(${PROJECT_NAME}
    PUBLIC lib
    PUBLIC import/glfw/include
)

target_link_directories(${PROJECT_NAME}
    PUBLIC lib
    PUBLIC import/glfw/src
)

target_link_libraries(${PROJECT_NAME} lib glfw)