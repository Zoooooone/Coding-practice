package main

var s string

func fcf() {
	s = "G"
	print(s)
	f1()
}

func f1() {
	s := "O"
	print(s)
	f2()
}

func f2() {
	print(s)
}
