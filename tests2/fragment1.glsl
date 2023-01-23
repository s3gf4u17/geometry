#version 330 core

out vec4 FragColor;

in vec3 colorPosition;

void main()
{
FragColor = vec4(colorPosition,1.0f);
}