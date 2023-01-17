use std::fs;
use std::env;
// use std::time::Instant;

fn main() {
    // let start = Instant::now();
    let filepath : &String = &(env::args().collect::<Vec<String>>())[1];
    let mut vertices : Vec<Vec<f64>> = Vec::new();
    let mut normals : Vec<Vec<f64>> = Vec::new();
    let mut textures : Vec<Vec<f64>> = Vec::new();
    let mut mesh : Vec<f64> = Vec::new();

    let file : String = fs::read_to_string(filepath).expect("could not open file");
    let lines : Vec<&str> = file.split("\n").collect();

    for line in lines {
        let line:Vec<&str>=line.split(" ").collect();
        match line[0] {
            "v"=>{
                let x : f64 = line[1].parse().unwrap();
                let y : f64 = line[2].parse().unwrap();
                let z : f64 = line[3].parse().unwrap();
                vertices.push(vec![x,y,z]);
            },
            "vn"=>{
                let nx : f64 = line[1].parse().unwrap();
                let ny : f64 = line[2].parse().unwrap();
                let nz : f64 = line[3].parse().unwrap();
                normals.push(vec![nx,ny,nz]);
            },
            "vt"=>{
                let s : f64 = line[1].parse().unwrap();
                let t : f64 = line[2].parse().unwrap();
                textures.push(vec![s,t]);
            },
            "f"=>{
                let triangles = line.len()-3; // calculate how much traingles we need to build a face
                let mut face_vertices : Vec<&Vec<f64>> = Vec::new();
                let mut face_normals : Vec<&Vec<f64>> = Vec::new();
                let mut face_textures : Vec<&Vec<f64>> = Vec::new();
                for element in line {
                    if element == "f" {continue}
                    let values : Vec<&str> = element.split("/").collect();
                    if values[0]==""||values[1]==""||values[2]==""{panic!("obj file contains element with missing atributes")}
                    face_vertices.push(&vertices[values[0].parse::<usize>().unwrap()-1]);
                    face_normals.push(&normals[values[2].parse::<usize>().unwrap()-1]);
                    face_textures.push(&textures[values[1].parse::<usize>().unwrap()-1]);
                }
                let mut vertex_order : Vec<usize> = Vec::new();
                for i in 0..triangles {
                    vertex_order.push(0);
                    vertex_order.push(i+1);
                    vertex_order.push(i+2);
                }
                for i in vertex_order {
                    for x in face_vertices[i] {mesh.push(*x);}
                    for x in face_textures[i] {mesh.push(*x);}
                    for x in face_normals[i] {mesh.push(*x);}
                }
            },
            _=>(),
        }
    }
}
