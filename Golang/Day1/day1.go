package Day1

import (
	"fmt"
	"sync"
	"unicode"
)

var digitWordMap = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

// GetCalibrationValue Solution will be using linear searching since input
// strings are <50 characters and regexp is expensive
func getCalibrationValue(line string, parseDigitsFromWords bool) int {
	digits := make([]int, 0)
	for pos := 0; pos < len(line); pos++ {
		c := rune(line[pos])
		if unicode.IsDigit(c) {
			digits = append(digits, int(c-'0'))
			continue
		}

		if !parseDigitsFromWords {
			continue
		}

		isDigit, digit, offset := isDigitWord(pos, line)
		if !isDigit {
			continue
		}

		digits = append(digits, digit)
		pos += offset
	}

	if len(digits) == 1 {
		return digits[0]*10 + digits[0]
	}
	return digits[0]*10 + digits[len(digits)-1]
}

func isDigitWord(startPos int, line string) (bool, int, int) {
	for offset := 0; offset <= 5; offset++ {
		if len(line) < startPos+offset {
			break
		}
		var check = line[startPos : startPos+offset]
		if digitVal, ok := digitWordMap[check]; ok {
			return true, digitVal, offset - 1
		}
	}
	return false, -1, -1
}
func PartOne(input []string, wg *sync.WaitGroup) int {
	if wg != nil {
		defer wg.Done()
	}

	var total = 0
	for _, line := range input {
		total += getCalibrationValue(line, false)
	}
	fmt.Println("Day1.Part1: ", total)
	return total
}
func PartTwo(input []string, wg *sync.WaitGroup) int {
	if wg != nil {
		defer wg.Done()
	}

	var total = 0
	for _, line := range input {
		total += getCalibrationValue(line, true)
	}
	fmt.Println("Day1.Part2: ", total)
	return total
}
