package main

import "fmt"

func main() {
	M := make(map[int]string)
	M[0] = "H"
	M[1] = "e"
	M[2] = "l"
	M[3] = "l"
	M[4] = "o"

	for i := 0; i < 5; i++ {
		fmt.Print(M[i])
	}
}
