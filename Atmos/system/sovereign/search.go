package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strconv"
)

// AtmosData represents the structure of our JSON logs
type AtmosData struct {
	Timestamp string  `json:"timestamp"`
	Altitude  float64 `json:"altitude"`
	Pressure  float64 `json:"pressure"`
	Density   float64 `json:"density"`
}

func main() {
	// 1. Validate Input
	if len(os.Args) < 2 {
		fmt.Println("❌ Usage: make search D=[THRESHOLD]")
		fmt.Println("Example: make search D=0.85")
		return
	}

	threshold, err := strconv.ParseFloat(os.Args[1], 64)
	if err != nil {
		fmt.Println("❌ Error: Threshold must be a valid number.")
		return
	}

	// 2. Define Absolute Paths for Sovereign Stability
	const dataPath = "/data/data/com.termux/files/home/Atmos/Atmos/Atmos/data.json"
	const logPath = "/data/data/com.termux/files/home/Atmos/Atmos/Atmos/alerts.log"

	// 3. Open Data Source
	file, err := os.Open(dataPath)
	if err != nil {
		fmt.Println("❌ No data.json found. Please run 'make sweep' to generate data.")
		return
	}
	defer file.Close()

	// 4. Prepare the Alert Log (Append Mode)
	logFile, err := os.OpenFile(logPath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Printf("❌ Could not open alert log: %v\n", err)
		return
	}
	defer logFile.Close()

	// 5. Process and Filter
	scanner := bufio.NewScanner(file)
	fmt.Printf("🔍 Filtering logs for Density < %.4f...\n", threshold)
	fmt.Println("--------------------------------------------------")

	matchCount := 0
	for scanner.Scan() {
		var d AtmosData
		if err := json.Unmarshal(scanner.Bytes(), &d); err != nil {
			continue // Skip malformed lines
		}

		if d.Density < threshold {
			matchCount++
			// Display to Terminal
			fmt.Printf("📍 MATCH [%s] | Alt: %.0fm | Density: %.4f\n", 
				d.Timestamp[:19], d.Altitude, d.Density)
			
			// Write to Permanent Alert Log
			logEntry := fmt.Sprintf("[%s] ALERT: Threshold %.4f exceeded | Alt: %.0fm | Density: %.4f\n", 
				d.Timestamp, threshold, d.Altitude, d.Density)
			logFile.WriteString(logEntry)
		}
	}

	// 6. Final Summary
	if matchCount > 0 {
		fmt.Println("--------------------------------------------------")
		fmt.Printf("✅ Success: %d anomalies exported to alerts.log\n", matchCount)
	} else {
		fmt.Println("⚪ No records found matching that threshold.")
	}
}

