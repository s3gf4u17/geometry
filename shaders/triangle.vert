#version 330 core

//locations correspond to attributes specified with "glEnableVertexAttribArray"
layout (location=0) in vec3 vertexPos;
layout (location=1) in vec3 vertexColor;
layout (location=2) in vec2 vertexTexCoord;

//out will go into fragments shader as in
out vec3 fragmentColor;
out vec2 fragmentTexCoord;

void main() {
    gl_Position = vec4(vertexPos,1.0);
    fragmentColor=vertexColor;
    fragmentTexCoord=vertexTexCoord;
}