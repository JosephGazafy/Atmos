// Snippet for main.go
import (
    "math/rand"
    "time"
)

func jitterSleep() {
    // Random delay between 45s and 75s to mask the 60s average
    delay := 45 + rand.Intn(30)
    time.Sleep(time.Duration(delay) * time.Second)
}


