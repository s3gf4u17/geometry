// collection

// normal arrays and tuples are stored on the stack (cant be resized)

fn main() {
    // vectors <- have to be mutable if we want to change
    let mut v1 : Vec<i32> = Vec::new(); // initialize 1 using associated function
    v1.push(1);
    let v2 = vec![1,2,3]; // initialize 2 using vec macro
    println!("{:?} {:?}",v1,v2);
}