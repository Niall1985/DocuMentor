// package main

// import (
// 	"fmt"
// 	"time"
// )

// func printMessage(message string) {
// 	for i := 0; i < 5; i++ {
// 		fmt.Println(message)
// 		time.Sleep(100 * time.Millisecond)
// 	}
// }

// func main() {
// 	start := time.Now()

// 	go printMessage("Goroutine 1")
// 	go printMessage("Goroutine 2")
// 	go printMessage("Goroutine 3")

// 	time.Sleep(1 * time.Second)

// 	elapsed := time.Since(start)
// 	fmt.Println("Execution Time with Goroutines:", elapsed)
// }

package main

import (
	"fmt"
	"time"
)

func printMessage(message string) {
	for i := 0; i < 5; i++ {
		fmt.Println(message)
		time.Sleep(100 * time.Millisecond) // Simulate some work
	}
}

func main() {
	start := time.Now() // Start timer

	// Call the functions sequentially
	printMessage("Function 1")
	printMessage("Function 2")
	printMessage("Function 3")

	elapsed := time.Since(start) // Measure elapsed time
	fmt.Println("Execution Time without Goroutines:", elapsed)
}
