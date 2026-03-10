package main

import (
	"fmt"
	"strconv"
	"strings"
)

func input() (int, int, int) {
	var a, b, c int
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	fmt.Scanln(&c)
	return a, b, c
}

func output(res1 int, res2 int) {
	fmt.Println(res1)
	fmt.Println(res2)
}

func operateIntString(A int, B int, C int) (int, int) {
	var res1 int = A + B - C
	strs := []string{
		strconv.Itoa(A),
		strconv.Itoa(B)}
	aplusb, _ := strconv.Atoi((strings.Join(strs, "")))
	var res2 int = aplusb - C

	return res1, res2
}

func main() {
	res1, res2 := operateIntString(input())

	output(res1, res2)
}
