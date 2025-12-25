
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
)

type AtmosData struct {
	Altitude float64 `json:"altitude"`
	Density  float64 `json:"density"`
}

func main() {
	// Absolute path to the data file
	dataPath := "/data/data/com.termux/files/home/Atmos/Atmos/Atmos/data.json"

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
			if d.Density < 0.5 {
				fmt.Printf("⚠️  Alert: Low Density (%.4f) detected at %.0fm\n", d.Density, d.Altitude)
			}
		}
	}
	fmt.Println("✅ Scan Complete.")
}

