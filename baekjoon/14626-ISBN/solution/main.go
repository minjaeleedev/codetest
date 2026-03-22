package main

import (
	"fmt"
)

func input() string {
	var isbn string
	fmt.Scanln(&isbn)
	return isbn
}

func output(res int) {
	fmt.Println(res)
}

func findISBN(isbn string) int {
	checkSum := 0
	weight := 0
	for i, c := range isbn {
		w := 1
		if i%2 == 1 {
			w = 3
		}

		if c == '*' {
			weight = w
			continue
		}

		checkSum += w * int(c-'0')
	}

	remainder := (10 - checkSum%10) % 10
	if weight == 3 {
		// 3의 mod 10 modular inverse은 7 (3*7 = 21 ≡ 1 mod 10)
		return (7 * remainder) % 10
	}
	return remainder
}

func main() {
	isbn := input()
	res := findISBN(isbn)

	output(res)
}
