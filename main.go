// main.go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os/exec"
	"sync"
	"time"
)

// Sequential function to handle sequential execution
func runSequentialPythonScript(scriptPath string, input string, results *[]string) {
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

func handleSequential(w http.ResponseWriter, r *http.Request) {
	input := r.URL.Query().Get("input")

	var results []string
	start := time.Now()

	runSequentialPythonScript("py1.py", input, &results)
	runSequentialPythonScript("py2.py", input, &results)
	runSequentialPythonScript("py3.py", input, &results)
	runSequentialPythonScript("py4.py", input, &results)
	runSequentialPythonScript("py5.py", input, &results)
	runSequentialPythonScript("py6.py", input, &results)

	elapsed := time.Since(start)
	results = append(results, fmt.Sprintf("Total execution time: %s\n", elapsed))

	json.NewEncoder(w).Encode(results) // Send JSON response
}

func sequential() {
	http.HandleFunc("/run-sequential", handleSequential)
	fmt.Println("Sequential server is running on http://localhost:8082")
	http.ListenAndServe(":8082", nil)
}

// Multithreaded function to handle concurrent execution
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

func main() {
	go sequential() // Start the sequential server in a goroutine
	multithreaded() // Start the multithreaded server
}
