// collections

use unicode_segmentation::UnicodeSegmentation;
use std::collections::HashMap;

// normal arrays and tuples are stored on the stack (cant be resized)

fn main() {
    // vectors <- have to be mutable if we want to change
    let mut v1 : Vec<i32> = Vec::new(); // initialize 1 using associated function
    v1.push(1);
    let mut v2 = vec![1,2,3]; // initialize 2 using vec macro
    let first = &v2[0]; // error prone if index out of boundaries
    match v2.get(1) {
        Some(x)=>println!("second item: {}",x),
        None=>println!("index out of boundaries")
    }; // uses Option enum
    println!("{:?} {:?} {}",v1,v2,first);
    for i in &mut v2 { // takes mutable reference to all items in v2 vector
        *i += 1;
    }
    for i in &v2 { // takes immutable reference to all items in v2 vector
        println!("{}",i);
    }

    // strings <- collection of utf8 encoded bytes
    let s1 = String::new();
    let s2 = "initial string"; // string slice
    let s3 = s2.to_string();
    let mut s4 = String::from("initial contents");
    s4.push_str(" changed");
    s4.push('!');
    println!("{}",s4);
    let s1 = s1 + &s4;
    println!("{}",s1);
    let s4 = format!("{} {}",s1,s2); // format macro does not take ownership
    println!("{}",s4);

    // unicode
    // bytes -> chars -> clusters (these are the actual letters)
    // clusters are used to store data other than just english alphabet

    for b in "涅槃".bytes() {
        println!("{}",b);
    }
    for c in "涅槃".chars() {
        println!("{}",c);
    }
    for s in "涅槃".graphemes(true) {
        println!("{}",s);
    }

    // hash maps (key-value) pairs
    let blue = String::from("Blue");
    let yellow = String::from("Yellow");

    let mut scores : HashMap<String,i32> = HashMap::new();
    scores.insert(blue,10); // moves ownership of blue
    scores.insert(yellow,30);

    let team_name = String::from("Green");
    let score = scores.get(&team_name); // score is an option (key can not exist)

    for (key,value) in &scores {
        println!("{}: {}",key,value);
    }

    let mut scores2 : HashMap<String,i32> = HashMap::new();
    scores2.insert(String::from("Blue"),20);
    scores2.insert(String::from("Blue"),40); // overwrites value
    scores2.entry(String::from("Yellow")).or_insert(30);
    scores2.entry(String::from("Yellow")).or_insert(40); // does not overwrite value
    for (key,value) in &scores2 {
        println!("{}: {}",key,value);
    }
}