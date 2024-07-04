package main

var a = "G"
var b = "G"

func vs() {
	println()
	n()
	m()
	n()
}

func n() {
	println(a, b)
}

func m() {
	a := "O"
	b = "O"
	println(a, b)
}
