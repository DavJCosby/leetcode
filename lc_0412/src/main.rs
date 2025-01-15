use std::vec::Vec;

fn fizz_buzz(n: i32) -> Vec<String> {
    (0..=n)
        .map(|i| {
            let divisible_by_3 = i % 3 == 0;
            let divisible_by_5 = i % 5 == 0;

            match (divisible_by_3, divisible_by_5) {
                (true, true) => String::from("FizzBuzz"),
                (true, false) => String::from("Fizz"),
                (false, true) => String::from("Buzz"),
                (false, false) => format!("{}", i),
            }
        })
        .collect()
}

fn main() {
    println!("{:?}", fizz_buzz(36));
}
