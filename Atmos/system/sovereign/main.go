package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
)

type AtmosData struct {
	Altitude float64 `json:"altitude"`
	Density  float64 `json:"density"`
}

func main() {
// Replace the previous path logic with this finer approach
cwd, _ := os.Getwd()
// We check multiple possible locations to ensure interoperability
locations := []string{
    filepath.Join(cwd, "data.json"),           // Root
    filepath.Join(cwd, "../../data.json"),    // Nested depth 2
    filepath.Join(cwd, "../../../data.json"), // Nested depth 3
}

var file *os.File
var err error
for _, loc := range locations {
    file, err = os.Open(loc)
    if err == nil {
        fmt.Printf("✅ Data Link Established: %s\n", loc)
        break
    }
}

if err != nil {
    fmt.Println("❌ Data Link Broken: Please run 'atmos -a 1000 -j' first.")
    return
}






