mod front_of_the_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
        pub fn seat_at_table() {}
    }

    mod serving {
        fn take_order() {}
        fn serve_order() {}
        fn take_payment() {}
    }
}

use crate::front_of_the_house::hosting;

pub fn eat_at_restaurant() {
    // absolute path
    // crate::front_of_the_house::hosting::add_to_waitlist();
    hosting::add_to_waitlist();

    // relative path
    front_of_the_house::hosting::seat_at_table();
}

// we can make structs public but even then fields in the struct are private, we need to use pub keyword on them explicitly