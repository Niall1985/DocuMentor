// // package main

// // import (
// // 	"encoding/json"
// // 	"fmt"
// // 	"net/http"
// // 	"os/exec"
// // 	"sync"
// // 	"time"
// // )

// // // CORS middleware
// // func corsMiddleware(next http.Handler) http.Handler {
// // 	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
// // 		w.Header().Set("Access-Control-Allow-Origin", "http://localhost:5173")
// // 		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
// // 		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

// // 		// Handle preflight requests
// // 		if r.Method == http.MethodOptions {
// // 			w.WriteHeader(http.StatusOK)
// // 			return
// // 		}

// // 		next.ServeHTTP(w, r)
// // 	})
// // }

// // // Result struct to capture JSON output
// // type Result struct {
// // 	Result string `json:"result"`
// // }

// // // Sequential function to handle sequential execution
// // func runSequentialPythonScript(scriptPath string, input string, results *[]Result) {
// // 	start := time.Now()

// // 	cmd := exec.Command("python", scriptPath, input)
// // 	output, err := cmd.CombinedOutput()

// // 	elapsed := time.Since(start)

// // 	if err != nil {
// // 		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
// // 	} else {
// // 		var result Result
// // 		if json.Unmarshal(output, &result) == nil {
// // 			result.Result += fmt.Sprintf("\nTime taken for %s: %s\n", scriptPath, elapsed)
// // 			*results = append(*results, result)
// // 		} else {
// // 			fmt.Printf("Failed to parse JSON output from %s: %s\n", scriptPath, string(output))
// // 		}
// // 	}
// // }

// // func handleSequential(w http.ResponseWriter, r *http.Request) {
// // 	input := r.URL.Query().Get("input")

// // 	fmt.Printf("Sequential handler received input: %s\n", input)

// // 	var results []Result
// // 	start := time.Now()

// // 	// Run each Python script sequentially
// // 	runSequentialPythonScript("py1.py", input, &results)
// // 	runSequentialPythonScript("py2.py", input, &results)
// // 	runSequentialPythonScript("py3.py", input, &results)
// // 	runSequentialPythonScript("py4.py", input, &results)
// // 	runSequentialPythonScript("py5.py", input, &results)
// // 	runSequentialPythonScript("py6.py", input, &results)

// // 	elapsed := time.Since(start)
// // 	results = append(results, Result{Result: fmt.Sprintf("Total execution time: %s\n", elapsed)})

// // 	json.NewEncoder(w).Encode(results)
// // }

// // func sequential() {
// // 	fmt.Println("Initializing sequential server...")
// // 	seqMux := http.NewServeMux()
// // 	seqMux.HandleFunc("/run-sequential", handleSequential)
// // 	err := http.ListenAndServe(":9002", corsMiddleware(seqMux)) // Apply CORS to sequential server
// // 	if err != nil {
// // 		fmt.Printf("Failed to start sequential server: %v\n", err)
// // 	}
// // }

// // // Multithreaded function to handle concurrent execution
// // func runPythonScript(scriptPath string, input string, wg *sync.WaitGroup, results *[]Result) {
// // 	defer wg.Done()

// // 	start := time.Now()

// // 	cmd := exec.Command("python", scriptPath, input)
// // 	output, err := cmd.CombinedOutput()

// // 	elapsed := time.Since(start)

// // 	if err != nil {
// // 		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
// // 	} else {
// // 		var result Result
// // 		if json.Unmarshal(output, &result) == nil {
// // 			result.Result += fmt.Sprintf("\nTime taken for %s: %s\n", scriptPath, elapsed)
// // 			*results = append(*results, result)
// // 		} else {
// // 			fmt.Printf("Failed to parse JSON output from %s: %s\n", scriptPath, string(output))
// // 		}
// // 	}
// // }

// // func handleMultithreaded(w http.ResponseWriter, r *http.Request) {
// // 	input := r.URL.Query().Get("input")
// // 	fmt.Printf("Multithreaded handler received input: %s\n", input)

// // 	var wg sync.WaitGroup
// // 	wg.Add(6)
// // 	var results []Result

// // 	start := time.Now()

// // 	// Run scripts concurrently
// // 	go runPythonScript("py1.py", input, &wg, &results)
// // 	go runPythonScript("py2.py", input, &wg, &results)
// // 	go runPythonScript("py3.py", input, &wg, &results)
// // 	go runPythonScript("py4.py", input, &wg, &results)
// // 	go runPythonScript("py5.py", input, &wg, &results)
// // 	go runPythonScript("py6.py", input, &wg, &results)

// // 	wg.Wait()
// // 	elapsed := time.Since(start)

// // 	// Add total time
// // 	results = append(results, Result{Result: fmt.Sprintf("Total execution time: %s\n", elapsed)})
// // 	// json.NewEncoder(w).Encode(results)
// // 	fmt.Printf("%s", results)

// // 	fmt.Printf("Received request for multithreaded execution at: http://localhost:9001/run-multithreaded?input=%s\n", input)
// // }

// // func multithreaded() {
// // 	fmt.Println("Initializing multithreaded server...")
// // 	mtMux := http.NewServeMux()
// // 	mtMux.HandleFunc("/run-multithreaded", handleMultithreaded)
// // 	err := http.ListenAndServe(":9001", corsMiddleware(mtMux)) // Apply CORS to multithreaded server
// // 	if err != nil {
// // 		fmt.Printf("Failed to start multithreaded server: %v\n", err)
// // 	}
// // }

// // func main() {
// // 	// Start sequential and multithreaded servers
// // 	go sequential()
// // 	go multithreaded()

// // 	// Serve static files on main server (port 9000)
// // 	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./frontend/src/assets"))))

// // 	fmt.Println("Main server running on http://localhost:9000")
// // 	err := http.ListenAndServe(":9000", corsMiddleware(http.DefaultServeMux))
// // 	if err != nil {
// // 		fmt.Printf("Failed to start main server: %v\n", err)
// // 	}
// // }

// package main

// import (
// 	"encoding/json"
// 	"fmt"
// 	"net/http"
// 	"os/exec"
// 	"sync"
// 	"time"
// )

// // CORS middleware
// func corsMiddleware(next http.Handler) http.Handler {
// 	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
// 		w.Header().Set("Access-Control-Allow-Origin", "http://localhost:5173")
// 		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
// 		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

// 		// Handle preflight requests
// 		if r.Method == http.MethodOptions {
// 			w.WriteHeader(http.StatusOK)
// 			return
// 		}

// 		next.ServeHTTP(w, r)
// 	})
// }

// // Result struct to capture JSON output
// type Result struct {
// 	Result string `json:"result"`
// }

// // Function to run Python scripts sequentially
// func runSequentialPythonScript(scriptPath string, input string, results *[]Result) {
// 	start := time.Now()

// 	cmd := exec.Command("python", scriptPath, input)
// 	output, err := cmd.CombinedOutput()

// 	elapsed := time.Since(start)

// 	if err != nil {
// 		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
// 	} else {
// 		var result Result
// 		if json.Unmarshal(output, &result) == nil {
// 			result.Result += fmt.Sprintf("\nTime taken for %s: %s\n", scriptPath, elapsed)
// 			*results = append(*results, result)
// 		} else {
// 			fmt.Printf("Failed to parse JSON output from %s: %s\n", scriptPath, string(output))
// 		}
// 	}
// }

// // Handler for sequential execution
// func handleSequential(w http.ResponseWriter, r *http.Request) {
// 	input := r.URL.Query().Get("input")

// 	fmt.Printf("Sequential handler received input: %s\n", input)

// 	var results []Result
// 	start := time.Now()

// 	// Run each Python script sequentially
// 	for i := 1; i <= 6; i++ {
// 		runSequentialPythonScript(fmt.Sprintf("py%d.py", i), input, &results)
// 	}

// 	elapsed := time.Since(start)
// 	results = append(results, Result{Result: fmt.Sprintf("Total execution time: %s\n", elapsed)})

// 	w.Header().Set("Content-Type", "application/json")
// 	json.NewEncoder(w).Encode(results)
// }

// // Function to run Python scripts concurrently
// func runPythonScript(scriptPath string, input string, wg *sync.WaitGroup, results *[]Result) {
// 	defer wg.Done()

// 	start := time.Now()

// 	cmd := exec.Command("python", scriptPath, input)
// 	output, err := cmd.CombinedOutput()

// 	elapsed := time.Since(start)

// 	if err != nil {
// 		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
// 	} else {
// 		var result Result
// 		if json.Unmarshal(output, &result) == nil {
// 			result.Result += fmt.Sprintf("\nTime taken for %s: %s\n", scriptPath, elapsed)
// 			*results = append(*results, result)
// 		} else {
// 			fmt.Printf("Failed to parse JSON output from %s: %s\n", scriptPath, string(output))
// 		}
// 	}
// }

// // Handler for multithreaded execution
// func handleMultithreaded(w http.ResponseWriter, r *http.Request) {
// 	input := r.URL.Query().Get("input")
// 	fmt.Printf("Multithreaded handler received input: %s\n", input)

// 	var wg sync.WaitGroup
// 	var results []Result

// 	start := time.Now()

// 	// Run scripts concurrently
// 	for i := 1; i <= 6; i++ {
// 		wg.Add(1)
// 		go runPythonScript(fmt.Sprintf("py%d.py", i), input, &wg, &results)
// 	}

// 	wg.Wait()
// 	elapsed := time.Since(start)

// 	// Add total execution time
// 	results = append(results, Result{Result: fmt.Sprintf("Total execution time: %s\n", elapsed)})

// 	w.Header().Set("Content-Type", "application/json")
// 	json.NewEncoder(w).Encode(results)
// }

// // Start the sequential server
// func sequential() {
// 	fmt.Println("Initializing sequential server...")
// 	seqMux := http.NewServeMux()
// 	seqMux.HandleFunc("/run-sequential", handleSequential)
// 	err := http.ListenAndServe(":9002", corsMiddleware(seqMux)) // Apply CORS to sequential server
// 	if err != nil {
// 		fmt.Printf("Failed to start sequential server: %v\n", err)
// 	}
// }

// // Start the multithreaded server
// func multithreaded() {
// 	fmt.Println("Initializing multithreaded server...")
// 	mtMux := http.NewServeMux()
// 	mtMux.HandleFunc("/run-multithreaded", handleMultithreaded)
// 	err := http.ListenAndServe(":9001", corsMiddleware(mtMux)) // Apply CORS to multithreaded server
// 	if err != nil {
// 		fmt.Printf("Failed to start multithreaded server: %v\n", err)
// 	}
// }

// func main() {
// 	// Start sequential and multithreaded servers
// 	go sequential()
// 	go multithreaded()

// 	// Serve static files on main server (port 9000)
// 	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./frontend/src/assets"))))

// 	fmt.Println("Main server running on http://localhost:9000")
// 	err := http.ListenAndServe(":9000", corsMiddleware(http.DefaultServeMux))
// 	if err != nil {
// 		fmt.Printf("Failed to start main server: %v\n", err)
// 	}
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

// Chunk struct to capture individual chunks of JSON output
type Chunk struct {
	Chunk           string   `json:"chunk"`
	SimilarityScore *float64 `json:"similarity_score"` // Use pointer to handle null values
	Source          string   `json:"source"`
}

// Output struct to capture the full JSON structure
type Output struct {
	TopRelevantChunks     []Chunk `json:"top_relevant_chunks"`
	ProcessingTimeSeconds float64 `json:"processing_time_seconds"`
}

// Result struct to capture overall result and output
type Result struct {
	Result  string `json:"result"`
	Output  Output `json:"output,omitempty"`  // Use omitempty for optional field
	Message string `json:"message,omitempty"` // For error messages
}

// Function to run Python scripts sequentially
func runSequentialPythonScript(scriptPath string, input string, results *[]Result) {
	start := time.Now()

	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()

	elapsed := time.Since(start)

	if err != nil {
		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
		*results = append(*results, Result{Result: fmt.Sprintf("Error executing %s: %v", scriptPath, err)})
		return
	}

	var result Output
	if err := json.Unmarshal(output, &result); err != nil {
		// If unmarshalling fails, log the output and add a specific error message
		fmt.Printf("Failed to parse JSON output from %s: %s\n", scriptPath, string(output))
		*results = append(*results, Result{Result: fmt.Sprintf("Failed to parse JSON output from %s: %s", scriptPath, string(output))})
		return
	}

	// If successful, add execution time to the result
	result.ProcessingTimeSeconds = elapsed.Seconds()
	*results = append(*results, Result{Result: "Success", Output: result})
}

// Handler for sequential execution
func handleSequential(w http.ResponseWriter, r *http.Request) {
	input := r.URL.Query().Get("input")

	fmt.Printf("Sequential handler received input: %s\n", input)

	var results []Result
	start := time.Now()

	// Run each Python script sequentially
	for i := 1; i <= 6; i++ {
		runSequentialPythonScript(fmt.Sprintf("py%d.py", i), input, &results)
	}

	elapsed := time.Since(start)
	results = append(results, Result{Result: fmt.Sprintf("Total execution time: %s\n", elapsed)})

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(results)
}

// Function to run Python scripts concurrently
func runPythonScript(scriptPath string, input string, wg *sync.WaitGroup, results *[]Result) {
	defer wg.Done()

	start := time.Now()

	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()

	elapsed := time.Since(start)

	if err != nil {
		fmt.Printf("Error executing %s: %v\nOutput: %s\n", scriptPath, err, string(output))
		*results = append(*results, Result{Result: fmt.Sprintf("Error executing %s: %v", scriptPath, err)})
		return
	}

	var result Output
	if err := json.Unmarshal(output, &result); err != nil {
		// If unmarshalling fails, log the output and add a specific error message
		fmt.Printf("Failed to parse JSON output from %s: %s\n", scriptPath, string(output))
		*results = append(*results, Result{Result: fmt.Sprintf("Failed to parse JSON output from %s: %s", scriptPath, string(output))})
		return
	}

	// If successful, add execution time to the result
	result.ProcessingTimeSeconds = elapsed.Seconds()
	*results = append(*results, Result{Result: "Success", Output: result})
}

// Handler for multithreaded execution
func handleMultithreaded(w http.ResponseWriter, r *http.Request) {
	input := r.URL.Query().Get("input")
	fmt.Printf("Multithreaded handler received input: %s\n", input)

	var wg sync.WaitGroup
	var results []Result

	start := time.Now()

	// Run scripts concurrently
	for i := 1; i <= 6; i++ {
		wg.Add(1)
		go runPythonScript(fmt.Sprintf("py%d.py", i), input, &wg, &results)
	}

	wg.Wait()
	elapsed := time.Since(start)

	// Add total execution time
	results = append(results, Result{Result: fmt.Sprintf("Total execution time: %s\n", elapsed)})

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(results)
}

// Start the sequential server
func sequential() {
	fmt.Println("Initializing sequential server...")
	seqMux := http.NewServeMux()
	seqMux.HandleFunc("/run-sequential", handleSequential)
	err := http.ListenAndServe(":9002", corsMiddleware(seqMux)) // Apply CORS to sequential server
	if err != nil {
		fmt.Printf("Failed to start sequential server: %v\n", err)
	}
}

// Start the multithreaded server
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
