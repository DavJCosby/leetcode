use std::cmp::Ordering;

pub fn my_sqrt(x: i32) -> i32 {
    let mut low = 0;
    let mut high = ((x / 2) + 1).min(46341); // 46341 is the sqrt of the highest possible i32 representation
    let x = x as u64;

    if x == 1 {
        return 1;
    }

    loop {
        if high - low == 1 {
            return low;
        }

        let mid = (low + high) / 2;

        match x.cmp(&(mid as u64 * mid as u64)) {
            Ordering::Less => {
                high = mid;
            }
            Ordering::Equal => {
                return mid;
            }
            Ordering::Greater => {
                low = mid;
            }
        }
    }
}

fn main() {
    println!("{}", my_sqrt(49));
}
