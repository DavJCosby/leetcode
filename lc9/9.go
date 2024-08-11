package main

import (
	"strconv"
)

func reverse(s string) string {
	length := len(s)
	reversedChars := make([]byte, length)

	for i := 0; i < length; i++ {
		reversedChars[length-i-1] = s[i]
	}

	return string(reversedChars)
}

func isPalindrome(x int) bool {
	asString := strconv.Itoa(x)
	strReversed := reverse(asString)
	return asString == strReversed
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
