cmake_minimum_required(VERSION 3.22.1)

project(tests)

add_executable(${PROJECT_NAME} main.cpp)

add_subdirectory(glad)
add_subdirectory(glfw)

target_include_directories(${PROJECT_NAME}
    PUBLIC glfw/include
)

target_link_directories(${PROJECT_NAME}
    PUBLIC glfw/src
)

target_link_libraries(${PROJECT_NAME}
    PUBLIC glad
    PUBLIC glfw
)