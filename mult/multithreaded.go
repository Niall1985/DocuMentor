// package mult

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

// func multithreaded() {
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

// func mult() {
// 	multithreaded()
// }

