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

package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os/exec"
	"sync"
	"time"
)

func runPythonScript(scriptPath string, input string, wg *sync.WaitGroup, results *[]string) {
	defer wg.Done()

	start := time.Now()

	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()

	elapsed := time.Since(start)

	if err != nil {
		fmt.Printf("Error executing %s: %v\n", scriptPath, err)
	}
	result := fmt.Sprintf("Output from %s:\n%s\nTime taken for %s: %s\n", scriptPath, output, scriptPath, elapsed)
	*results = append(*results, result)
}

func handleMultithreaded(w http.ResponseWriter, r *http.Request) {
	var wg sync.WaitGroup
	input := r.URL.Query().Get("input")

	wg.Add(6)
	var results []string

	start := time.Now()

	// Run scripts concurrently
	go runPythonScript("py1.py", input, &wg, &results)
	go runPythonScript("py2.py", input, &wg, &results)
	go runPythonScript("py3.py", input, &wg, &results)
	go runPythonScript("py4.py", input, &wg, &results)
	go runPythonScript("py5.py", input, &wg, &results)
	go runPythonScript("py6.py", input, &wg, &results)

	wg.Wait()
	elapsed := time.Since(start)

	// Add total time
	results = append(results, fmt.Sprintf("Total execution time: %s\n", elapsed))
	json.NewEncoder(w).Encode(results) // Send JSON response
}

func multithreaded() {
	http.HandleFunc("/run-multithreaded", handleMultithreaded)
	fmt.Println("Multithreaded server is running on http://localhost:8081")
	http.ListenAndServe(":8081", nil)
}
