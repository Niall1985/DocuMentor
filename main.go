// // with goroutines
// package main

// import (
// 	"fmt"
// 	"os/exec"
// 	"sync"
// 	"time"
// )

// func runPythonScript(scriptPath string, input string, wg *sync.WaitGroup) {
// 	defer wg.Done()

// 	start := time.Now() // Start time for each script execution

// 	cmd := exec.Command("python", scriptPath, input)
// 	output, err := cmd.CombinedOutput()

// 	elapsed := time.Since(start) // Time taken for this script execution

// 	if err != nil {
// 		fmt.Printf("Error executing %s: %v\n", scriptPath, err)
// 	}
// 	fmt.Printf("Output from %s:\n%s\n", scriptPath, output)
// 	fmt.Printf("Time taken for %s: %s\n", scriptPath, elapsed)
// }

// func main() {
// 	// reader := bufio.NewReader(os.Stdin)

// 	// fmt.Print("Enter query to pass to Python scripts: ")
// 	input := "Advantages of Using Computer Application in Agriculture"
// 	// input, _ := reader.ReadString('\n')
// 	// input = input[:len(input)-1]

// 	var wg sync.WaitGroup
// 	wg.Add(6)

// 	start := time.Now() // Start time for all goroutines

// 	go runPythonScript("py1.py", input, &wg)
// 	go runPythonScript("py2.py", input, &wg)
// 	go runPythonScript("py3.py", input, &wg)
// 	go runPythonScript("py4.py", input, &wg)
// 	go runPythonScript("py5.py", input, &wg)
// 	go runPythonScript("py6.py", input, &wg)
// 	// go runPythonScript("main.py", input, &wg)

// 	wg.Wait() // Wait for all goroutines to finish

// 	elapsed := time.Since(start) // Time taken for all goroutines

// 	fmt.Printf("All scripts executed successfully.\n")
// 	fmt.Printf("Total execution time: %s\n", elapsed)
// }

// // // without go routines
package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"time"
)

func runPythonScript(scriptPath string, input string) {
	start := time.Now()

	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()

	elapsed := time.Since(start)

	if err != nil {
		fmt.Printf("Error executing %s: %v\n", scriptPath, err)
	}
	fmt.Printf("Output from %s:\n%s\n", scriptPath, output)
	fmt.Printf("Time taken for %s: %s\n", scriptPath, elapsed)
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter query to pass to Python scripts: ")
	input, _ := reader.ReadString('\n')
	input = input[:len(input)-1]

	start := time.Now()

	runPythonScript("py1.py", input)
	runPythonScript("py2.py", input)
	runPythonScript("py3.py", input)
	runPythonScript("py4.py", input)
	runPythonScript("py5.py", input)
	runPythonScript("py6.py", input)
	// runPythonScript("main.py", input)

	elapsed := time.Since(start) // Time taken for all scripts

	fmt.Println("All scripts executed successfully.")
	fmt.Printf("Total execution time: %s\n", elapsed)
}
