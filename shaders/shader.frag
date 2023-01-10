#version 330 core

in vec2 fragmentTexCoord;

out vec4 color;

uniform sampler2D imageTexture;

void main(){
    color = texture(imageTexture,fragmentTexCoord);
}