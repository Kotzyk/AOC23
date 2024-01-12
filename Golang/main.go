package main

import (
	"github.com/Kotzyk/AOC2023/Day1"
	"github.com/Kotzyk/AOC2023/helpers"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup

	var input = helpers.ReadFileIntoArray("../Inputs/day1.txt")
	wg.Add(2)
	defer helpers.TimeTrack(time.Now(), "Day1.Part1")

	go Day1.PartOne(input, &wg)
	defer helpers.TimeTrack(time.Now(), "Day1.Part2")

	go Day1.PartTwo(input, &wg)

	wg.Wait()
}
