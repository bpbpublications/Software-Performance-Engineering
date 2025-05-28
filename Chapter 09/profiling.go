package main

import (
	"fmt"
	"math/rand"
	"net/http"
	_ "net/http/pprof"
	"os"
	"runtime/pprof"
	"time"
)

func main() {
	// Expose pprof HTTP endpoints
	go func() {
		fmt.Println("Starting pprof server on http://localhost:6060")
		http.ListenAndServe("localhost:6060", nil)
	}()

	// Simulate low-performance code
	for i := 0; i < 1000000; i++ {
		// Introduce artificial delay to simulate low performance
		time.Sleep(time.Duration(rand.Intn(10)) * time.Millisecond)
		// Perform some CPU-bound computation
		_ = expensiveComputation()
	}

	// Generate heap profile
	hf, err := os.Create("heap_profile.prof")
	if err != nil {
		fmt.Println("Error creating heap profile:", err)
		return
	}
	defer hf.Close()
	if err := pprof.WriteHeapProfile(hf); err != nil {
		fmt.Println("Error writing heap profile:", err)
		return
	}

	fmt.Println("Program execution complete")
}

func expensiveComputation() int {
	// Simulate CPU-bound computation
	result := 0
	for i := 0; i < 10000; i++ {
		result += i
	}
	return result
}