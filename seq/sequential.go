// package seq

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

// func seq() {
// 	sequntial()
// }