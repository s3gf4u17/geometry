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
    let s2 = s1; // move ownership
    let s3 = s2.clone(); // creates a clone instead of moving ownership
    // ERROR println!("{} {}",s1,s2); - ownership transfered from s1 to s2
    println!("{} {}",s2,s3);
    takes_ownership(s3);
    // println!("{} {}",s2,s3); - s3 ownership moved
    makes_copy(b);
    println!("{}",b); // b still can be used (its stored on a stack)
    let s2=takes_and_gives_back(s2);
    println!("{}",s2); // s2 can still be used (ownership returned)

    let (len,s2) = calculate_length_ownership(s2);
    println!("{} {} {} {}",s2,len,calculate_length_reference(&s2),s2);
}

fn takes_ownership(s: String) {
    println!("{}",s);
}

fn makes_copy(i: i32) {
    println!("{}",i);
}

fn takes_and_gives_back(s: String) -> String {
    println!("{}",s);
    s
}

fn calculate_length_ownership(s:String) -> (usize,String) {
    (s.len(),s)
}

fn calculate_length_reference(s:&String) -> usize { // references do not take ownership (borrowing) - references are immutable by default, you can set it to mutable, but you can borrow mutable value only once in a scope
    s.len()
}

// fn returns_reference() -> &'static String {
//     String::from("hello") // string is only in scope of this function, so rust will drop it when function finishes (reference pointing to invalid memory) we have to use lifetime
// }