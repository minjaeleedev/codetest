package main

import "fmt"

func input() []int {
	var N int
	var S, M, L, XL, XXL, XXXL int
	var T, P int
	fmt.Scanln(&N)
	fmt.Scanln(&S, &M, &L, &XL, &XXL, &XXXL)
	fmt.Scanln(&T, &P)

	return []int{N, S, M, L, XL, XXL, XXXL, T, P}
}

func output(res1 int, res2 int, res3 int) {
	fmt.Println(res1)
	fmt.Println(res2, res3)
}

func getBundleOfShirtsAndPen(values []int) (int, int, int) {
	N := values[0]
	T, P := values[7], values[8]
	shirtsBundle := 0
	for _, v := range values[1:7] {
		if v%T != 0 {
			shirtsBundle += v/T + 1
		} else {
			shirtsBundle += v / T
		}
	}
	penBundle := N / P
	penRemain := N % P
	return shirtsBundle, penBundle, penRemain
}

func main() {
	r1, r2, r3 := getBundleOfShirtsAndPen(input())
	output(r1, r2, r3)
}
