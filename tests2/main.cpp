#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <math.h>
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

struct Geometry {
    unsigned int VAO;
    unsigned int VBO;
    unsigned int EBO;
    unsigned int program;
    int tcount;
}; // hold VAO, VBO, EBO, shader program, EBO size of a geometry

unsigned int createShader(std::string source, int type); // create shader from .glsl file

unsigned int createProgram(std::vector<unsigned int> shaders); // link shaders and compile them into one program

Geometry createGeometry(float *vertices, int versize, unsigned int *indices, int indsize, unsigned int program); // return geometry with VAO, VBO && EBO buffers

void deleteShaders(std::vector<unsigned int> shaders); // free memory when shaders no longer used

void framebuffer_size_callback(GLFWwindow* window, int width, int height); // resize opengl viewport on window resize

void processInput(GLFWwindow *window); // react to user input

int main()
{
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    //glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
  
    GLFWwindow* window = glfwCreateWindow(400, 300, "LearnOpenGL", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    glViewport(0, 0, 400, 300);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    unsigned int vertexShader = createShader("vertex.glsl",GL_VERTEX_SHADER);
    unsigned int fragmentShader1 = createShader("fragment1.glsl",GL_FRAGMENT_SHADER);
    unsigned int fragmentShader2 = createShader("fragment2.glsl",GL_FRAGMENT_SHADER);
    unsigned int fragmentShader3 = createShader("fragment3.glsl",GL_FRAGMENT_SHADER);
    unsigned int shaderProgram1 = createProgram(std::vector<unsigned int>{vertexShader,fragmentShader1});
    unsigned int shaderProgram2 = createProgram(std::vector<unsigned int>{vertexShader,fragmentShader2});
    unsigned int shaderProgram3 = createProgram(std::vector<unsigned int>{vertexShader,fragmentShader3});

    Geometry geoms[3];

    float vertices1[] = {1.0f,1.0f,0.0f,1.0f,0.0f,0.0f,0.0f,0.0f,0.0f,0.0f, 1.0f,0.0f};
    unsigned int indices1[] = {0,1,3,1,2,3}; 
    geoms[0] = createGeometry(vertices1,sizeof(vertices1),indices1,sizeof(indices1),shaderProgram1);

    float vertices2[] = {0.0f,0.0f,0.0f,1.0f,-1.0f,0.0f,1.0f,0.0f,0.0f,0.0f,-1.0f,0.0f};
    unsigned int indices2[] = {0, 1, 2,0,1,3};
    geoms[1] = createGeometry(vertices2,sizeof(vertices2),indices2,sizeof(indices2),shaderProgram2);

    float vertices3[] = {0.0f,0.0f,0.0f,-1.0f,0.0f,0.0f,-1.0f,1.0f,0.0f};
    unsigned int indices3[] = {0, 1, 2};
    geoms[2] = createGeometry(vertices3,sizeof(vertices3),indices3,sizeof(indices3),shaderProgram3);

    int width, height, nrChannels;
    unsigned char *data = stbi_load("textures/container.jpg", &width, &height, &nrChannels, 0);
    if (!data)
    {
        std::cout << "Failed to load texture" << std::endl;
    }
    unsigned int texture;
    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);	
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
    glGenerateMipmap(GL_TEXTURE_2D);
    stbi_image_free(data);

    // window render loop
    while(!glfwWindowShouldClose(window))
    {
        // handle user input
        processInput(window);

        // rendering
        // ...
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        for (Geometry geom : geoms) {
            glUseProgram(geom.program);
            float timeValue = glfwGetTime();
            float redValue = sin(timeValue) / 2.0f + 0.5f;
            int vertexColorLocation = glGetUniformLocation(geom.program, "myColor");
            glUniform4f(vertexColorLocation, redValue, 0.0f, 0.0f, 1.0f);
            glBindTexture(GL_TEXTURE_2D, texture);
            glBindVertexArray(geom.VAO);
            glDrawElements(GL_TRIANGLES,geom.tcount,GL_UNSIGNED_INT,0);
        }

        // check and call events and swap the buffers
        glBindVertexArray(0);
        glfwSwapBuffers(window);
        glfwPollEvents();    
    }

    deleteShaders(std::vector<unsigned int>{vertexShader,fragmentShader1,fragmentShader2,fragmentShader3});
    glfwTerminate();
    return 0;
}

unsigned int createShader(std::string source, int type){
    std::string sourceCode;
    char buff;
    std::fstream shaderFile(source);
    while (shaderFile >> std::noskipws >> buff) {sourceCode.push_back(buff);}
    const char *sourceCodeChar = sourceCode.c_str();

    unsigned int shader = glCreateShader(type);
    glShaderSource(shader, 1, &sourceCodeChar, NULL);
    glCompileShader(shader);
    // check compilation status
    int success;
    char infoLog[512];
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if(!success)
    {
        glGetShaderInfoLog(shader, 512, NULL, infoLog);
        std::cout << "ERROR::SHADER::COMPILATION_FAILED\n" << infoLog << std::endl;
    }
    return shader;
}

unsigned int createProgram(std::vector<unsigned int> shaders){
    unsigned int shaderProgram = glCreateProgram();
    for (unsigned int shader : shaders) {
        glAttachShader(shaderProgram, shader);
    }
    glLinkProgram(shaderProgram);
    int success;
    char infoLog[512];
    glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
    if(!success) {
        glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
        std::cout << "ERROR::PROGRAM::COMPILATION_FAILED\n" << infoLog << std::endl;
    }
    return shaderProgram;
}

void deleteShaders(std::vector<unsigned int> shaders) {
    for (unsigned int shader : shaders) {
        glDeleteShader(shader);
    }
}

void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}

void processInput(GLFWwindow *window) {
    if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) glfwSetWindowShouldClose(window, true);
}

Geometry createGeometry(float *vertices, int versize, unsigned int *indices, int indsize,unsigned int program){
    unsigned int VAO;
    glGenVertexArrays(1, &VAO);
    glBindVertexArray(VAO);
    unsigned int VBO;
    glGenBuffers(1, &VBO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, versize, vertices, GL_STATIC_DRAW);
    // attributes
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    unsigned int EBO;
    glGenBuffers(1, &EBO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indsize, indices, GL_STATIC_DRAW);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    Geometry geom;
    geom.VAO = VAO;
    geom.VBO = VBO;
    geom.EBO = EBO;
    geom.tcount = indsize;
    geom.program = program;
    return geom;
}