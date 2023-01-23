#version 330 core
out vec4 FragColor;
// in vec4 vertexColor; // we set this variable as out in shader before (ex vertex)
uniform vec4 myColor; // we set this variable in the opengl code
void main()
{
FragColor = myColor;
}