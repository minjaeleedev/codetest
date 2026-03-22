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
	isOne := true
	for i, c := range isbn {
		if c == '*' {
			isOne = i%2 == 0
			continue
		}

		val := int(c) - int('0')
		if i%2 == 0 {
			checkSum += val
		} else {
			checkSum += 3 * val
		}
	}

	res := 0
	for val := range 10 {
		if isOne {
			if (checkSum+val)%10 == 0 {
				res = val
			}
		} else {
			if (checkSum+3*val)%10 == 0 {
				res = val
			}
		}
	}

	return res
}

func main() {
	isbn := input()
	res := findISBN(isbn)

	output(res)
}
