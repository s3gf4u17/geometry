// // structs

// struct User {
//     username: String,
//     email: String,
//     sign_count: u64,
//     active: bool,
// }

// // tuple struct

// struct Color (i8,i8,i8);
// struct Point (i32,i32,i32);

// fn build_user(email:String,username:String) -> User {
//     User {
//         email,
//         username,
//         sign_count:0,
//         active:true,
//     }
// }

#[derive(Debug)]
struct Rectangle {
    width:u32,
    height:u32,
}

impl Rectangle { // methods
    fn area(&self) -> u32 {
        self.width*self.height
    }
    fn can_contain(&self,other:&Rectangle)->bool {
        (self.width>=other.width&&self.height>=self.height)||(self.width>=other.height&&self.height>=self.width)
    }
}

impl Rectangle {
    fn square(size:u32) -> Rectangle {
        Rectangle{
            width:size,
            height:size
        }
    } // associated function
}

fn main() {
    let rect = Rectangle{width:11,height:7};
    println!("rect: {:#?}\narea: {}",rect,rect.area());
    let rect2 = Rectangle{width:12,height:8};
    println!("can contain: {}",rect.can_contain(&rect2));
    let rect2 = Rectangle{width:6,height:11};
    println!("can contain: {}",rect.can_contain(&rect2));
    let rect2 = Rectangle{width:11,height:7};
    println!("can contain: {}",rect.can_contain(&rect2));
    let rect4 = Rectangle::square(12);
    println!("square: a={} b={}",rect4.width,rect4.height)
    // let mut user1 = User{email:String::from("test@test.test.test"),username:String::from("s3gf4u17"),sign_count:12,active:true};
    // user1.username=String::from("admin");
    // user1.sign_count+=1;
    // user1.active=false;
    // println!("{}",user1.email);

    // let user2 = build_user(String::from("a@b.c"),String::from("bot"));
    // println!("{} {}",user2.email,user2.sign_count);

    // let user3 = User {
    //     email:String::from("user@mail.br"),
    //     username:String::from("user"),
    //     .. user2 // copy user2 values for the rest
    // };
    // println!("{} {}",user3.active,user3.sign_count);
}