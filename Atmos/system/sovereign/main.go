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
	// Use absolute path discovery for Termux interoperability
	cwd, _ := os.Getwd()
	dataPath := filepath.Join(cwd, "../../data.json")

	file, err := os.Open(dataPath)
	if err != nil {
		fmt.Printf("❌ Data Link Broken: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Println("🚀 Scanning Atmos Interoperability Layer...")

	for scanner.Scan() {
		var d AtmosData
		if err := json.Unmarshal(scanner.Bytes(), &d); err == nil {
			if d.Density < 0.5 { // Threshold for "Thin Air"
				fmt.Printf("⚠️  Alert: Low Density (%.4f) detected at %.0fm\n", d.Density, d.Altitude)
			}
		}
	}
}

