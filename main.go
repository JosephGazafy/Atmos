cat << 'EOF' > ~/Atmos/main.go
package main

import (
	"fmt"
	"os"
	"time"
	probing "github.com/prometheus-community/pro-bing"
)

func main() {
	// 1. Determine Anchor: Use argument if provided, else default to Cloudflare
	anchor := "1.1.1.1"
	if len(os.Args) > 1 {
		anchor = os.Args[1]
	}

	pinger, err := probing.NewPinger(anchor)
	if err != nil {
		fmt.Printf("⚠️ ERROR: %v\n", err)
		os.Exit(1)
	}

	pinger.SetPrivileged(true)
	peak := 100 * time.Millisecond

	fmt.Printf("[*] ATMOS ANCHOR SET TO: %s\n", anchor)

	pinger.OnRecv = func(pkt *probing.Packet) {
		if pkt.Rtt < peak {
			peak = pkt.Rtt
		}
		// Dynamic Variance Calculation
		fmt.Printf("📡 Heartbeat: %v | Δ: %.2f\n", pkt.Rtt, float64(pkt.Rtt)/float64(peak))
	}

	pinger.Run()
}
EOF

# Recompile the binary for the local environment
go build -o main main.go

