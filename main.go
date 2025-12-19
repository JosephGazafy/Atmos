package main
import (
    "fmt"
    "time"
    probing "github.com/prometheus-community/pro-bing"
)
func main() {
    pinger, _ := probing.NewPinger("8.8.8.8")
    pinger.SetPrivileged(true)
    peak := 100 * time.Millisecond
    pinger.OnRecv = func(pkt *probing.Packet) {
        if pkt.Rtt < peak { peak = pkt.Rtt }
        fmt.Printf("📡 Heartbeat: %v | Δ: %.2f\n", pkt.Rtt, float64(pkt.Rtt)/float64(peak))
    }
    pinger.Run()
}

