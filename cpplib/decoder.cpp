#include <string>
#include <vector>
#include <iostream>
#include <fstream>

std::vector<std::string> split_string(std::string s,char delimiter) {
    int start=0;
    std::vector<std::string> vect;
    for (int i=0;i<s.length();i++) {
        if (s[i] == delimiter){
            std::string subs=s.substr(start,i-start);
            vect.push_back(subs);
            start=i+1;
        } else if (i==s.length()-1) {
            std::string subs=s.substr(start,i-start+1);
            vect.push_back(subs);
        }
    }
    return vect;
}

int main() {
    std::vector<std::vector<double>> vertices;
    std::vector<std::vector<double>> normals;
    std::vector<std::vector<double>> textures;
    std::vector<double> mesh;

    std::string buff;
    std::ifstream ObjectFile("cube.obj");
    while (getline(ObjectFile,buff)) {
        std::vector<std::string> ans = split_string(buff,' ');
        if (ans[0]=="v") {
            vertices.push_back({std::stod(ans[1]),std::stod(ans[2]),std::stod(ans[3])});
        } else if (ans[0]=="vn") {
            normals.push_back({std::stod(ans[1]),std::stod(ans[2]),std::stod(ans[3])});
        } else if (ans[0]=="vt") {
            textures.push_back({std::stod(ans[1]),std::stod(ans[2])});
        } else if (ans[0]=="f") {
            int triangles = ans.size()-3;
            std::vector<std::vector<double>> face_vertices;
            std::vector<std::vector<double>> face_normals;
            std::vector<std::vector<double>> face_textures;
            for (int i=1; i<ans.size();i++) {
                std::vector<std::string> face = split_string(ans[i],'/');
                if (face[0]==""||face[1]==""||face[2]=="") return 1;
                face_vertices.push_back(vertices[std::stoi(face[0])-1]);
                face_normals.push_back(normals[std::stoi(face[2])-1]);
                face_textures.push_back(textures[std::stoi(face[1])-1]);
            }
            std::vector<int> vertex_order;
            for (int i =0;i<triangles;i++){
                vertex_order.push_back(0);
                vertex_order.push_back(i+1);
                vertex_order.push_back(i+2);
            }
            for (int i: vertex_order) {
                for (double vertex : face_vertices[i]) mesh.push_back(vertex);
                for (double texture : face_textures[i]) mesh.push_back(texture);
                for (double normal : face_normals[i]) mesh.push_back(normal);
            }
        }
    }

    return 0;
}