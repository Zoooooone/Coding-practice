package main

import "fmt"

func literal() {
	s := "hello world"
	fmt.Print("aoivboidnoa \n")
	fmt.Println(`aobviuqeoqe \n`)
	fmt.Println(s[3], string(s[3]), len(s))
	fmt.Printf("%c \n", s[3])
	fmt.Println(s[3] == 'l')
}
