#version 330 core

//locations correspond to attributes specified with "glEnableVertexAttribArray"
layout (location=0) in vec3 vertexPos;
layout (location=1) in vec2 vertexTexCoord;

uniform mat4 model;
uniform mat4 projection;

//out will go into fragments shader as in
out vec2 fragmentTexCoord;

void main() {
    gl_Position = projection*model*vec4(vertexPos,1.0);
    fragmentTexCoord=vertexTexCoord;
}