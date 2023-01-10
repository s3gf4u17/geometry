// ownership

// garbage collection - error free, faster write time, no control over memory, slower and upredictable runtime performance, larger program size
// manual memory management - control over memory, faster runtime, smaller program size, eror prone, slower write time
// ownership model - control over memory, error free, faster runtime, smaller program size, slower write time, high learning curve

// ----- ownership rules -----
// 1. each value in rust has a variable thats called its owner
// 2. there can only be one owner at a time
// 3. when the owner goes out of scope, the value will be dropped

fn main () {
    let a = 5; // stack variable
    let b = a; // copy
    println!("{} {}",a,b);
    let s1 = String::from("string"); // heap variable 
    let s2 = s1; // transfer ownership
    // ERROR println!("{} {}",s1,s2); - ownership transfered from s1 to s2
    println!("{}",s2);
}