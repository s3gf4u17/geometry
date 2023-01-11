// enums
enum IpAddrKind {
    V4,
    V6,
}

enum IpAddrData {
    V4(u8,u8,u8,u8),
}

impl IpAddrData {
    fn print(&self) {
        println!("test");
    }
}

struct IpAddr {
    kind: IpAddrKind,
    address: String
}

enum Message {
    Quit,
    Move {x:i32,y:i32},
    Write(String),
    ChangeColor(i32,i32,i32),
}

// option enum (we have no values but option enum instead)
// enum Option<T> {
//     Some<T>,
//     None,
// } // we can check if the value does not exist
// option enum is implemented by default

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn main() {
    let _four = IpAddrKind::V4;
    let _six = IpAddrKind::V6;

    let localhost = IpAddr{kind:IpAddrKind::V4,address:String::from("127.0.0.1")};
    let localhost = IpAddrData::V4(127,0,0,1);
    localhost.print();

    let some_number = Some(5);
    let some_string = Some("string");
    let absent: Option<i32> = None;

    let x = 5;
    let y : Option<i8> = Some(5);
    // let z = x+y; - compile time error
    let z = x+y.unwrap_or(0); // set default to 0
    println!("{}",z);

    let coin = Coin::Nickel;
    let value =  match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    };
    println!("{}",value);

    let x = increment(Some(5));
    let y = increment(None);
    println!("{:?} {:?}",x,y);
}

fn increment(x:Option<i32>) -> Option<i32> {
    match x {
        // None => None,
        Some(i) => Some(i+1)
        _ => None,
    }
}