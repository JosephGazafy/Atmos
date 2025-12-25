package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strconv"
)

type AtmosData struct {
	Timestamp string  `json:"timestamp"`
	Altitude  float64 `json:"altitude"`
	Density   float64 `json:"density"`
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run search.go [DENSITY_THRESHOLD]")
		return
	}

	threshold, _ := strconv.ParseFloat(os.Args[1], 64)
	dataPath := "/data/data/com.termux/files/home/Atmos/Atmos/Atmos/data.json"

	file, _ := os.Open(dataPath)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Printf("🔍 Searching for Density < %.4f...\n", threshold)

	for scanner.Scan() {
		var d AtmosData
		json.Unmarshal(scanner.Bytes(), &d)
		if d.Density < threshold {
			fmt.Printf("📍 Match: Alt %.0fm | Density %.4f | %s\n", d.Altitude, d.Density, d.Timestamp)
		}
	}
}


