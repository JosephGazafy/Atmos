package main

import (
    "fmt"
    "os"
    "time"
    probing "github.com/prometheus-community/pro-bing"
)

func main() {
    // UPDATED: Optimized for US-East Anchor
    pinger, err := probing.NewPinger("1.1.1.1") 
    if err != nil {
        fmt.Printf("⚠️ ERROR: %v\n", err)
        os.Exit(1)
    }
    
    pinger.SetPrivileged(true)
    peak := 100 * time.Millisecond

    pinger.OnRecv = func(pkt *probing.Packet) {
        if pkt.Rtt < peak {
            peak = pkt.Rtt
        }
        // Calculation of Variance relative to the 32ms baseline
        fmt.Printf("📡 Heartbeat: %v | Δ: %.2f\n", pkt.Rtt, float64(pkt.Rtt)/float64(peak))
    }

    pinger.Run()
}

