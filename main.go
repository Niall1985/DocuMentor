package main

import (
	"fmt"
	"net/http"
	"os/exec"
	"runtime"
	"sync"
	"time"
)

func corsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "http://localhost:5173")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")

		if r.Method == http.MethodOptions {
			w.WriteHeader(http.StatusOK)
			return
		}

		next.ServeHTTP(w, r)
	})
}

func getResourceUtilization() string {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)

	return fmt.Sprintf("Memory Usage: Alloc = %v MiB, TotalAlloc = %v MiB, Sys = %v MiB",
		memStats.Alloc/1024/1024, memStats.TotalAlloc/1024/1024, memStats.Sys/1024/1024)
}

func runPythonScript(scriptPath string, input string) (string, error) {
	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()
	if err != nil {
		return fmt.Sprintf("Error executing %s: %s", scriptPath, string(output)), err
	}
	return string(output), nil
}

func handleSequential(w http.ResponseWriter, r *http.Request) {
	input := r.URL.Query().Get("input")
	fmt.Printf("Sequential handler received input: %s\n", input)

	var results []string
	start := time.Now()

	for i := 1; i <= 6; i++ {
		scriptPath := fmt.Sprintf("py%d.py", i)
		result, err := runPythonScript(scriptPath, input)
		if err != nil {
			results = append(results, result)
		} else {
			results = append(results, result)
			fmt.Printf("Output from %s:\n%s\n", scriptPath, result)
		}
	}

	elapsed := time.Since(start)
	results = append(results, fmt.Sprintf("Total execution time: %s\n", elapsed))

	resourceStats := getResourceUtilization()
	results = append(results, resourceStats)
	fmt.Printf("Sequential Resource Utilization: %s\n", resourceStats)

	w.Header().Set("Content-Type", "text/plain")
	for _, result := range results {
		fmt.Fprintln(w, result)
	}
}

func sequential() {
	fmt.Println("Initializing sequential server...")
	seqMux := http.NewServeMux()
	seqMux.HandleFunc("/run-sequential", handleSequential)
	err := http.ListenAndServe(":9002", corsMiddleware(seqMux))
	if err != nil {
		fmt.Printf("Failed to start sequential server: %v\n", err)
	}
}

func handleMultithreaded(w http.ResponseWriter, r *http.Request) {
	input := r.URL.Query().Get("input")
	fmt.Printf("Multithreaded handler received input: %s\n", input)

	var wg sync.WaitGroup
	var results []string
	var mu sync.Mutex

	start := time.Now()

	wg.Add(6)
	for i := 1; i <= 6; i++ {
		scriptPath := fmt.Sprintf("py%d.py", i)
		go func(path string) {
			defer wg.Done()
			output, err := runPythonScript(path, input)

			mu.Lock()
			defer mu.Unlock()
			if err != nil {
				results = append(results, fmt.Sprintf("Error executing %s: %s", path, output))
			} else {
				results = append(results, output)
			}
		}(scriptPath)
	}

	wg.Wait()
	elapsed := time.Since(start)

	results = append(results, fmt.Sprintf("Total execution time: %s\n", elapsed))
	resourceStats := getResourceUtilization()
	results = append(results, resourceStats)

	fmt.Printf("Multithreaded Resource Utilization: %s\n", resourceStats)

	w.Header().Set("Content-Type", "text/plain")
	for _, result := range results {
		fmt.Fprintln(w, result)
	}
}

func multithreaded() {
	fmt.Println("Initializing multithreaded server...")
	mtMux := http.NewServeMux()
	mtMux.HandleFunc("/run-multithreaded", handleMultithreaded)

	err := http.ListenAndServe(":9001", corsMiddleware(mtMux))
	if err != nil {
		fmt.Printf("Failed to start multithreaded server: %v\n", err)
	}
}

func main() {

	go sequential()
	go multithreaded()

	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./frontend/src/assets"))))

	fmt.Println("Main server running on http://localhost:9000")
	err := http.ListenAndServe(":9000", corsMiddleware(http.DefaultServeMux))
	if err != nil {
		fmt.Printf("Failed to start main server: %v\n", err)
	}
}
