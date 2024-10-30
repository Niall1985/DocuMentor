package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os/exec"
	"sync"
	"time"
)

// CORS middleware
func corsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "http://localhost:5173")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

		// Handle preflight requests
		if r.Method == http.MethodOptions {
			w.WriteHeader(http.StatusOK)
			return
		}

		next.ServeHTTP(w, r)
	})
}

// Sequential function to handle sequential execution
func runSequentialPythonScript(scriptPath string, input string, results *[]string) {
	start := time.Now()

	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()

	elapsed := time.Since(start)

	if err != nil {
		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
	} else {
		result := fmt.Sprintf("Output from %s:\n%s\nTime taken for %s: %s\n", scriptPath, string(output), scriptPath, elapsed)
		*results = append(*results, result)
	}
}

func handleSequential(w http.ResponseWriter, r *http.Request) {
	input := r.URL.Query().Get("input")

	fmt.Printf("Sequential handler received input: %s\n", input)

	var results []string
	start := time.Now()

	// Run each Python script sequentially
	runSequentialPythonScript("py1.py", input, &results)
	runSequentialPythonScript("py2.py", input, &results)
	runSequentialPythonScript("py3.py", input, &results)
	runSequentialPythonScript("py4.py", input, &results)
	runSequentialPythonScript("py5.py", input, &results)
	runSequentialPythonScript("py6.py", input, &results)

	elapsed := time.Since(start)
	results = append(results, fmt.Sprintf("Total execution time: %s\n", elapsed))

	json.NewEncoder(w).Encode(results)
}

func sequential() {
	fmt.Println("Initializing sequential server...")
	seqMux := http.NewServeMux()
	seqMux.HandleFunc("/run-sequential", handleSequential)
	err := http.ListenAndServe(":9002", corsMiddleware(seqMux)) // Apply CORS to sequential server
	if err != nil {
		fmt.Printf("Failed to start sequential server: %v\n", err)
	}
}

// Multithreaded function to handle concurrent execution
func runPythonScript(scriptPath string, input string, wg *sync.WaitGroup, results *[]string) {
	defer wg.Done()

	start := time.Now()

	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()

	elapsed := time.Since(start)

	if err != nil {
		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
	} else {
		result := fmt.Sprintf("Output from %s:\n%s\nTime taken for %s: %s\n", scriptPath, string(output), scriptPath, elapsed)
		*results = append(*results, result)
	}
}

func handleMultithreaded(w http.ResponseWriter, r *http.Request) {
	input := r.URL.Query().Get("input")
	fmt.Printf("Multithreaded handler received input: %s\n", input)

	var wg sync.WaitGroup
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
	json.NewEncoder(w).Encode(results)

	fmt.Printf("Received request for multithreaded execution at: http://localhost:9001/run-multithreaded?input=%s\n", input)
}

func multithreaded() {
	fmt.Println("Initializing multithreaded server...")
	mtMux := http.NewServeMux()
	mtMux.HandleFunc("/run-multithreaded", handleMultithreaded)
	err := http.ListenAndServe(":9001", corsMiddleware(mtMux)) // Apply CORS to multithreaded server
	if err != nil {
		fmt.Printf("Failed to start multithreaded server: %v\n", err)
	}
}

func main() {
	// Start sequential and multithreaded servers
	go sequential()
	go multithreaded()

	// Serve static files on main server (port 9000)
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./frontend/src/assets"))))

	fmt.Println("Main server running on http://localhost:9000")
	err := http.ListenAndServe(":9000", corsMiddleware(http.DefaultServeMux))
	if err != nil {
		fmt.Printf("Failed to start main server: %v\n", err)
	}
}
