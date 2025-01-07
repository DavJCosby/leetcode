fn sum_of_digits_sq(n: i32) -> i32 {
    let mut n = n;
    let mut sum = 0;

    while n > 0 {
        let d = n % 10;
        sum += d * d;
        n /= 10;
    }

    return sum;
}

pub fn is_happy(n: i32) -> bool {
    let sum = sum_of_digits_sq(n);

    return match sum {
        1 => true,
        4 => false, // 4 is in our infite sequence
        _ => is_happy(sum)
    }
}

fn main() {
    println!("{}", is_happy(19));
}
