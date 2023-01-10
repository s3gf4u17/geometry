// // PART 2 
// use std::io;
// use rand::Rng;
// use colored::*;

fn main() {
    // // PART 2
    // println!("Guess the number!");
    // let secret = rand::thread_rng().gen_range(1, 101);
    // loop {
    //     println!("Please input your guess:");
    //     let mut guess = String::new();
    //     io::stdin().read_line(&mut guess).expect("Failed to read line");
    //     let guess: u32 = match guess.trim().parse() {
    //         Ok(num)=>num,
    //         Err(_)=>continue,
    //     };
    //     match guess.cmp(&secret) {
    //         std::cmp::Ordering::Less => println!("{}","Too small!".red()),
    //         std::cmp::Ordering::Greater => println!("{}","Too big!".red()),
    //         std::cmp::Ordering::Equal => {
    //             println!("{}","You guessed correctly!".green());
    //             break;
    //         },
    //     }
    // }

    // // PART 3
    // let mut x : i32 = 0; // variables are immutable by default so we need to specify mut
    // println!("{}",x);
    // x=1;
    // println!("{}",x);
    // const PI : f32 = 3.1415926; // const can not be mutable (mut keyword results in an error), we have to specify type, can not be a computed value
    // println!("{}",PI);
    // let x: &str = "six"; // shadowing
    // println!("{}",x); // scalar data types represent single value, compound data types represent a group of values
    // let a = 98_222; // decimal
    // let b = 0xff; // hex
    // let c = 0o77; // octal
    // let d = 0b1111_0000; // binary
    // let e = b'A'; // byte (only u8) // overflow - normally panick, release build - 2s complement wrapping (max+1)=0
    // let f = 2.0; // default floating point type is f64
    // let g : f32 = 1.0;
    // let h = false;
    // let i= 'z'; // unicode character
    // let j = '🐈';
    // println!("{}",j);
    // let mut k : (&str,i32) = ("rust",100_000); // fixed size array of data with different types
    // k.0="rusty";
    // let (mystring,mynumber) = k; // destructurize
    // println!("{} {} {} {}",k.0,k.1,mystring,mynumber);
    // let l : [i32;3] = [100,200,300]; // fixed length array
    // let m : [i32;8] = [0;8]; // array filled with 0s
    // println!("{} {}",l[1],m[7]);
    // let n = increment(10);
    // println!("{}",n);
    // let o = false;
    // let mut p = if o {5} else {6};
    // println!("{}",p);
    // let mut loopreturn = loop {
    //     if p > 5 {
    //         p-=1;
    //     } else if p < 5 {
    //         p+=1;
    //     } else {
    //         break p // we can break with variable (return it)
    //     }
    // };
    // println!("{}",loopreturn);
    // while loopreturn>0{
    //     loopreturn-=1;
    // }
    // println!("{}",loopreturn);
    // for element in l.iter(){ // looping collection
    //     println!("{}",element)
    // }
    // for number in 1..3 { // last number exclusive
    //     println!("{}",number);
    // }
}

/*
    PART 3
    increment function
*/
// fn increment(x:i32) -> i32 {
//     println!("increment function"); // statement
//     x+1 // expression (returns value) - last expression acts as a return
// }