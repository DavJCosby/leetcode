// Submitted 2024.8.10
// O(N)

package main

import (
	"strconv"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	asString := strconv.Itoa(x)
	length := len(asString)
	for i := 0; i < length/2; i++ {
		if asString[i] != asString[length-i-1] {
			return false
		}
	}

	return true
}

func main() {
	if !isPalindrome(121) {
		println("failed case 1")
	}

	if isPalindrome(-121) {
		println("failed case 2")
	}

	if isPalindrome(10) {
		println("failed case 3")
	}
}
