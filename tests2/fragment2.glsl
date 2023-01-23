#version 330 core
out vec4 FragColor;
in vec2 texturePosition;

uniform sampler2D myTexture;

void main()
{
    FragColor = texture(myTexture,texturePosition);
// FragColor = vec4(texturePosition,0.0f, 1.0f);
}