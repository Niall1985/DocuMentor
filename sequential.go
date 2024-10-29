// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"os/exec"
// 	"time"
// )

// func runSequentialPythonScript(scriptPath string, input string) {
// 	start := time.Now()

// 	cmd := exec.Command("python", scriptPath, input)
// 	output, err := cmd.CombinedOutput()

// 	elapsed := time.Since(start)

// 	if err != nil {
// 		fmt.Printf("Error executing %s: %v\n", scriptPath, err)
// 	}
// 	fmt.Printf("Output from %s:\n%s\n", scriptPath, output)
// 	fmt.Printf("Time taken for %s: %s\n", scriptPath, elapsed)
// }

// func sequntial() {
// 	reader := bufio.NewReader(os.Stdin)

// 	fmt.Print("Enter query to pass to Python scripts: ")
// 	input, _ := reader.ReadString('\n')
// 	input = input[:len(input)-1]

// 	start := time.Now()

// 	runSequentialPythonScript("py1.py", input)
// 	runSequentialPythonScript("py2.py", input)
// 	runSequentialPythonScript("py3.py", input)
// 	runSequentialPythonScript("py4.py", input)
// 	runSequentialPythonScript("py5.py", input)
// 	runSequentialPythonScript("py6.py", input)

// 	elapsed := time.Since(start)

// 	fmt.Println("All scripts executed successfully.")
// 	fmt.Printf("Total execution time: %s\n", elapsed)
// }

package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os/exec"
	"time"
)

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
