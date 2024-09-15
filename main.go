package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"sync"
)

func runPythonScript(scriptPath string, input string, wg *sync.WaitGroup) {

	defer wg.Done()

	cmd := exec.Command("python", scriptPath, input)
	output, err := cmd.CombinedOutput()

	if err != nil {
		fmt.Printf("Error executing %s: %v\n", scriptPath, err)
	}
	fmt.Printf("Output from %s:\n%s\n", scriptPath, output)
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter query to pass to Python scripts: ")
	input, _ := reader.ReadString('\n')
	input = input[:len(input)-1]

	var wg sync.WaitGroup
	wg.Add(7)

	go runPythonScript("script1.py", input, &wg)
	go runPythonScript("script2.py", input, &wg)
	go runPythonScript("script3.py", input, &wg)
	go runPythonScript("script4.py", input, &wg)
	go runPythonScript("script5.py", input, &wg)
	go runPythonScript("script6.py", input, &wg)
	go runPythonScript("main.py", input, &wg)

	wg.Wait()
	fmt.Println("Both scripts executed successfully.")
}
