use std::io;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret = rand::thread_rng().gen_range(1, 101);

    // println!("The secret number is {}",secret);

    loop {

        println!("Please input your guess:");

        let mut guess = String::new();

        io::stdin().read_line(&mut guess).expect("Failed to read line");

        // variable shadowing
        let guess: u32 = match guess.trim().parse() {
            Ok(num)=>num,
            Err(_)=>continue,
        };

        // println!("You guessed {}",guess);

        match guess.cmp(&secret) {
            std::cmp::Ordering::Less => println!("Too small!"),
            std::cmp::Ordering::Greater => println!("Too big!"),
            std::cmp::Ordering::Equal => {
                println!("You guessed correctly!");
                break;
            },
        }

    }
}