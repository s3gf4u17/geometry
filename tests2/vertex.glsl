#version 330 core

layout (location = 0) in vec3 aPos;
// layout (location = 1) in vec3 color; // if sending color in vao

out vec3 colorPosition;
out vec2 texturePosition;

// out vec4 vertexColor;

void main()
{
gl_Position = vec4(aPos, 1.0);
colorPosition = aPos;
texturePosition = vec2(aPos.x,aPos.y);
// vertexColor = vec4(255f/255f, 42f/255f, 38f/255f, 1.0f);
// gl_Position = vec4(aPos.xyz, 1.0); // aPos as a vec3
// gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}