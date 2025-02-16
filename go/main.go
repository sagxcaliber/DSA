package main

import "fmt"

const s string = "constant"

func main() {
	fmt.Println("Hello World")
	fmt.Println("sagar")
	fmt.Println(1 + 1)
	fmt.Println(true && true)
	fmt.Println(false || false)
	fmt.Println(!true)
	fmt.Println(7.0 / 3.0)

	/*
		now we learn how to declare new varible
		we need to use var
	*/
	var myName string
	myName = "my first variable"
	// myName = "40"
	println(myName)

	var numberSample int
	numberSample = 10
	println(numberSample)
	easyVar := "hello world!!"
	easyNumbervar := 100
	fmt.Println(easyNumbervar)
	fmt.Println(easyVar)

	// now we will learn constant
	const n = 1000000000
	const d = 3e20 / n
	fmt.Println(n)
	fmt.Println(d)
	fmt.Println(int64(d))
	fmt.Println(s)

	// lets learn for loop
	i := 1
	for i <= 3000 {
		fmt.Println("new for loop", i)
		i += 1
	}
}
