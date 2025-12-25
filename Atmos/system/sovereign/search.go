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
		fmt.Println("Usage: make search D=[THRESHOLD]")
		return
	}

	threshold, _ := strconv.ParseFloat(os.Args[1], 64)
	dataPath := "data.json"
	logPath := "alerts.log"

	// Open data source
	file, err := os.Open(dataPath)
ALERT_COUNT=$(wc -l < alerts.log 2>/dev/null || echo "0")
sed -i "s/Status:.*/Status:     OPERATIONAL (Alerts: $ALERT_COUNT)/" welcome.txt
	if err != nil {
		fmt.Println("❌ No data.json found. Run 'make sweep' first.")
		return
	}
	defer file.Close()

	// Open or create alerts.log in Append mode
	logFile, _ := os.OpenFile(logPath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	defer logFile.Close()

	scanner := bufio.NewScanner(file)
	fmt.Printf("🔍 Filtering Density < %.4f...\n", threshold)

	matchCount := 0
	for scanner.Scan() {
		var d AtmosData
		json.Unmarshal(scanner.Bytes(), &d)
		if d.Density < threshold {
			matchCount++
			entry := fmt.Printf("📍 Match: Alt %.0fm | Density %.4f\n", d.Altitude, d.Density)
			// Write to the alert log
			logFile.WriteString(fmt.Sprintf("[%s] ALERT: Alt %.0fm | Density %.4f\n", d.Timestamp, d.Altitude, d.Density))
		}
	}

	if matchCount > 0 {
		fmt.Printf("✅ %d matches exported to %s\n", matchCount, logPath)
	} else {
		fmt.Println("⚪ No anomalies detected.")
	}
}

